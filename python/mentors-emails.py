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

# Config
csvfile = "python/data/mentors/mentors_formstack.csv"
mentorsdir = "_mentors/"
organisationsdir = "_organisations/"
eventsdir = "_locations/"
mentorimagesdir = "resources/images/mentors/"
tmpdir = "python/tmp/"

# For seeing if the mentor's organisations exists
mentors_emails = []
for root, dirnames, filenames in os.walk(mentorsdir):
    for filename in fnmatch.filter(filenames, "*.md"):
        post = frontmatter.load(os.path.join(mentorsdir, filename))
        if "email" in post.metadata["contact"]:
            names = post.metadata["name"].split(" ")
            first_name = names[0]
            last_name = " ".join(names[1:])
            print "%s,%s,%s" % (post.metadata["contact"]["email"], first_name, last_name)
