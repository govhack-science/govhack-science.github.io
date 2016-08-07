---
category: ''
datasets_used:
- agency: Transport and Main Roads
  name: General transit feed specification (GTFS)—South East Queensland
  url: https://data.qld.gov.au/dataset/general-transit-feed-specification-gtfs-seq
- agency: Transport and Main Roads
  name: TransLink real time data
  url: https://data.qld.gov.au/dataset/translink-real-time-data
event: brisbane
hackerspace_url: https://2016.hackerspace.govhack.org/node/1546
image_url: https://2016.hackerspace.govhack.org/sites/default/files/field/image/quickbus2.png
jurisdiction: qld
prizes:
- australia-creative-humanities-hack
- australia-fresh-data-hack-(api’s-and-data-services)
- australia-location-data
- australia-transport-data
- qld-advance-queensland!
- qld-getting-around-brisbane
- qld-engaging-with-brisbane-city-council
- qld-supporting-the-best-of-brisbane
- qld-supporting-the-best-of-brisbane
project_title: QuickBus
project_url: ''
repo:
  name: QuickBus Code Repository
  type: github
  url: https://github.com/schomper/GovHack2016
team_name: The Quick Bus Boys
video:
  type: youtube
  url: https://www.youtube.com/watch?v=CheNzWAoTWs
---

While Journey Planning apps and services are well established within the Brisbane bus transit ecosystem, one very common use case is neglected by current systems. QuickBus aims to allow users who are on their regular commute - who know their bus route and travel from a regular stop - to instantly and easily find out where their bus is.
Finding when a particular bus is coming to a particular stop, and whether it is delayed, using the MyTranslink app takes over a dozen taps and anywhere from 30 seconds to a minute to complete. QuickBus aims to make this information available in a single step, thereby providing the single most relevant piece of transit information available to commuters instantly.
When opening the application, users immediately see the incoming buses for the nearest stop, complete with information as to whether these buses are delayed or running early. By swiping, they can switch through nearby stops, and by long pressing on a bus, they can show only buses of that route.
QuickBus makes use of Translink data, through the Translink GTFS network information dataset, augmented with real-time transit update data drawn from the GTFS-realtime API.