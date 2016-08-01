---
datasets_used:
- agency: Public Transport Victoria (PTV)
  name: Traffic (VICROADS)
  url: http://ptv.vic.gov.au/assets/PTV/PTV%20docs/research/PTV-Station-by-Station-Fact-Sheet-accessible-version-2015.xls
- agency: Melbourne Data (City of Melbourne)
  name: Pedestrian Counts
  url: https://data.melbourne.vic.gov.au/Transport-Movement/Pedestrian-Counts/b2ak-trbp
- agency: Yarra Trams
  name: Facts-Figures (About Us)
  url: http://www.yarratrams.com.au/about-us/who-we-are/facts-figures/
- agency: Bureau of Meteorology (BoM)
  name: Melbourne, Daily Weather Observation
  url: http://www.bom.gov.au/climate/dwo/IDCJDW3050.latest.shtml
- agency: Bureau of Meteorology (BoM)
  name: Daily rainfall Melbourne Regional Office
  url: http://www.bom.gov.au/climate/dwo/IDCJDW3050.latest.shtml
- agency: Bureau of Meteorology (BoM)
  name: Daily rainfall Melbourne (Olympic Park)
  url: http://www.bom.gov.au/jsp/ncc/cdio/weatherData/av?p_nccObsCode=136&p_display_type=dailyDataFile&p_startYear=&p_c=&p_stn_num=86338
- agency: Bureau of Meteorology (BoM)
  name: Daily maximum temperature Melbourne Regional Office
  url: http://www.bom.gov.au/jsp/ncc/cdio/weatherData/av?p_nccObsCode=122&p_display_type=dailyDataFile&p_startYear=&p_c=&p_stn_num=86071
- agency: Bureau of Meteorology (BoM)
  name: Daily minimum temperature Melbourne Regional Office
  url: http://www.bom.gov.au/jsp/ncc/cdio/weatherData/av?p_nccObsCode=123&p_display_type=dailyDataFile&p_startYear=&p_c=&p_stn_num=86071
- agency: Bureau of Meteorology (BoM)
  name: Daily minimum temperature Melbourne (Olympic Park)
  url: http://www.bom.gov.au/jsp/ncc/cdio/weatherData/av?p_nccObsCode=123&p_display_type=dailyDataFile&p_startYear=&p_c=&p_stn_num=86338
event: melbourne-open-raster
hackerspace_url: https://2016.hackerspace.govhack.org/node/2726
jurisdiction: vic
prizes:
- australia-commerically-viable-hack
- australia-creative-humanities-hack
- australia-data-intelligence-hack
- australia-entrepreneurial-hack
- australia-fresh-data-hack-(api’s-and-data-services)
- australia-inspired-by-research-hack
- australia-machine-learning-hack
- australia-location-data
- australia-new-infrastructure
- australia-transport-data
- australia-weather-forecast
- vic-journey-plannning
- vic-mav-technology-bounty
- vic-how-can-city-of-melbourne-data-be-used-to-help-businesses-make-better-decisions?
project_title: futureNow
project_url: https://futurenow.shinyapps.io/GovHack2016-master/
repo:
  name: Github
  type: github
  url: https://github.com/AndrewManHayChiu/GovHack2016
team_name: Level One
video:
  type: youtube
  url: https://youtu.be/OUSPHrd7pk0
---

