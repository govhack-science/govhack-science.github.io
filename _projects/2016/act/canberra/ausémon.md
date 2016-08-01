---
datasets_used:
- agency: Atlas of Living Australia
  name: Specimen & observation data searching API
  url: http://biocache.ala.org.au/ws/occurrences/search
- agency: ACT Government
  name: Canberra Centenary Trail
  url: https://www.data.act.gov.au/Environment/Canberra-Centenary-Trail/86di-ncd5
event: canberra
hackerspace_url: https://2016.hackerspace.govhack.org/node/1001
jurisdiction: act
prizes:
- australia-commerically-viable-hack
- australia-creative-humanities-hack
- australia-data-intelligence-hack
- australia-entrepreneurial-hack
- australia-fresh-data-hack-(api’s-and-data-services)
- australia-innovative-ideas-hack
- australia-storytelling-hack
- australia-location-data
- australia-ncris-data
- australia-no-boundaries-data-hack
- act-best-data-wrangling
- act-best-in-act
- act-best-use-of-act-government-spatial-data
- act-most-fun-use-of-act-government-data
- act-most-innovative-project-for-canberrans
project_title: Ausémon
project_url: http://ausemon.io/
repo:
  name: Ausémon GovHack 2016 Working Folder
  type: unknown
  url: http://ausemon.io/
team_name: rgb(255,0,0)
video:
  type: vimeo
  url: https://vimeo.com/176903634
---

Ausémon is a mobile application aimed at getting more people exploring and enjoying the Canberra Centenary Trail.  It provides a fun and educational guide for the trail and the types of animals you could expect to see.  Ausémon is gameified in the style of Pokémon Go to provide additional appeal to youth.  Getting people outside and walking supports the Healthy Canberra initiative.
Ausémon uses a number of datasets, but could easily be extended to utilise more.  The Canberra Centenary Trail location, or spatial, data comes from the ACT Government open data website; these data were split into two GeoJSON datasets, cleaned, and stored locally for use by the application.  The animal location comes from the Atlas of Living Australia Specimen and Observation Data Searching API.  We were originally planning on calling this API in real-time from the application, but found that it needed a vast aount of cleaning and enrichment; the API was used to extract the data and stored locally for use by the application.
From a technical point of view, Ausémon is a typical 3-tier application with a front-end mobile application, a back-end database, and a middle-tier providing integration logic.  The mobile application is built using Ionic and Google Maps API, then packaged inside a Cordova container for installation on a smartphone.  All of the data has been stored in Oracle Database Cloud Service to take advantage of the spatial querying features; this significantly simplified the querying of data based on location, distance, and geofencing.  And lastly, the middle-tier consists of the Oracle Mobile Cloud Service (MCS) to talk to the database (through Oracle Application Container Cloud Service for simplicity) and expose those data as APIs to be called by the mobile application.  MCS also manages API security and provides analytics of the usage of Ausémon.
We see several benefits of an application like Ausémon.  Firstly, it gets residents out exercising which is good for the Health agenda and contributes to the goal of reducing pressure on the ACT Health System.  Secondly, it helps promote Canberra tourism and the Trail itself.  Lastly, it provides the ACT Government with useful data on the usage of the Trail, such as which sections of the Trail are being utilised; these data could be used for preventitive maintenance, for example.
This platform could easily be extended to incorporate other locations and features of Canberra, such as heritage sites and places of interest.  While it would be ideal for the mobile application to integrate directly with the source data via APIs, we feel that the APIs would need to be refined to be suitable for small and frequent queries which is typical of a mobile application.