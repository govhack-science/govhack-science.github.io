# -*- coding: utf-8 -*-

import fnmatch
import codecs
import tablib
import os
import requests
import urlparse
import shutil
import frontmatter
import yaml
import io
import validators
import re

# Config
csvfile = "python/data/projects/projects.csv"
projects_dir = "_projects/"
jurisdictions_dir = "_jurisdictions/"
eventsdir = "_locations/"
prizesdir = "_prizes/"
mentorimagesdir = "resources/images/mentors/"
gids = []

# For matching projects to jurisdictions
jurisdiction_names = []
jurisdiction_frontmatter = {}
for root, dirnames, filenames in os.walk(jurisdictions_dir):
    for filename in fnmatch.filter(filenames, "*.md"):
        post = frontmatter.load(os.path.join(jurisdictions_dir, filename))
        jurisdiction_names.append(post.metadata["name"])
        jurisdiction_frontmatter[post.metadata["name"]] = post.metadata

# For matching projects to events
event_names = []
event_frontmatter = {}
for root, dirnames, filenames in os.walk(eventsdir):
    for filename in fnmatch.filter(filenames, "*.md"):
        post = frontmatter.load(os.path.join(root, filename))
        event_names.append(post.metadata["name"].lower())
        event_frontmatter[post.metadata["name"].lower()] = post.metadata

# For matching projects to prizes
prize_names = []
prize_frontmatter = {}
for root, dirnames, filenames in os.walk(prizesdir):
    for filename in fnmatch.filter(filenames, "*.md"):
        post = frontmatter.load(os.path.join(root, filename))
        prize_names.append(post.metadata["name"].lower())
        post.metadata["path"] = os.path.join(root, filename)
        post.metadata["content"] = post.content
        prize_frontmatter[post.metadata["name"].lower()] = post.metadata

# For fixing inconsistencies in event names between Portal and Hackerspace
event_name_lookup = {
    "Canberra Heritage Hack": "heritage hack",
    "Melbourne": "melbourne official",
    "Brisbane Maker Node": "brisbane govhack maker node"
}

# For fixing inconsistencies in prize names between Portal and Hackerspace
prize_name_lookup = {
    "ABS - That thing we all need": "That thing we all need",
    u'Fresh Data Hack (API’s and Data Services)': "Fresh Data Hack (APIs and Data Services)",
    "Data Intelligence Hack": "Data Intelligence Hack (Data journalism, spatial modelling, analytics)",
    "Weather Forecast": "Weather Forecasts",
    "Supporing the Best of Brisbane": "Supporting the Best of Brisbane",
    "Helping small businesses make better decisions": "How can City of Melbourne data be used to help businesses make better decisions?",
    "Student Droput Rates": "Student Dropout Rates",
    "The Northern Agricultural Region Prize": "Sustainable Coastlines Prize",
    "Geospatial Prize": "Most Innovative Use Of Location-based Information Prize",
    "Land Use and Development": "Logan Land Use and Development"
}

# for k, v in enumerate(prize_name_lookup):
#     prize_name_lookup[]

with codecs.open(csvfile, "rb", encoding="utf-8") as f:
    csv = f.read().encode("utf-8")
  
data = tablib.Dataset()
data.csv = csv

# Group by project name first (multiple rows for each Project Image URL)
projects_by_name = {}
projects = []
for row in data.dict:
    if row["Project Title"] not in projects_by_name:
        projects_by_name[row["Project Title"]] = []
    projects_by_name[row["Project Title"]].append(row)

# The last entry for each project seems to be the one that has the
# Project Image URL actually used on the project, so discard the others.
for project_name, rows in projects_by_name.iteritems():
    projects.append(rows[-1])

