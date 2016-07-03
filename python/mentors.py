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

# Config
csvfile = "python/data/mentors_20160703_formstack.csv"
mentorsdir = "_mentors/"
organisationsdir = "_organisations/"
eventsdir = "_locations/"
mentorimagesdir = "resources/images/mentors/"
tmpdir = "python/tmp/"

# Init
if not os.path.exists(tmpdir):
    os.makedirs(tmpdir)

# For seeing if the mentor's organisations exists
organisation_names = []
for root, dirnames, filenames in os.walk(organisationsdir):
    for filename in fnmatch.filter(filenames, "*.md"):
        organisation_names.append(filename.split(".")[0])

# For matching mentors to events
event_names = []
event_md_files = {}
for root, dirnames, filenames in os.walk(eventsdir):
    for filename in fnmatch.filter(filenames, "*.md"):
        event_name = filename.split(".")[0]
        event_names.append(event_name)
        event_md_files[event_name] = os.path.join(root, filename)

with codecs.open(csvfile, "rb", encoding="iso-8859-1") as f:
    csv = f.read().encode("utf-8")
  
data = tablib.Dataset()
data.csv = csv
new_mentors_count = 0

for row in data.dict:
    # Skip empty rows populated by the export process
    if row["Time"] == "":
        continue
    
    # Skip test user
    if row["Email"] == "testing@123.com":
        continue

    # Assign our mentor a globally unique id
    name = "%s %s" % (row["Name (First)"], row["Name (Last)"])
    gid = name.lower().replace(" ", "-")

    # if gid != "claire-sainsbury":
    #     continue

    # Create records for mentors who haven't been processed yet
    if not os.path.exists(mentorsdir + "%s.md" % (gid)):
        new_mentors_count += 1
        print name

        mentor = {
            "name": name,
            "gid": gid,
            "type": row["What type of mentor are you?"],
            "position_title": row["Job title"],
            "ask_me_about": row["What can people ask you about? (in a sentence)"],
            "organisation": row["Agency/Organisation"],
            "jurisdiction": row["What state or territory do you reside in?"].lower(),
            "contact": {
                "email": row["Email"]
            }
        }

        organisation_gid = row["Agency/Organisation"].lower().replace(" ", "-").replace(",", "")
        if organisation_gid in organisation_names:
            mentor["organisation"] = organisation_gid
        else:
            print "WARNING: Could not resolve organisation: %s" % (row["Agency/Organisation"])
            print organisation_gid

        if len(row["Photograph URL"]) > 0:
            # Download and stash the mentor image locally
            r = requests.get(row["Photograph URL"], stream=True)
            if r.status_code == 200:
                # Hacky, should use actual mimetype
                path = urlparse.urlparse(row["Photograph URL"]).path
                fileext = os.path.splitext(path)[1]

                mentor_image_path = mentorimagesdir + "%s%s" % (gid, fileext)
                with open(mentor_image_path, 'wb') as f:
                    r.raw.decode_content = True
                    shutil.copyfileobj(r.raw, f) 
                    mentor["photo_url"] = "/" + mentor_image_path

        if len(row["Twitter Handle"]) > 0:
            mentor["contact"]["twitter"] = row["Twitter Handle"]

        if len(row["Who are you on LinkedIn?"]) > 0:
            mentor["contact"]["linkedin"] = row["Who are you on LinkedIn?"]
        
        events = ["ACT", "NSW", "NT", "QLD", "SA", "TAS", "VIC", "WA"]
        found_event = False
        for event in events:
            col_name = "GovHack %s Events" % (event)
            if len(row[col_name]) > 0:
                found_event = True
                event_gid = row[col_name].lower().replace(" ", "-").replace("-official-event", "")
                
                if event_gid in event_names:
                    print "Attending Event: %s" % (event_gid)

                    post = frontmatter.load(event_md_files[event_gid])
                    mentor["location"] = post.metadata["gid"]
                    
                    if post.metadata["gid"] != event_gid:
                        print "WARNING: Event .md file does not match event gid. %s, %s" % (event_gid, post.metadata["gid"])
                else:
                    print "WARNING: Could not find region '%s' in list of regions." % (event_gid)
        
        if found_event == False:
            print "WARNING: Mentor did not say which event they're attending."
            print "Attending event: %s" % (row["Which event will you be attending?"])

        print

        # continue
        # with io.open(tmpdir + "%s.md" % (gid), "w", encoding="utf-8") as f:
        with io.open(mentorsdir + "%s.md" % (gid), "w", encoding="utf-8") as f:
            f.write(u'---\n')
            f.write(unicode(yaml.safe_dump(mentor, width=200, default_flow_style=False, encoding="utf-8", allow_unicode=True), "utf-8"))
            f.write(u'---\n')
            f.write(u'\n')
            f.write(row["Tell us a bit about yourself"])

if new_mentors_count == 0:
    print "No new mentors were found!"
    print "Mentors in CSV: %s" % (len(data.dict))
else:
    print "> Fin"
    print "> %s mentors were created" % (new_mentors_count)
    print
    print "NEXT STEPS:"
    print "  1. Review the log for any WARNINGS you can resolve."
    print "  2. Load mentors.html on your local version of Jekyll and validate that the mentor profiles look OK."
    print "  3. Commit!"