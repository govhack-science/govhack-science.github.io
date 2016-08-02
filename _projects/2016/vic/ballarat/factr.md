---
datasets_used:
- agency: Ballarat Council
  name: Ballarat Car Parking Data
  url: http://data.gov.au/geoserver/ballarat-car-parking-areas/wfs?request=GetFeature&typeName=eb670c53_1fbc_4ca5_9ffd_4e336fdb0763&outputFormat=csv
- agency: Ballarat Council
  name: Ballarat CCTV Cameras
  url: http://data.gov.au/dataset/e99f92a8-beea-4725-9897-c1854eb9cc3d/resource/e9e0a68d-1bc9-4f49-8df5-7528d2129100/download/cctv.csv
- agency: Ballarat Council
  name: Ballarat Drinking Fountains
  url: http://data.gov.au/dataset/0c41aa28-5d9c-48f5-b4a7-5eecd8f90c8c/resource/a21e5855-747f-4631-8179-8604b2040e7f/download/BallaratDrinkingFountains.csv
- agency: Geelong Council
  name: Geelong Child Care Centres
  url: http://data.gov.au/geoserver/child-care-centres-city-of-greater-geelong/wfs?request=GetFeature&typeName=ckan_6a564f08_0dd0_4845_bd9c_eedb5d8071fa&outputFormat=csv
- agency: Ballarat Council
  name: Ballarat Parking Infringements
  url: http://data.gov.au/dataset/ballarat-parking-infringements
- agency: Ballarat Council
  name: Ballarat Graffiti Defects
  url: http://data.gov.au/dataset/ballarat-graffiti-defects
- agency: Geelong Council
  name: Geelong Residential Vacant Land
  url: http://data.gov.au/geoserver/residential-vacant-land-city-of-greater-geelong/wfs?request=GetFeature&typeName=ckan_46892a6f_eae7_46ef_9ad3_d022c33fa730&outputFormat=csv
- agency: Geelong Council
  name: Geelong CCTV Cameras
  url: http://data.gov.au/dataset/1b36f1e0-3bd4-45c4-b69c-da7515ec1710/resource/d433ed76-9f19-43c0-9687-71812307decb/download/CCTVcameralocation2.csv
- agency: Ballarat Council
  name: Ballarat Child Care Centres
  url: http://data.gov.au/dataset/c8642f6b-0c28-48d2-867f-4c95ed64a84a/resource/57b5b44c-a477-41c2-b3ba-dfb7f7047848/download/ballaratchildcarecentres.csv
- agency: Ballarat Council
  name: Ballarat Toilets
  url: http://data.gov.au/dataset/4f875c86-2a8c-4daf-b40d-dca04aab49ea/resource/76d31bf1-a106-4c24-b37f-dae17fc691bd/download/ballaratpublictoilets.csv
- agency: Ballarat Council
  name: Ballarat Playgrounds
  url: http://data.gov.au/dataset/a9b248c1-2078-45fa-b9c6-b2ae562c87b2/resource/f63ad2fa-9d7e-410e-a488-04219701af5d/download/BallaratPlaygrounds.csv
- agency: Geelong Council
  name: Geelong Street Lights
  url: http://data.gov.au/dataset/e3b72b58-3875-4c5d-82a4-cb16dc0b0af8/resource/41139bf8-6c28-48c2-a423-ca61a3b3da36/download/geelongstreetlights.csv
- agency: Ballarat Council
  name: Ballarat BBQ's
  url: http://data.gov.au/dataset/f2ab58d7-18b7-44dc-9121-9cd0ae829d22/resource/f01abfb8-ae42-44cc-a82c-d966649aa7d8/download/BallaratBBQs.csv
event: ballarat
hackerspace_url: https://2016.hackerspace.govhack.org/node/2056
image_url: https://2016.hackerspace.govhack.org/sites/default/files/field/image/bhacktest.png
jurisdiction: vic
prizes:
- australia-abc-news-content
- australia-creative-humanities-hack
- australia-fresh-data-hack-(api’s-and-data-services)
- australia-future-australia-hack
- australia-innovative-ideas-hack
- australia-community-resilience-hack
- australia-machine-learning-hack
- australia-storytelling-hack
- vic-geelong-open-data---creative-challenge
- vic-best-use-of-ballarat-data
project_title: factr
project_url: https://factr.bhack.in/ui/
repo:
  name: Github
  type: github
  url: https://github.com/ballarat-hackerspace/factr
team_name: bHack Gamma
video:
  type: youtube
  url: https://www.youtube.com/watch?v=H23M_oPXRVc
---

Factr is designed to provide amusing, but also surprisingly insightful statements by combining huge amounts of disparate location data. We've combined 13 local government data sets as a starting point for this, but have also developed a tool that allows us to rapidly add additional datasets (of different structures) without requiring lengthy manual processing. 
We analyse this data using cognitive methods to extract meaning and provide random a natural language statement about it based on your location. Sometimes this data is as simple as the number of things around you, other times it might be an average or combined total of nearby activities. Eg:
"The average parking fine in this area is $61.92. Really makes you think"
Each stage of the process (loading, analysing, language processing etc) is modular and can be swapped for different services as needed. 
Note: For our demo, the location is fixed as the centre of Ballarat by default, but it is possible to use the current GPS location by clicking the factr label in the top right corner