for row in projects:
    # Skip unfinished projects
    if row["Project Status"] != "Submitted":
        continue
    
    # Log and skip incomplete projects
    if row["Video URL"] == "" and row["Video Upload"] == "":
        # print "WARNING: Project '%s' is incomplete! No video provided." % (row["Project Title"].strip())
        continue
    if row["Source URL"] == "":
        # print "WARNING: Project '%s' is incomplete! No repo provided." % (row["Project Title"].strip())
        continue
    # if row["Homepage/Demo URL"] == "":
        # print "WARNING: Project '%s' is incomplete! No homepage/demo provided." % (row["Project Title"].strip())
        # continue
    # continue

    # Assign our project a globally unique id
    gid = row["Project Title"].strip().lower().replace(" ", "-").replace("'", "").replace("?", "").replace("#", "")
    if gid in gids:
        raise ValueError("GID '%s' is not unique." % (gid))
    gids.append(gid)

    # print row["Project Title"].strip()

    project = {
        "project_title": row["Project Title"].strip(),
        "team_name": row["Team Name"].strip(),
        "repo": {
            "name": row["Evidence Repository Title"].strip(),
            "url": row["Source URL"].strip(),
        },
        "project_url": row["Homepage/Demo URL"].strip(),
        "hackerspace_url": row["Project URL"].strip(),
        "video": {
            "url": row["Video URL"].strip()
        }
    }

    # Set the project's jurisdiction
    region = row["Region"]
    if region == "West Australia": # Westralia shall be free!
        region = "Western Australia"

    if region not in jurisdiction_names:
        raise ValueError("Region '%s' is not valid." % (region))
    project["jurisdiction"] = jurisdiction_frontmatter[region]["gid"]

    # Set the project's local event
    event_name = row["Local Event State"]
    if event_name in event_name_lookup:
        event_name = event_name_lookup[event_name]

    if event_name.lower() not in event_names:
        raise ValueError("Event name '%s' is not valid." % (event_name))
    project["event"] = event_frontmatter[event_name.lower()]["gid"]

    # Set the project's image url
    # "image_url": row["Project Image URL"].strip(),
    if row["Project Image URL"] != "":
        image_url = row["Project Image URL"].strip().lower()
        r_image = re.compile(r".*\.(jpg|jpeg|png|gif)$")
        if r_image.match(image_url) != None:
            project["image_url"] = image_url

    # Set the alternate video URL (GovHack S3 hosted videos)
    if row["Video Upload"] != "":
        project["video"]["alt_url"] = row["Video Upload"]

    # Determine the video hosting service used
    if "youtube.com" in row["Video URL"] or "youtu.be" in row["Video URL"]:
        project["video"]["type"] = "youtube"
    elif "vimeo.com" in row["Video URL"]:
        project["video"]["type"] = "vimeo"
    elif "prezi.com" in row["Video URL"]:
        project["video"]["type"] = "prezi"
    elif "drive.google.com" in row["Video URL"]:
        project["video"]["type"] = "google-drive"
    elif "dropbox.com" in row["Video URL"]:
        project["video"]["type"] = "dropbox"
    elif "1drv.ms" in row["Video URL"]:
        project["video"]["type"] = "onedrive"
    else:
        project["video"]["type"] = "unknown"
    
    # Determine the source code hosting service used
    if "github.com" in row["Source URL"]:
        project["repo"]["type"] = "github"
    elif "gitlab.com" in row["Source URL"]:
        project["repo"]["type"] = "gitlab"
    elif "bitbucket.org" in row["Source URL"]:
        project["repo"]["type"] = "bitbucket"
    elif "drive.google.com" in row["Source URL"] or "docs.google.com" in row["Source URL"]:
        project["repo"]["type"] = "google-drive"
    elif "dropbox.com" in row["Source URL"]:
        project["repo"]["type"] = "dropbox"
    elif "arcgis.com" in row["Source URL"]:
        project["repo"]["type"] = "arcgis"
    elif "tableau.com" in row["Source URL"]:
        project["repo"]["type"] = "tableau"
    else:
        project["repo"]["type"] = "unknown"
    
    # Something something prizes
    if row["Prizes"] != "":
        # Skip NZ prizes for now. So many names don't match
        if project["jurisdiction"] == "nz":
            continue

        if "Data Intelligence Hack (Data journalism, spatial modelling, analytics)" in row["Prizes"]:
            row["Prizes"] = row["Prizes"].replace(" (Data journalism, spatial modelling, analytics)", "")

        project["prizes"] = []
        prizes = row["Prizes"].split(", ")
        for prize in prizes:
            if prize in prize_name_lookup:
                prize = prize_name_lookup[prize]

            if "International Prize: " in prize:
                prize = prize.replace("International Prize: ", "")

            if prize.lower() not in prize_names:
                raise ValueError("Prize name '%s' is not valid." % (prize))
            project["prizes"].append(prize_frontmatter[prize.lower()]["gid"])

            # Give prizes a list of their associated projects too
            if "projects" not in prize_frontmatter[prize.lower()]:
                prize_frontmatter[prize.lower()]["projects"] = []
            prize_frontmatter[prize.lower()]["projects"].append(gid)

    # Something something datasets
    if row["Used Datasets"] != "":
        project["datasets_used"] = []
        datasets = row["Used Datasets"].split("\n")
        for dataset in datasets[:-1]:
            dataset_idents, dataset_url = dataset.split(" @ ", 1)
            dataset_name, agency_name = dataset_idents.split(" [", 1)

            project["datasets_used"].append({
                "name": dataset_name.strip(),
                "url": dataset_url.strip(),
                "agency": agency_name[:-1].strip()
            })

    project_md_dir = os.path.join(projects_dir, "2016", project["jurisdiction"], project["event"])
    project_md_file = os.path.join(project_md_dir, "%s.md" % (gid))
    
    # continue
    if not os.path.exists(project_md_dir):
        os.makedirs(project_md_dir)

    with io.open(project_md_file, "w", encoding="utf-8") as f:
        f.write(u'---\n')
        f.write(unicode(yaml.safe_dump(project, width=200, default_flow_style=False, encoding="utf-8", allow_unicode=True), "utf-8"))
        f.write(u'---\n')
        f.write(u'\n')
        f.write(row["Project Description"].strip())


# Now attach project gids to prizes
for prize_name, fm in prize_frontmatter.iteritems():
    if "projects" in fm:
        path = fm["path"]
        content = fm["content"]
        del fm["path"]
        del fm["content"]
        # print fm
        continue

        with io.open(path, "w", encoding="utf-8") as f:
            f.write(u'---\n')
            f.write(unicode(yaml.safe_dump(fm, width=200, default_flow_style=False, encoding="utf-8", allow_unicode=True), "utf-8"))
            f.write(u'---\n')
            f.write(u'\n')
            f.write(content)


print "> Fin"
print
print "NEXT STEPS:"
print "  1. Review the log for any WARNINGS you can resolve."
print "  2. Load mentors.html on your local version of Jekyll and validate that the mentor profiles look OK."
print "  3. Commit!"