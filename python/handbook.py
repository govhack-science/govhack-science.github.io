import sys
import io
import requests
# import json
#import urllib2
import frontmatter
import yaml

# consts
chapters_dir = "handbook/_chapters"

def save_markdown_file( doc ):
    with io.open("%s/%s.md" % ( chapters_dir, doc["fileName"] ), "w", encoding="utf-8") as f:
        f.write(u'---\n')
        
        f.write(unicode("slug: '%s'" % ( doc["fileName"] )))
        f.write(u'\n')
        
        f.write(unicode("title: '%s'" % ( doc["title"] )))
        f.write(u'\n')
        
        f.write(unicode("last_updated: '%s'" % ( doc["lastUpdated"] )))
        f.write(u'\n')
        
        if 'categories' in doc:
            f.write(u'categories:\n')
            # f.write(unicode("  - %s" % ( doc['categories'] )))
            # f.write(u'\n')
            for category in doc['categories']:
                f.write(unicode("  - %s" % ( category )))
                f.write(u'\n')
        
        if 'tags' in doc:
            f.write(u'tags:\n')
            for tag in doc['tags']:
                f.write(unicode("  - %s" % ( tag )))
                f.write(u'\n')
        
        f.write(u'---\n')
        f.write(u'\n')
        
        f.write(unicode(doc["content"]))
        f.write(u'\n')

# Endpoint for dumping comp stuff. Unauthenticated. Thank you based google docs script webapp.
# https://script.google.com/macros/s/AKfycbxU0RI14fAzSK5pHC6ibx9gVfX96mxnA8KbujmQDmi5tjPn_n5F/exec

# Get the latest API
# This takes a couple of seconds...
# Then parse through and save each doc as an em-dee

try:
    print "Retrieving handbook content..."
    resp = requests.post("https://script.google.com/macros/s/AKfycbxU0RI14fAzSK5pHC6ibx9gVfX96mxnA8KbujmQDmi5tjPn_n5F/exec")
    docs = resp.json()
except:
    print "Couldn't read JSON, check the source"
    sys.exit(1);
    
# Proceed...
    
for doc in docs: 
    print "Saving %s/%s.md" % ( chapters_dir, doc["fileName"] )
    save_markdown_file( doc )
    
print "Done."