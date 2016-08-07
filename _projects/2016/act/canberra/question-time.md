---
category: ''
datasets_used:
- agency: Parliament of NSW
  name: Hansard - NSW Parliament
  url: http://data.nsw.gov.au/data/dataset/40e30b07-d32b-4717-89cf-8789fd54b123
- agency: Department of the Prime Minister and Cabinet
  name: NSW Suburb/Locality Boundaries - PSMA Administrative Boundaries
  url: https://data.gov.au/dataset/nsw-suburb-locality-boundaries-psma-administrative-boundaries/resource/0fea6eba-b9d4-4428-953b-a1cf87533aff
- agency: OpenStreetMap Foundation
  name: Open Street Map
  url: https://www.openstreetmap.org/
event: canberra
gid: question-time
hackerspace_url: https://2016.hackerspace.govhack.org/node/831
image_url: https://2016.hackerspace.govhack.org/sites/default/files/field/image/Screen%20Shot%202016-07-31%20at%2010.56.46%20AM.png
jurisdiction: act
prizes-entered:
- australia-creative-humanities-hack
- australia-location-data
- act-best-data-wrangling
project_title: Question Time
project_url: http://questiontime.xyz
repo:
  name: GitHub Repository
  type: github
  url: https://github.com/MatthewJA/govhack-2016
team_name: ''';-- -'
video:
  type: youtube
  url: https://youtu.be/hiblYDqgvew
---

Love Hansard but wish it was somehow represented on a map? So do we. That's why we created Question Time.
We love political banter, and we wanted to visualise how political debate occurs over time. For each day of the 2015 – 2016 NSW Parliament, Question Time visualises mentions of NSW suburbs found in the NSW Parliament Hansard with a heatmap of how unusually often each suburb was mentioned.
Question Time also identifies interesting places for each day Parliament sat. Clicking one of these locations shows a quick snippet of what we think made it interesting. 
We mined location data from the NSW Hansard using the API provided by the Parliament of NSW, and tallied each location mentioned on each day, taking note of where that location was mentioned in the Hansard fragments for later reference. Locations such as Sydney and Newcastle dominated the tallies, so we normalised all tallies by dividing by the average number of mentions per day across the whole 2015 – 2016 period. We then used the tallies to construct and display a heatmap over NSW using the OpenLayers 3 mapping library. For each day, we extracted interesting locations by looking for locations with unusually high numbers of mentions, and again used the NSW Hansard API to extract snippets of text about that location on that day. We then used the NLTK Python library along with github/@aneesha's implementation of the RAKE algorithm to highlight key phrases in these snippets and included these alongside the interesting locations to try and explain what made each location interesting. Finally, we built a web app to display the heatmap and interesting locations for each day.