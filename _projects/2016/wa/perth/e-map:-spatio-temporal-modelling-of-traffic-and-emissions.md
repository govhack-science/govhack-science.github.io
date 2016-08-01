---
datasets_used:
- agency: Department of the Prime Minister and Cabinet
  name: PSMA Administrative Boundaries
  url: https://data.gov.au/dataset/psma-administrative-boundaries
- agency: Main Roads Western Australia
  name: Network Operations Traffic Data MRWA
  url: http://catalogue.beta.data.wa.gov.au/dataset/network-operations-traffic-data-mrwa
- agency: NASA LAADS Web Level 1 and Atmosphere Archive and Distribution System
  name: MODIS AOD data (MOD04_3K)
  url: https://ladsweb.nascom.nasa.gov/data/detail.html?orderID=501057284&email=songyz%40lreis.ac.cn
event: perth
hackerspace_url: https://2016.hackerspace.govhack.org/node/2201
jurisdiction: wa
prizes:
- australia-data-intelligence-hack
- australia-innovative-ideas-hack
- australia-location-data
- australia-no-boundaries-data-hack
- australia-transport-data
- australia-weather-forecast
- wa-big-data-and-analytics-prize
- wa-geospatial-prize
- wa-most-promising-govhacker
- wa-the-keep-western-australia-moving-prize
- wa-western-australian-solution-prize
- wa-western-australian-sustainability-prize
project_title: 'E-Map: Spatio-temporal modelling of traffic and emissions'
project_url: https://zacksong.carto.com/viz/0bb462e8-562a-11e6-8dc7-0ee66e2c9693/embed_map
repo:
  name: Code of models, data processing and results including data and figures
  type: github
  url: https://github.com/zacksong/emission.git
team_name: Transmissions
video:
  type: vimeo
  url: https://vimeo.com/176907351
---

We have combined traffic volume data with NASA satellite data to predict traffic-induced emissions across the Perth Metro region.
First, we use the traffic data from the Main Roads WA data on 988 road sections in the Perth Metro region. From this, we can see the traffic volume, speed, and type, such as freight or private vehicle. Then, we use modelling to predict the volume and speed of traffic on the rest of the roads in the Perth metro region: over 10,000 road segments in total.
NASA produces a worldwide dataset measuring  "aerosol depth", which aggregates the amount of heavy and light particulate emissions, as well as polluting gases like nitrous and sulphur oxides. We cross-correlate this dataset with our traffic modelling, producing a prediction of the emissions near every road in WA.
We can make predictions of the emission for any times for which the traffic volume data are available, and even into the future! We can do this by aggregating traffic data to find out the typical traffic conditions at any given time. For instance, a weekday peak hour traffic distribution looks very different to midnight on Sunday, but every weekday peak hour looks a lot like every other weekday peak hour, and every Sunday night looks a lot like every other Sunday night, on average. Now that we know how a particular traffic distribution produces a particular emission distribution, we can predict the emissions from the traffic. So, we can do live tracking, and emissions forecasting!
In future, we hope to incorporate more data into our model; for instance:
 - incorporating weather effects, such as temperature, humidity, and importantly, wind direction;
 - taking other land uses into account, such as vegetation (will reduce emissions) and manufacturing (will increase emissions);
 - cross-correlating with other measures of traffic emissions, such as the Air Quality Index.
We could also see what correlates with our model, such as:
 - incidence of respiratory illness;
 - land and house prices;
 - public transport and rail freight provision (or lack thereof).