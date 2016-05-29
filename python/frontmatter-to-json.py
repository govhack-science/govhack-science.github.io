import frontmatter
import json
import os

dirs = ["_dataportals", "_datasets", "_fields", "_jurisdictions", "_locations", "_mentors", "_organisations", "_prizes", "_themes"]
basepath, pythondir = os.path.split(os.path.dirname(os.path.realpath(__file__)))
portalurl = "http://portal.govhack.org"

for dir in dirs:
  print "# Processing %s" % (dir[1:])
  path = os.path.join(basepath, dir)
  jsonbasepath = os.path.join(basepath, "feed", dir[1:]) # Trim the leading underscore
  jsonall = []
  
  if not os.path.exists(jsonbasepath):
    print "Initialising directory %s" % (jsonbasepath)
    os.makedirs(jsonbasepath)
  
  for dirpath, dirnames, files in os.walk(path):
    for f in files:
      if f.endswith(".md"):
        print "Creating %s" % (f)
        jsonpath = os.path.join(jsonbasepath, f.replace(".md", ".json"))
        post = frontmatter.load(os.path.join(dirpath, f))
        jsonblob = post.metadata
        
        # Generate a URL for locations for www to use
        if dir == "_locations":
          basepath, dirname = os.path.split(dirpath)
          jsonblob["url"] = "%s/%s/%s/%s" % (portalurl, "locations", dirname, f.replace(".md", ".html"))
        
        with open(jsonpath, "w") as outfile:
          json.dump(jsonblob, outfile)
        
        jsonall.append(jsonblob)
    
  if dir == "_locations":
    print
    print "Creating all.json"
    
    jsonallpath = os.path.join(jsonbasepath, "all.json")
    with open(jsonallpath, "w") as outfile:
        json.dump(jsonall, outfile)
  
  print