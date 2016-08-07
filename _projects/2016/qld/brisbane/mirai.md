---
category: ''
datasets_used:
- agency: Australian Bureau of Statistics
  name: 'Australian Statistical Geography Standard (ASGS): Correspondences, July 2011'
  url: http://www.abs.gov.au/AUSSTATS/abs@.nsf/DetailsPage/1270.0.55.006July%202011?OpenDocument
- agency: Australian Bureau of Statistics
  name: Job Vacancies, States and Territories ('000)
  url: http://www.abs.gov.au/ausstats/meisubs.NSF/log?openagent&6354001.xls&6354.0&Time%20Series%20Spreadsheet&FA0C3DEC2F29F12DCA257FE10013CB9D&0&May%202016&30.06.2016&Latest
- agency: Department of Employment via Australian Bureau of Statistics
  name: SA4 - Employment by Industry, May 2016
  url: http://lmip.gov.au/PortalFile.axd?FieldID=1453545
- agency: Department of Employment via Australian Bureau of Statistics
  name: SA4 - Population by Age Group, May 2016
  url: http://lmip.gov.au/PortalFile.axd?FieldID=1453551
- agency: Department of Employment via Australian Bureau of Statistics
  name: SA4 - Employment by Occupation May 2016
  url: http://lmip.gov.au/PortalFile.axd?FieldID=1453548
- agency: Australian Bureau Statistics
  name: Employee Earnings and Hours, Australia, May 2014
  url: http://www.abs.gov.au/ausstats/subscriber.nsf/log?openagent&63060do001_201405.xls&6306.0&Data%20Cubes&579D9C93BCEDC1A3CA257DD400758DF6&0&May%202014&22.01.2015&Latest
- agency: Australian Taxation Office
  name: GovHack2016
  url: https://data.gov.au/dataset/govhack2016/resource/f6e42012-4233-4fa3-aa9f-7063d27df5f8
- agency: Australian Bureau of Statistics
  name: 1380.0.55.011 Non-School Qualifications in Regions, 2011
  url: http://www.abs.gov.au/ausstats/subscriber.nsf/log?openagent&138055011.xls&1380.0.55.011&Data%20Cubes&19E52DBB51397DFCCA257C0800103D79&0&2011&21.10.2013&Latest
- agency: Department of Employment via Australian Bureau of Statistics
  name: 2016 Industry Employment Projections - five years to November 2020
  url: http://lmip.gov.au/PortalFile.axd?FieldID=1462972
- agency: Australian Bureau of Statistics
  name: Job Vacancies, Industry, Australia ('000)
  url: http://www.abs.gov.au/ausstats/meisubs.NSF/log?openagent&6354004.xls&6354.0&Time%20Series%20Spreadsheet&DB133C01E48CB80CCA257FE10013D17D&0&May%202016&30.06.2016&Latest
- agency: Department of Employment
  name: Indicative Department of Employment Skill Shortage Ratings - 1986 to 2015
  url: https://docs.employment.gov.au/system/files/doc/other/historicalskillshortagelist1986_2015.xlsx
- agency: Department of Employment
  name: SA4 - Area Profile, May 2016
  url: http://lmip.gov.au/PortalFile.axd?FieldID=1453543
event: brisbane
hackerspace_url: https://2016.hackerspace.govhack.org/node/1116
image_url: https://2016.hackerspace.govhack.org/sites/default/files/field/image/13843397_10207964798212460_1174125046_o_1.jpg
jurisdiction: qld
prizes-entered:
- australia-commerically-viable-hack
- australia-creative-humanities-hack
- australia-future-australia-hack
- australia-local-industry-activity
- australia-smarter-data
- australia-training-data
- qld-best-innovative-use-of-data-sets
- qld-mentoring-the-best-of-queensland
- qld-make-your-hack-a-thing
- qld-supporting-the-best-of-brisbane
project_title: Mirai
project_url: ''
repo:
  name: Mirai
  type: github
  url: https://github.com/genius-hub/mirai
team_name: GeniusHub
video:
  type: google-drive
  url: https://drive.google.com/file/d/0B2MKVwQfYo4oaGdxYXl3UDJpcTQ/view
---

The web application namely Miria was developed to give employment information based on the location provided by the user. The employment  information throughout Australia is used to help the user determine if a location is suitable to their needs.
The parameters for the web app includes: current location, future location, industry and age. These parameters are processed by the web app to produce information based on the scenario and given input. 
Due to limited knowledge of the SEAN(SQLite, Express, Angular and Node.js) stack the front end was not created in time and with full functionality. 
The work achieved over the weekend was the determination of using various datasets, cleaning up the datasets, migration into the database, creation of various scenario web services and the partial creation of the front end of the website. 
Through the datasets provided, many scenarios were mapped out and their various web services were created to facilitate the calling from the database.  
These are the scenarios:

Average HELP debt based on occupation and location.


Average income based on age and location.


Employment statistics based on industry and location.


Percentage HELP debt based on location.


Singles based on location.


Vacancies based on Industry and location.

The services can be viewed to see what data has been returned:
An example being: http://104.155.224.96:9000/api/incomeByAgeATOs?postcode=4000&age=21 
The other various services can be viewed in the source code in the repository.
Website screenshot: http://imgur.com/j5QGjwh
 
​​​​​​​