​​​​​​​futureNow
One of our biggest, hidden problems is the commute to and from work and school.
We often decide how to go to work based on the present weather and past experience. The weather can influence traffic conditions such as speed and accidents, and also our preference for comfort, convenience and speed.
However, herding behaviour often results in suboptimal decisions. For example, on a cold rainy day, a commuter who needs to walk 15 minutes to the closest station may decide that driving to work would be a better decision. When a multitude of people make this same decision, roads may become congested, and braving the weather may have been a wiser decision.
Understanding where large crowds appear from smart sensors and the Internet of Things may help inform us of making better travel arrangements.
futureNow is a web application we built that predicts the volume of people using different modes of transport for specific locations (i.e: train stations). Predictions on train patronage and traffic volume are based on weather indicators and time variables (day of the week, month etc.).
​​​​​​​Target Audience
Our target audiences are commuters and government agencies. Commuters can look into the app and get a rough picture of how crowded their destination or route will be. They can then decide if they would like to drive or use public transportation. Government agencies, on the other hand, can anticipate and plan for extra emergency and public transport services or modify lane ways.
Other potential users include the Police Force, Ambulances and Public Transport Victoria (PTV). The Police can estimate traffic volume and enforcement. Ambulances can predict the volume of patronage within an area and choose the best route to take. PTV can predict the number of commuters and decide if they would like to use an extra train/tram to accommodate the number of passengers.
Businesses can also use the information provided when plan logistic, like the best time for pick-up and delivery.
Scenarios
1. John is a 28 year old who has had a very bad day and wishes to travel home after a long and tiring day, he gets onto the website, puts in all the necessary information, and can immediately see the trains will be overcrowded. He realizes that it’s going to be too crowded, so he decides to hail a taxi/uber instead of the train.
2. Anna drives the ambulance and responds to emergency calls. She needs to be informed about congested areas and determine the quickest route to the hospital. Before her shift starts, she checks our website on her phone and can immediately tell which areas have a low probability of congestion throughout the day.
3. Andrew works at PTV and is in charge of ensuring train efficiency. Our website helps inform him that Glenferrie Station will be very crowded today. He decides to deploy extra services on the Belgrave, Lilydale or Alamein lines to accommodate the volume of commuters.
4. Mike is running a delivery business. Not all of the products he deliver are time sensitive and have to be delivered or picked up in exact time. Having the information about expected use of roads he can better plan when and where he'll drive.
Limitation of the current version and potential improvements
Ideally the application requires hourly or daily data about use of all different ways of the transportation (train, tram, bus, bike, cars, walk) and weather across multiple locations across Melbourne Metro area. We were able to located the daily datasets of pedestrian movement in city of Melbourne, we have to estimate daily train station traffic based on this pedestrian movement.  At the moment app predicts only the train patronage.
Applicable Prizes​​​​​​​
**Commercially Viable Hack**
A potential commercialization avenue to service Local and State Government customers and scale to internationally.
**Creative Humanities Hack**
We have combined data from local (City of Melbourne), state (PTV and VicRoads) and federal (Bureau of Meteorology) departments to produce our prediction and insights.
**Data Intelligence Hack (Data journalism, spatial modelling, analytics):**
Using different sets of data from different sources to produce a predictive model. This will help optimize business decisions from local government, transport authorities and many more.
**Entrepreneurial Hack**
A potential commercialization avenue to service Local and State Government customers and scale to international level.
**Fresh Data Hack (API’s and Data Services)**
The main function of the app requires a mash up of these datasets to produce a predictive model that helps the community decide on their daily mode of transportation.
**Inspired by Research Hack**
We have combined data from local (City of Melbourne), state (PTV and VicRoads) and federal (Bureau of Meteorology) departments to produce our prediction and insights.
**Journey Planning, helping businesses make better decisions**
The main function of the app requires a mash up of these datasets to produce a predictive model that helps the community decide on their daily mode of transportation.
**Machine Learning Hack**
A simple linear regression to produce the predictions on stations and train patronage.
**MAV Technology**
We have combined data from City of Melbourne and State Level Agencies to produce our prediction and insights.
**New Infrastructure**
A potential commercialization avenue to service Local and State Government customers and scale to international level.
**Transport Data, Location Data**
The main function of the app requires a mash up of these datasets to produce a predictive model that helps the community decide on their daily mode of transportation.
**Weather Forecasts**
The main function of the app requires a mash up of these datasets to produce a predictive model that helps the community decide on their daily mode of transportation.