---
datasets_used:
- agency: ABS
  name: B29 Census Data Motor Vehicle Ownership
  url: http://stat.abs.gov.au/restsdmx/sdmx.ashx/GetData/ABS_CENSUS2011_B29/TOT.D.+.SA2.+.A/ABS?startTime=2011&endTime=2011
- agency: ABS
  name: 2011 IRSAD - SA2
  url: http://www.ausstats.abs.gov.au/ausstats/subscriber.nsf/0/4B80C5D126524576CA257B3B001A69C6/$File/2033.0.55.001%20irsad%20sa2.zip
- agency: ABS
  name: SA2_2016_AUST
  url: http://www.abs.gov.au/AUSSTATS/abs@.nsf/DetailsPage/1270.0.55.001July%202016?OpenDocument
- agency: ABS
  name: ArcGIS Information system for ABS data
  url: http://censusdata.abs.gov.au/arcgis/rest/services/ASGS2016/SA2
- agency: ''
  name: Environmental monitoring site locations
  url: http://www.ehp.qld.gov.au/data-sets/monitoring/monitoring-sites-on-open-data.csv
- agency: ''
  name: Air Quality Monitoring - Live data feed
  url: http://www.ehp.qld.gov.au/cgi-bin/air/xml.php
- agency: ''
  name: npi-2015-qld-air-point-emissions
  url: http://ehp.qld.gov.au/data-sets/npi/npi-2015-qld-air-point-emissions.csv
- agency: ''
  name: npi-2015-qld-air-fugitive-emissions
  url: http://ehp.qld.gov.au/data-sets/npi/npi-2015-qld-air-fugitive-emissions.csv
- agency: ''
  name: npi-2015-qld-air-total-emissions
  url: http://ehp.qld.gov.au/data-sets/npi/npi-2015-qld-air-total-emissions.csv
- agency: ''
  name: npi-2015-qld-water-emissions
  url: http://ehp.qld.gov.au/data-sets/npi/npi-2015-qld-water-emissions.csv
- agency: ''
  name: npi-2015-qld-land-emissions
  url: http://ehp.qld.gov.au/data-sets/npi/npi-2015-qld-land-emissions.csv
- agency: ''
  name: npi-2015-qld-transfers
  url: http://ehp.qld.gov.au/data-sets/npi/npi-2015-qld-transfers.csv
event: brisbane
hackerspace_url: https://2016.hackerspace.govhack.org/node/1036
jurisdiction: qld
prizes:
- australia-commerically-viable-hack
- australia-creative-humanities-hack
- australia-data-intelligence-hack
- australia-entrepreneurial-hack
- australia-future-australia-hack
- australia-innovative-ideas-hack
- australia-inspired-by-research-hack
- australia-community-resilience-hack
- australia-storytelling-hack
- australia-local-industry-activity
- australia-location-data
- australia-no-boundaries-data-hack
- wa-sustainable-coastlines-prize
- australia-training-data
- australia-transport-data
- australia-weather-forecast
- qld-advance-queensland!
- qld-best-innovative-use-of-data-sets
- qld-create-a-cutting-edge-concept---the-science-sandpit!
- qld-educate-us!
- qld-getting-around-brisbane
- qld-linking-logan---getting-people-out-of-their-cars
- qld-mentoring-the-best-of-queensland
- qld-an-active-and-healthy-brisbane
- qld-best-brisbane-or-queensland-oriented-business-related-application
- qld-best-visualisation-of-data
- qld-engaging-with-brisbane-city-council
- qld-make-your-hack-a-thing
- qld-supporting-the-best-of-brisbane
- qld-supporting-the-best-of-brisbane
project_title: Breathe Easy
project_url: https://github.com/rfern/remark
repo:
  name: Breathe Easy Git Repo
  type: github
  url: https://github.com/rfern/remark
team_name: REMARK
video:
  type: youtube
  url: https://youtu.be/oJ8S8FV0yag
---

Each year, 1600 Australians die from exposure to air pollution. The life expectancy of Australians is diminished by an average 69 days on account of air pollution. Australia has the highest prevalence of Asthma in the world, with 1 in 10 people suffering from the chronic condition. 
We all have the right to know about the quality of air we breathe and whether we are exposed to dangerous levels of pollution. The information empowers us to make decisions on whether to stay indoors or to relocate. Monitoring the quality of air can assist in determining the factors contributing to pollution. It is important to prevent air pollution from reaching toxic levels as seen in countries such as China and Mexico. Based on current emission trends, mortality due to outdoor air pollution is projected to double by 2050.
Breathe Easy is an app that informs users of the levels of air pollution in real-time on an interactive map. It clearly illustrates the quality of air from poor to good. The web application is responsive for easy use on both desktop and mobile.
The data sets integrated into the Breathe Easy App include a real-time feed of the air quality monitoring data, a list of all the monitoring sites with associated geographic information, and six NPI emission data sets containing industry emission data.
Within the Springboot application, the program is written in Groovy. Using the build tool Gradle, all the required data from the API servers were retrieved. The CSV files were converted into JSON documents to be loaded onto the MONGO no SQL database. The Springboot application was used as a framework to build the back-end API. Furthermore, the API for real-time data is called and reformatted into JSON documents to be passed to the front end. The Australian Government's Cloud service, NECTAR, hosts the APIs and front-end.
The front-end web interface is programmed in JavaScript, HTML and CSS, and served from Springboot. The open source libraries used were Bootstrap, J-Query, and the Google Map JavaScript API. 
In the age of Internet Of Things, sensors have the potential to be implemented in a range of locations and monitor air quality. This crowdsourcing of data will be invaluable in the future.