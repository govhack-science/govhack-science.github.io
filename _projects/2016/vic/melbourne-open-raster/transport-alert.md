---
datasets_used:
- agency: Public Transport Victoria
  name: PTV Timetable API
  url: https://www.data.vic.gov.au/data/dataset/ptv-timetable-api
- agency: Google
  name: Google Maps Traffic Layer
  url: https://developers.google.com/maps/documentation/javascript/trafficlayer
event: melbourne-open-raster
hackerspace_url: https://2016.hackerspace.govhack.org/node/1071
image_url: https://2016.hackerspace.govhack.org/sites/default/files/field/image/icon_0.png
jurisdiction: vic
prizes:
- australia-commerically-viable-hack
- australia-creative-humanities-hack
- australia-entrepreneurial-hack
- australia-fresh-data-hack-(api’s-and-data-services)
- australia-innovative-ideas-hack
- australia-location-data
- australia-transport-data
- vic-journey-plannning
- vic-mav-technology-bounty
- vic-how-can-city-of-melbourne-data-be-used-to-help-businesses-make-better-decisions?
project_title: Transport Alert
project_url: https://popapp.in/w/projects/579d562a81201bbf39c85000/mockups
repo:
  name: Transport Alert (Github)
  type: github
  url: https://github.com/BetterTransportChoices/Main
team_name: Transport Alert
video:
  type: youtube
  url: https://www.youtube.com/watch?v=IdgftHm7h6k&feature=youtu.be
---

Transport Alert is a mobile application that alerts users to localised road and public disruptions and events. Existing transport apps (such as official PTV apps and TripGo) make use of maps and timetable data but do not incorporate real-time disruptions.
Transport Alert was inspired by the Victorian FireReady app that notifies users of local fires and other emergencies.
A video explanation is provided on YouTube.
A prototype is available on POP. It currently includes:
The user's current location and a list of user-defined watch zones
Map and list views of a watch zone with current traffic conditions and disruptions
Details about specific disruptions
A share sheet for sharing disruption information to social media
The disruption screen displays a Google Map with two layers:
Google Maps Traffic Layer displaying current traffic conditions (as VicRoads live traffic API was not available in time for GovHack)
Real-time disruption information from the PTV Timetable API. This needs to be parsed in two steps:
Display PTV stops in the selected area
Parse the text descriptions in the disruption data to correlate them with nearby stops (as disruption data does not provide geographical data)