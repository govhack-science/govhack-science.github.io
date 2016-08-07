---
category: ''
datasets_used:
- agency: Environment Protection Authority (EPA) - South Australia
  name: Aquatic Ecosystem Condition Reports
  url: https://data.sa.gov.au/data/dataset/aquatic-ecosystem-condition-reports
- agency: Dept of Environment, Water and Natural Resources
  name: Shore Based Recreational Fishing
  url: https://data.sa.gov.au/data/dataset/shore-based-recreational-fishing
- agency: DPTI
  name: Jetties
  url: https://data.sa.gov.au/data/dataset/jetties/resource/b617df1e-345b-47e4-a61e-445487a2be9f
- agency: DPTI
  name: South Australian Boat Ramp Locator
  url: http://data.gov.au/dataset/05546e03-2997-4762-a439-0f2e9a492650
- agency: SA Whale Centre
  name: Whale Sightings Log
  url: http://www.sawhalecentre.com/whale-sightings/sightings-log/?mc_cid=00ccaf0043&mc_eid=3b8b4f019a
- agency: Dept of Environment, Water and Natural Resources
  name: Shipwrecks
  url: https://data.sa.gov.au/data/dataset/shipwrecks
event: adelaide
hackerspace_url: https://2016.hackerspace.govhack.org/node/1766
jurisdiction: sa
prizes:
- australia-creative-humanities-hack
- australia-data-intelligence-hack
- australia-exploring-underground
- australia-future-australia-hack
- australia-innovative-ideas-hack
- australia-inspired-by-research-hack
- australia-community-resilience-hack
- australia-machine-learning-hack
- australia-local-industry-activity
- australia-location-data
- wa-sustainable-coastlines-prize
- sa-jemsoft-technology-development-prize
- sa-neighbourhood-and-community-confidence
- sa-premiers-prize-co-sponsored-by-business-sa-and-chiliad-consulting
- sa-premiers-prize-co-sponsored-by-microsoft
- sa-protecting-our-environment
- sa-safe-travel
- sa-smart-lifestyles
- sa-supporting-sa-economy
- sa-vibrant-adelaide
project_title: Aquadex
project_url: https://github.com/Unleashed2016/aquadex
repo:
  name: Aquadex
  type: github
  url: https://github.com/Unleashed2016/aquadex
team_name: Bob's gang
video:
  alt_url: https://govhack-storage.s3-ap-southeast-2.amazonaws.com/2016/AquaDex%20v19%20Final%20HD.mp4
  type: youtube
  url: https://youtu.be/9x5itE49uMw
---

Background:
Collecting marine and aquatic data is an important part of preserving our marine resources. At the same time it is very important to make the collected data available to interested community members, tourists and related researchers.  
The Problem
Collecting and sharing marine resource data can be a very lengthy and expensive process considering the enormity of our marine area and aquatic resources. At the same time we have heaps amount of open marine & aquatic data that people are interested in. Collaboration between these two streams of requirement can be through an effective and interactive process and providing a platform where people from each sector can interact with each other. Our goal is to make the process easier with the participation and collaboration of community members and researchers & data analysts.     
The Solution
Aquadex provides a mediator solution to exhibit aquatic data through an app in a consolidated way. So the user can just open the app and then select a location of his/her particular interest or next venture. It then invites user to accept challenges of aquatic data collection. At the same time Aquadex provides an interactive and pleasant way of collecting data and logging data using through gaming and “Augmented Reality”. Fun & adventure are two basic human interests and the app uses these to encourage people to actively participate in data collection and ultimately contributing to preserve marine & aquatic resources for our future generations.       
How It Works:
Aquadex uses a range of aquatic and marine data. It also collects and process data provided by Aquadex users. It then combines open & user data and provides a consolidated view. Users can get a list of locations marine resources of their interest like - dolphins, whales, fish species and frequency of their sightings. Then there is a list of challenges for user to collect data and share on Aquadex. Here we have included gaming logic and used our “Augmented Reality” API to make it most interactive way of collecting data.  We have also integrated the Monocular Image recognition API from Jemsoft with our application and FaceBook interface, so that the recognition of specific species and individual marine mammals can be made and details provided to Marine agencies, together with direct feedback to the user.
Our game-logic enables user to participate in a contest with other app users and score points. Users are encouraged through a range of gift-cards and aquatic points. Our Augmented Reality engine, although in a POC right now, provides a very interactive and amusing way to locate & guide you to your next challenge through markers & direction. The key concept is to use the mobile device sensors, mainly accelerometer, magnetometer, GPS, camera to establish the current location, orientation and point-of-view (in terms of camera viewport) of the device. On top, of the camera feed on the phone screen, data is superimposed in transparent/semi-transparent layers. This is done by creating virtual markers based on geolocated dataset(s) and using algorithms to determine the approximate distance and direction of heading for the marker in relation to the user's (and phone camera's) point-of-view. Navigation features can be added by using the phone's motion sensors to determine direction of movement as well.