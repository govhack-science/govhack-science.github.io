---
category: ''
datasets_used:
- agency: Department of Industry, Innovation and Science
  name: SA3 Region Innovation Data 2009-15
  url: https://data.gov.au/dataset/sa3-region-innovation-data
- agency: Bioregional Assessment Programme
  name: ABS Boundaries 2011
  url: https://data.gov.au/dataset/8b65c3a4-7010-4a79-8eaa-5621b750347f
event: canberra
hackerspace_url: https://2016.hackerspace.govhack.org/node/2246
image_url: https://2016.hackerspace.govhack.org/sites/default/files/field/image/Screen%20Shot%202016-07-31%20at%207.53.39%20pm.png
jurisdiction: act
prizes-entered:
- australia-future-australia-hack
- australia-innovative-ideas-hack
- australia-inspired-by-research-hack
- australia-local-industry-activity
- act-best-data-wrangling
project_title: The Grid
project_url: http://hughevans.net/the-grid/
repo:
  name: Github
  type: github
  url: https://github.com/hughevans/the-grid
team_name: ISOs
video:
  type: youtube
  url: https://youtu.be/WwhjQujamJk
---

Isometric representations of industry data on grids that represent the actual shape files - states and SA3 zones.
I had to first parse the Innovation SA3 data and calculate the number of tiles and their colour for each one:
Blue: Office jobs/commercialRed: Health, education, public administration and artsYellow: Industry and wholesaleBlack: MiningGreen: Agriculture
Working back from the point that I wanted the maximum amount of tiles to be ~300 (which is the SA3 zone Sydney Inner City and the state of NSW) I caculated each other one in relation to that - allowing you to compare zones and states.
Then I needed to create a tile matrix based on the shape files… So I busted up the larger shape files into individual ones. Then I created a point grid that covered the entire shape. I then discarded the points that fell outside the boundry. I used the fantastic Turf library from Mapbox to help with this.
Now I needed to visualise these matrices along with their proportional colours. I did that with a little React JS app and the Isomer JS library.