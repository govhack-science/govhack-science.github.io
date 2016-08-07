---
category: ''
event: melbourne-open-raster
hackerspace_url: https://2016.hackerspace.govhack.org/node/786
image_url: https://2016.hackerspace.govhack.org/sites/default/files/field/image/logo_1.jpg
jurisdiction: vic
prizes:
- australia-creative-humanities-hack
- australia-storytelling-hack
- australia-transport-data
- vic-mav-technology-bounty
- vic-parks-vic--experience
- vic-the-regional-challenge
- vic-vic-map-features-of-interest
project_title: PsychedelicProsthetic
project_url: https://psypro.shinyapps.io/govhack2016/
repo:
  name: My Livability
  type: github
  url: https://github.com/mrjoh3/govhack2016
team_name: PsychedelicProsthetic
video:
  type: youtube
  url: https://www.youtube.com/watch?v=Hn3F4EHCLw4
---

Problem
- Liveability means something unique to everyone.
- It's your story, but you can't tell it at the moment
- Liveability rankings exist for Melbourne, but in such a diverse state, how do you know which area suits you best? Would a Weekend in Warrnambool suit you best, or or maybe a lifetime?
Solution
We're giving you the opportunity to interact with a range of government (and some non-government) data to find where's best for you based on your own preferences. You specify your preferences, and we give you a ranking of urban and regional suburbs that we think sound right for you.  We even have some ideas for what you might like to do when you arrive. 
Future Opportunities
Integrate more data, and better data.
Refine the ability of our algorithm to better define liveability based on your feedback.
Provide information to local councils to show them what they're doing well, and help them improve to attract both visitors and future  residents.
Collect data over time to create personalised stories for users, showing how their preferences and values change over time.
Aggregate users' preferences to determine whether values tend to converge or diverge, which could inform official liveability metrics in the future.
Team
Matthew Johnson
Andrew Marshall
Valerio Bisignanesi
Luke Wilson​​​​​​​
Datasets used
https://www.data.vic.gov.au/data/dataset/vicmap-lite-public-land-parks-and-reserves-1-1-million-to-1-5-million
-          Vicmap Lite - Public Land (Parks and Reserves) 1:1 million to 1:5 million
-          All layers (national parks and state parks etc)
https://www.data.vic.gov.au/data/dataset/foi-polygon-vicmap-features-of-interest
-          Vicmap Features of Interest
-          Parks & gardens
 Feature Type: Reserve
 Feature subtype: amusement centre; park; city square; zoo; gardens
http://www.abs.gov.au/AUSSTATS/abs@.nsf/DetailsPage/1270.0.55.003July%202011?OpenDocument
-          State suburbs and LGAs
https://www.data.vic.gov.au/data/dataset/sport-and-recreational-facilities
-          Sport and Recreation Facilities
https://www.data.vic.gov.au/data/dataset/vicmap-transport-road-network
-          Vicmap Transport – Road Network
-          Vicmap Class Codes 11 12: Bike path and walking tracks
-          Vicmap Class Codes 0 – 3: arterials
https://www.data.vic.gov.au/data/dataset/public-transport-a-collection-of-ptv-datasets
-          Public Transport a collection of PTV datasets
-          Bus stop; train stop; tram stop
-          Length of train and tram lines
http://www.communityindicators.net.au/lga_profiles
-          Community Indicators Victoria Measure of Community Engagement
ttps://developers.zomato.com/documentation#!/location/locations
-          Zomato API
 
Tools Used and What They Were Used For
R
Data cleaning, merging, aggregation.
Data analysis (building liveability index algorithm)
Producing leaflet maps
Shiny
The platform that turned the analysis into an interactive web application.
This enables the user to input data and see a visualised response as well as output the data that they generated.
Spatialite
Store the large spatial datasets, allowing us to query a small subset of that data. This saved us memory and processing time.
Python
To interface with the Zomato API https://developers.zomato.com/documentation#!/location/locations.
To generate a bunch of curl commands that dumped the json response from "locations" service to fetch the entity_type and entity_id for the suburbs of interest.
Then to generate curl commands that got the ratings and top restaurants for each of the suburbs, before collating all the data in .csv file to use in the Shiny app.
ArcGIS
Spatial joins between our data sets and spatial area (suburbs).
Slack
Sharing files and links
GitHub
Repository of files and code used for our entry
https://github.com/mrjoh3/govhack2016