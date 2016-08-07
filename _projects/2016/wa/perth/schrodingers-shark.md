---
category: ''
datasets_used:
- agency: Department of Fisheries
  name: Shark Hazard API
  url: http://api.fish.wa.gov.au/webapi/Other-Resources/Examples
- agency: Bureau of Meteorology
  name: Weather forecasting verification data (2015-05 to 2016-04)
  url: https://data.gov.au/dataset/weather-forecasting-verification-data-2015-05-to-2016-04
- agency: AODN/NCRIS
  name: Salinity CARS 2009 - WORLD MONTHLY
  url: https://catalogue-imos.aodn.org.au/geonetwork/srv/eng/metadata.show?uuid=d9302a48-57b1-41c2-a0dc-78bd00dd5e4b
- agency: NCRIS
  name: Precipitation Data
  url: http://dap.nci.org.au/thredds/remoteCatalogService?command=subset&catalog=http%3A//dapds00.nci.org.au/thredds/catalogs/rr9/emast_tern-climate-emast-anuclimate-0_01deg-v1m0_aus-mon-land-prec-e_01-1970_2012.xml&dataset=eMAST_ANUClimate_mon_prec_v1m0_1970_2012_agg
event: perth
gid: schrodingers-shark
hackerspace_url: https://2016.hackerspace.govhack.org/node/2546
image_url: https://2016.hackerspace.govhack.org/sites/default/files/field/image/SchrodingersShark.jpg
jurisdiction: wa
prizes-entered:
- australia-commerically-viable-hack
- australia-data-intelligence-hack
- australia-entrepreneurial-hack
- australia-fresh-data-hack-(api’s-and-data-services)
- australia-innovative-ideas-hack
- australia-inspired-by-research-hack
- australia-community-resilience-hack
- australia-ncris-data
- wa-sustainable-coastlines-prize
- australia-weather-forecast
- wa-big-data-and-analytics-prize
- wa-most-promising-govhacker
- wa-shark-solutions-prize
- wa-western-australian-community-prize
- wa-western-australian-entrepeneurial-prize
- wa-western-australian-solution-prize
project_title: Schrodinger's Shark
project_url: ''
repo:
  name: Schrödinger's Shark
  type: dropbox
  url: https://www.dropbox.com/sh/ervc2ambg69ldxa/AABp6Mg_xPpxxPfOF_X6Kuima?dl=0
team_name: Schrodinger's Shark
video:
  type: youtube
  url: https://youtu.be/uDbA1yWH9Ro
---

Is there a shark near the beach? Until a shark is sighted, it is there and not there - there is a probability.
Summary:
We have demonstrated a concept for spatially mapping the risk factors for local shark activity across the entire coast of Western Australia, which we aim to deliver via an easily accessible app interface for the public, and detailed predication data for research and government agencies. Our output empowers beach users to make informed decisions about beach use before a risk is iminent, and provides information for organisations and businesses to plan their future and shape their development.
The risk factors are assembled by looking at the trends and patterns between previously recorded sightings and environmental factors, such as season, migration and temperature, at the time of the sighting. The patterns are used to create a shark probability density function, which, given the current time, and current weather, can be used to predict the probability of shark activity along the Western Australia's coast in addition to condsidering real time detection of tagged sharks, whale carcasses and reports of sightings.
 
Problem:
Recent shark attacks around Australia’s coast have had a notable effect on the psyche of the country and peoples relationship with the water. Psychologists warn that the climate of fear generated around shark attacks risks producing a generation of children who are afraid of the beach, and is discouraging participation in water activities.  Recent surveys also indicate that recent high profile attacks have had international repercussions costing millions to Australia’s tourism industry.
Whilst shark detection and reporting programs exist in most Australian states, these methods are reactive and limited in their reach. Beachgoers are told to be aware and to make sensible decisions, relying on unproven and often conflicting advice from “avoid dark coloured swim wear” to “don’t swim if it’s overcast”.
We saw an opportunity here to separate the myths from the scientifically supported facts, and to synthesise historic shark sighting data with real time environmental conditions and reports. This information is coalesced to evaluate local risk factors, openly presenting them to allow people and organisations to make more informed decisions on their beach use and to feel safer in the water.
How we do it:
We read in the sighting and detection data, provided by the Department of Fisheries, applying science to data and assemble a list of shark sightings, along with its species, and location and time of sighting information. For each sighting, the time and location information is used to query other databases, such as the Bureau of Meteorology and NCRIS, for relevant environmental factors at the time of the sighting. The patterns and trends observed are used to train a probability classifier, which can take the current time and weather, and predict the probability of shark activity. This classifier will continuously evolve as it is presented with new data and research, and can further be expanded to incorporate more data, as it is made available, such as salinity and ocean floor depths.
What we show:
Trends in shark sightings: 
https://www.dropbox.com/s/wp94u1e0lorzp5g/histograms.jpg?dl=0
The evolution of the probability of shark activity across the year for broze, tiger and great white sharks.
https://www.dropbox.com/s/1osp2uz9otdtrmd/shark_migration_video.mp4?dl=0
An example of a web visualisation
https://www.dropbox.com/s/to144g57wl6ea8j/map_overlay.png?dl=0
What we need:
Going forward the platform will include data from other states and continually refine the risk equation based on emerging research and availability of new data.
In order to achieve this we specifically need contributors:
1. Geoscience Expertise - to integrate geospatial data related to water depth
2. App Developer
3. Marketing and UX/Graphic design
We need support/commitment from the government to help us with further research and data access, which we will then be able to employ to provide organisations and the public with the tools to make educated decisions on their beach use, reduce public uncertainty and effectively direct government resources.
 
We would like to say a special thanks to the mentors from the Department of Fisheries and GIS data for going well out of their way to provide support over the weekend.