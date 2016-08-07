---
category: ''
datasets_used:
- agency: City of Melbourne
  name: Building information
  url: https://data.melbourne.vic.gov.au/Property-Planning/Building-information/pmhb-s6pn
- agency: City of Melbourne
  name: Pedestrian Counts
  url: https://data.melbourne.vic.gov.au/Transport-Movement/Pedestrian-Counts/b2ak-trbp
- agency: City of Melbourne
  name: Pedestrian Sensor Locations
  url: https://data.melbourne.vic.gov.au/Transport-Movement/Pedestrian-Sensor-Locations/ygaw-6rzq
- agency: City of Melbourne
  name: Census Of Land Use And Employment (CLUE) Small Areas
  url: https://data.melbourne.vic.gov.au/Economy/Census-Of-Land-Use-And-Employment-CLUE-Small-Areas/gei8-3w86
event: brisbane
gid: pedestimate
hackerspace_url: https://2016.hackerspace.govhack.org/node/3056
jurisdiction: qld
prizes-entered:
- australia-commerically-viable-hack
- australia-data-intelligence-hack
- australia-entrepreneurial-hack
- australia-innovative-ideas-hack
- australia-location-data
- australia-transport-data
- qld-best-innovative-use-of-data-sets
- qld-logan-land-use-and-development
- qld-logan-land-use-and-development
- qld-best-brisbane-or-queensland-oriented-business-related-application
- qld-supporting-the-best-of-brisbane
- qld-supporting-the-best-of-brisbane
project_title: PedEstimate
project_url: http://jamiecook.github.io/pedestimate
repo:
  name: Pedestimate
  type: github
  url: https://github.com/jamiecook/pedestimate
team_name: ChristopherWalkIn
video:
  alt_url: https://govhack-storage.s3-ap-southeast-2.amazonaws.com/2016/PedEstimateDemo_1080p.mov
  type: unknown
  url: ''
---

Project Description
Starting a new restaurant is hard - there are so many things to consider:
Where do you get the best staff?
Have you organised appropriate insurance?
Is the menu going to be a hit?
But thankfully, choosing where to situate your new business just got easier with PedEstimate.
PedEstimate allows you to easily examine a range of potential locations to evaluate the amount of foot fall traffic in the vicinity. PedEstimate uses City of Melbourne pedestrian counter data and combines it with foursquare venue data and City of Melbourne land use data to build a predictive model of pedestrian foot traffic. It also enables you to easily see the surrounding drivers of this traffic such as office space, retail space, restaurants and residential accomodation.
Our simple to use web interface makes the process of site selection a quick and easy process. Checkout the demo below for more details.
For the nitty gritty, check out our github repo.​​​​​​​
Data Story
The core concept of PedEstimate is to use a predictive model to determine the likely footfall traffic based on a number of known predictors such as:
The amount of nearby office space (within 100, 200 and 300 meters)
The amount of nearby retail space
The number of competing dining establishments
The nearby employment density
Using cutting edge estimation techniques we are able to generate models which predict the pedestrian traffic at any location within the city.