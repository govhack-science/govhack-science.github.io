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
import ckanapi
import urlparse

class CKANLookup(object):
    """
    """

    def __init__(self, dataset_url):
        self.dataset_url = dataset_url

    def get_ckan_url(self):
        idx = self.dataset_url.find("dataset")
        if idx != -1:
            api_root_url = self.dataset_url[0:idx]
        else:
            api_root_url = urlparse.urljoin(self.dataset_url, "/")
        
        if api_root_url.endswith("/") == True:
            api_root_url = api_root_url[:-1]
        return api_root_url

    def is_ckan_url(self):
        api_root_url = self.get_ckan_url() + "/api/3"
        r = requests.get(api_root_url)
        if r.status_code == 200:
            return True
        else:
            return False

    def get_endpoint(self):
        api_root_url = self.get_ckan_url()
        return ckanapi.RemoteCKAN(api_root_url, user_agent="GovHackCKANService/1.0")

    def get_package_name(self):
        parse_object = urlparse.urlsplit(self.dataset_url)
        idx = parse_object.path.find("/dataset/")
        if idx != -1:
            return parse_object.path[idx + len("/dataset/"):]
        else:
            raise ValueError("Could not determine CKAN package name: %s" % (self.dataset_url))
    
    def get_package(self):
        endpoint = self.get_endpoint()
        package_name = self.get_package_name()
        package = endpoint.action.package_show(id=package_name)
        return package
        

# http://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks-in-python
def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in xrange(0, len(l), n):
        yield l[i:i+n]

# Config
csvfile = "python/data/datasets/datasets_formstack.csv"
org_lookup = "python/data/datasets/org_lookup.csv"
event_lookup = "python/data/datasets/event_lookup.csv"
datasetsdir = "_datasets/2016/"
organisationsdir = "_organisations/"
eventsdir = "_locations/"
tmpdir = "python/tmp/"
excerpt_separator = "<!--more-->"

# Init
if not os.path.exists(tmpdir):
    os.makedirs(tmpdir)

# For seeing if the dataset's organisations exists
organisation_names = []
for root, dirnames, filenames in os.walk(organisationsdir):
    for filename in fnmatch.filter(filenames, "*.md"):
        organisation_names.append(filename.split(".")[0])

# For matching datasets to events
event_names = []
event_md_files = {}
for root, dirnames, filenames in os.walk(eventsdir):
    for filename in fnmatch.filter(filenames, "*.md"):
        event_name = filename.split(".")[0]
        event_names.append(event_name)
        event_md_files[event_name] = os.path.join(root, filename)

# For seeing if the dataset's gid is in use
# @TODO Make this work across years
dataset_gids = []
for root, dirnames, filenames in os.walk(datasetsdir):
    for filename in fnmatch.filter(filenames, "*.md"):
        dataset_gids.append(filename.split(".")[0])

# For org lookup to workaround submissions using non-standard org names
with codecs.open(org_lookup, "rb", encoding="iso-8859-1") as f:
    csv = f.read().encode("utf-8")
  
org_lookup = tablib.Dataset()
org_lookup.csv = csv

org_lookup_table = {}
for row in org_lookup:
    org_lookup_table.update({row[0]: row[1]})

# For event lookup to workaround submissions using non-standard event names
with codecs.open(event_lookup, "rb", encoding="iso-8859-1") as f:
    csv = f.read().encode("utf-8")
  
event_lookup = tablib.Dataset()
event_lookup.csv = csv

event_lookup_table = {}
for row in event_lookup:
    event_lookup_table.update({row[0]: row[1]})

# For deprecated events
deprecated_events = ["Manly Northern Beaches", "Newcastle"]

# Open form submissions
with codecs.open(csvfile, "rb", encoding="iso-8859-1") as f:
    csv = f.read().encode("utf-8")

data = tablib.Dataset()
data.csv = csv
new_datasets_count = 0

