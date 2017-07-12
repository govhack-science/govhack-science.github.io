import fnmatch
import os
import io

# Config
prizesdir = "_prizes/2016/"
organisationsdir = "_organisations/"
eventsdir = "_locations/"

# Organisation names
organisation_names = []
for root, dirnames, filenames in os.walk(organisationsdir):
    for filename in fnmatch.filter(filenames, "*.md"):
        organisation_names.append(filename.split(".")[0])

# Event names
event_names = []
event_md_files = {}
for root, dirnames, filenames in os.walk(eventsdir):
    for filename in fnmatch.filter(filenames, "*.md"):
        event_name = filename.split(".")[0]
        event_names.append(event_name)
        event_md_files[event_name] = os.path.join(root, filename)

for event in sorted(event_names):
    print event.replace("-", " ").title()