---
datasets_used:
- agency: ABS
  name: Basic community profile
  url: http://www.abs.gov.au/websitedbs/censushome.nsf/home/datapacks?opendocument&navpos=250
- agency: Australian Financial Security Authority
  name: AFSA Regional statistics
  url: https://data.gov.au/dataset/quarterly-regional-statistics
- agency: Department of Industry, Innovation and Science
  name: sa3-region-innovation-data
  url: https://data.gov.au/dataset/sa3-region-innovation-data
- agency: PSMA
  name: administrative boundaries
  url: https://data.gov.au/dataset/psma-administrative-boundaries
- agency: Bureau of Crime Statistics and Research  Search...
  name: Recorded Crime Dataset
  url: http://www.bocsar.nsw.gov.au/Pages/bocsar_crime_stats/bocsar_detailedspreadsheets.aspx
- agency: Department of Social Services
  name: Settlement Data Extract
  url: https://data.gov.au/dataset/http-www-dss-gov-au-settlement-and-multicultural-affairs-programs-policy-settlement-services
- agency: Department of Education and Training
  name: Higher Education Attrition Rates 2005-2013
  url: http://portal.govhack.org/datasets/2016/australia/department-of-education-and-training/higher-education-attrition-rates-2005-2013.html
- agency: Insurance Australia Group
  name: iag flood data
  url: https://github.com/iag-edge-labs/flood-data
event: sydney
hackerspace_url: https://2016.hackerspace.govhack.org/node/2966
jurisdiction: nsw
prizes:
- australia-commerically-viable-hack
- australia-creative-humanities-hack
- australia-data-intelligence-hack
- australia-entrepreneurial-hack
- australia-fresh-data-hack-(api’s-and-data-services)
- australia-inspired-by-research-hack
- australia-storytelling-hack
- australia-location-data
- australia-no-boundaries-data-hack
- nsw-vibrant-sydney-night-time-economy
- nsw-most-fun-and-creative-use-of-data
- nsw-team-encouragement-award
project_title: Do you know Australia?
project_url: http://52.63.72.68/  https://invis.io/4E84LOJ7K
repo:
  name: Innovative Agents of Govhack
  type: github
  url: https://github.com/gersonadr/IAG_GovHack2016
team_name: Innovative Agents of GovHack
video:
  type: youtube
  url: https://www.youtube.com/watch?v=CcQlj_LIu_w&feature=youtu.be
---

How do we measure perception against reality? 
Use the innovative agents of govhack minigame!
“Do you know Australia?” is a fun and engaging online mini-game platform where YOU can learn more about YOUR area, and WE can all learn about OUR perceptions.
 
We all carry cognitive biases that affect our perception of the world. 
This is important because our collective perception has the power to change our communities. It impacts how we view our neighbours, how we interact with the people we meet, where we go and how we feel when we're there.
How do we measure perceptions so we know where to focus on improving them? So that we as communities, privates and governments can direct our attention, fuding and programs to the real issues. We need a better way of educating and engaging to understand eachother. We need the "Do you know Australia" minigame!
 

Using open government data on community themes, we present the user with a series of two random facts to compare about their area. 
​​​​​​​Behind the scenes, we collect the response and record the comparisons made. For example, this can be used to test and measure perceptions about crime in your local area. The anonymised data collected from the app can then be used by local government, to better understand how their citizens perceive the level of risk in the community.
The platform can be adapted to explore any topics - enabling the exploration of perceptions of everything from race, to employment, to ecology, and more. ​​​​​​​​​​​​​​
 
The Data and App
We mashed together datasets which helped us describe a community. We wanted to test perceptions on core community themes and topics. We also used a number of boundary datasets which enabled us to repost across boundaries, link to more datasets and aggregrate. We mashed the data with postgres into a single table that can be accessed in an api. 
We created a REST API which expose stateless endpoints which can be integrated with external applications (such as a mobile app or website). The technology of choice is micro-services using Spring Boot for rapid development and deploy.
Wireframes were designed to show what a working protoype could look like.
 
Commercialisation
There are three potential revenue streams for the "Do you know Australia" mini-game. First, the call to action at the end of the game could be altered to promote events, services and businesses in the user's area which, based on the data they could be more likely to enjoy with the new, corrected perceptions. Secondly, the response data collected could be sold to help inform policy and business decisions by private organisations. Finally, the game itself could be repurposed around a particular issue to form a key part of an awareness campaign.