for row in data:
    # Skip empty rows populated by the export process
    if row[0] == "":
        continue

    dataset_stub = {"excerpt_separator": excerpt_separator}
    event_locations = []
    found_event = False
    
    submission = {
        "Time": row[0],
        "Name (First)": row[1],
        "Name (Last)": row[2],
        "Email": row[3],
        "Agency/Organisation": row[4],
        "Jurisdiction": row[5],
        "Region": row[6],
        "GovHack Events": row[7],
        "GovHack ACT Events": row[8],
        "GovHack NSW Events": row[9],
        "GovHack VIC Events": row[10],
        "GovHack NT Events": row[11],
        "GovHack QLD Events": row[12],
        "GovHack SA Events": row[13],
        "GovHack TAS Events": row[14],
        "GovHack WA Events": row[15],
        "Number of datasets": row[16]
    }

    print "%s %s" % (submission["Name (First)"], submission["Name (Last)"])

    # Requirement: Find a valid organisation to link this dataset to
    organisation_gid = submission["Agency/Organisation"].lower().strip().replace(" ", "-").replace(",", "")
    if organisation_gid in organisation_names:
        print "FOUND %s" % (organisation_gid)
    elif submission["Agency/Organisation"] in org_lookup_table:
        organisation_gid = org_lookup_table[submission["Agency/Organisation"]]
        print "FOUND %s" % (organisation_gid)
    else:
        print "WARNING: Could not resolve organisation: %s" % (submission["Agency/Organisation"])
        print organisation_gid
        print "SKIPPING!"
        continue

    # Process the events to link these datasets to
    if submission["Jurisdiction"] == "Australian Government":
        dataset_stub["jurisdiction"] = "australia"
    else:
        dataset_stub["jurisdiction"] = submission["Region"].lower()
        events = ["ACT", "NSW", "NT", "QLD", "SA", "TAS", "VIC", "WA"]

        for event in events:
            col_name = "GovHack %s Events" % (event)
            if len(submission[col_name]) > 0:
                for event_name in submission[col_name].split("|"):
                    if event_name in deprecated_events:
                        # print "NOTICE: Skipping deprecated event %s" % (event_name)
                        continue
                    
                    if event_name not in event_lookup_table:
                        event_gid = event_name.lower().replace(" ", "-").replace("-official-event", "")
                    else:
                        event_gid = event_lookup_table[event_name]

                    if event_gid in event_names:
                        # print "Attending Event: %s" % (event_gid)

                        post = frontmatter.load(event_md_files[event_gid])
                        event_locations.append(post.metadata["gid"])
                        
                        if post.metadata["gid"] != event_gid:
                            print "WARNING: Event .md file does not match event gid. %s, %s" % (event_gid, post.metadata["gid"])
                    else:
                        print "WARNING: Could not find event '%s' in list of events." % (event_gid)
                
                break
            
        if(len(event_locations) > 0):
            found_event = True
        
        if found_event == False:
            print "WARNING: Events not provided. Skipping"
            continue
        else:
            dataset_stub["events"] = event_locations

    print
    # print dataset_stub

    # Magic - The dataset info starts at position, and the last 5 fields are irrelevant
    num_datasets = int(1 if submission["Number of datasets"] == "" else int(submission["Number of datasets"]))
    print "# Number of Datasets: %s" % (num_datasets)
    print

    for key, item in enumerate(chunks(row[17:-5], 4)):
        if key >= num_datasets:
            break

        dataset_url = item[0]
        dataset_name = item[1].strip()
        dataset_description = item[2].replace("|", "\n").strip()

        # Let's use the CKAN API to pull extra info about the dataset
        if dataset_name == "":
            ckan = CKANLookup(dataset_url)
            if ckan.is_ckan_url():
                package = ckan.get_package()
                dataset_name = package["title"].strip()
                dataset_description = package["notes"].strip()
            else:  
                print "WARNING: Doesn't look like CKAN. Is this a dataset?"
                print dataset_url
                continue

        # Description to excerpt
        # (For some reason automatic excerpt generation failed.)
        dataset_description = dataset_description.strip()
        idx = dataset_description.find("\n")
        if idx != -1:
            dataset_excerpt = dataset_description[0:idx].strip()
            dataset_description_remain = dataset_description[idx:].strip()
            dataset_description = dataset_excerpt + "\n\n" + excerpt_separator + "\n\n" + dataset_description_remain

        # Assign our dataset a globally unique id
        dataset_gid = dataset_name.lower().replace(" ", "-").replace("'", "")

        dataset_md_dir = os.path.join(datasetsdir, dataset_stub["jurisdiction"])
        dataset_md_file = os.path.join(dataset_md_dir, "%s.md" % (dataset_gid))

        # Create records for datasets who haven't been processed yet
        if not os.path.exists(dataset_md_file):
            if dataset_gid in dataset_gids:
                raise ValueError("WARNING: GID '%s' is already in use elsewhere." % (dataset_gid))
            else:
                dataset_gids.append(dataset_gid)

            new_datasets_count += 1
            print "## Processing Dataset %s" % (key)
            print dataset_name

            dataset = dataset_stub.copy()
            dataset["gid"] = dataset_gid
            dataset["name"] = dataset["title"] = dataset_name
            dataset["dataset_url"] = dataset_url
            dataset["organisation"] = organisation_gid
            if len(event_locations) > 0:
                dataset["events"] = event_locations

            if not os.path.exists(dataset_md_dir):
                os.makedirs(dataset_md_dir)

            # continue
            with io.open(dataset_md_file, "w", encoding="utf-8") as f:
                f.write(u'---\n')
                f.write(unicode(yaml.safe_dump(dataset, width=200, default_flow_style=False, encoding="utf-8", allow_unicode=True), "utf-8"))
                f.write(u'---\n')
                f.write(u'\n')
                f.write(dataset_description.rstrip())
    
    print
    print "---"
    print
    continue

if new_datasets_count == 0:
    print "No new datasets were found!"
    print "Submissions in CSV: %s" % (len(data.dict))
else:
    print "> Fin"
    print "> %s datasets were created" % (new_datasets_count)
    print
    print "NEXT STEPS:"
    print "  1. Review the log for any WARNINGS you can resolve."
    print "  2. Load datasets.html on your local version of Jekyll and validate that the dataset profiles look OK."
    print "  3. Commit!"