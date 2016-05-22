import frontmatter
import json
import os

dirs = ["_dataportals", "_datasets", "_fields", "_jurisdictions", "_locations", "_mentors", "_organisations", "_prizes", "_themes"]
basepath = os.path.dirname(os.getcwd())

for dir in dirs:
  print "Processing %s" % (dir[1:])
  path = os.path.join(basepath, dir)
  jsonbasepath = os.path.join(basepath, "feed", dir[1:]) # Trim the leading underscore
  
  if not os.path.exists(jsonbasepath):
    print "Initialising directory"
    os.makedirs(jsonbasepath)
  
  for dirpath, dirnames, files in os.walk(path):
    for f in files:
      if f.endswith(".md"):
        print "Creating %s" % (f)
        jsonpath = os.path.join(jsonbasepath, f.replace(".md", ".json"))
        post = frontmatter.load(os.path.join(dirpath, f))
        with open(jsonpath, "w") as outfile:
          json.dump(post.metadata, outfile)
  
  print