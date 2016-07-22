import frontmatter
import json
import os
import markdown2

# dirs = ["_dataportals", "_datasets", "_fields", "_jurisdictions", "_locations", "_mentors", "_organisations", "_themes", "_prizes"]
dirs = ["_jurisdictions", "_locations", "_organisations", "_prizes"]
basepath, pythondir = os.path.split(os.path.dirname(os.path.realpath(__file__)))
portalurl = "http://portal.govhack.org"

for dir in dirs:
  print "# Processing %s" % (dir[1:])
  path = os.path.join(basepath, dir)
  jsonbasepath = os.path.join(basepath, "feed", dir[1:]) # Trim the leading underscore
  jsonall = {
    "_locations": [],
    "_prizes": []
  }
  
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
          junk, dirname = os.path.split(dirpath)
          jsonblob["url"] = "%s/%s/%s/%s" % (portalurl, "locations", dirname, f.replace(".md", ".html"))
        
        # Include Markdown body
        if dir == "_prizes":
          if post.metadata["type"] is not None and post.metadata["type"].lower() == "spirit":
            continue

          jsonblob["body"] = markdown2.markdown(post.content)
          jsonblob["portal_url"] = "%s/%s/%s/%s" % (portalurl, "prizes/2016", post.metadata["jurisdiction"], f.replace(".md", ".html"))
        
        if "gid" in jsonblob:
          jsonblob["id"] = jsonblob["gid"]
          del jsonblob["gid"]
        
        with open(jsonpath, "w") as outfile:
          json.dump(jsonblob, outfile)
        
        if dir in jsonall:
          jsonall[dir].append(jsonblob)
    
  if dir in jsonall:
    print
    print "Creating all.json"
    
    jsonallpath = os.path.join(jsonbasepath, "all.json")
    with open(jsonallpath, "w") as outfile:
        json.dump(jsonall[dir], outfile)
  
  print