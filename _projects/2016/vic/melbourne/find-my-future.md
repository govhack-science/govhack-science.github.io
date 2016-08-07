---
category: ''
datasets_used:
- agency: Department of Employment
  name: Employment Regions 2015-2020
  url: https://data.gov.au/dataset/employment-regions/resource/c31b3ef9-33e0-47bf-b2b3-cd3c14043263
- agency: Department of Employment
  name: Employment Services Provider Locations and Contacts
  url: https://data.gov.au/dataset/employment-provider-locations-and-contacts/resource/d9c69f98-f0af-4db8-b598-513e1da748ce
- agency: Department of Employment
  name: Labour Market Information Portal Employment projections
  url: http://lmip.gov.au/default.aspx?LMIP%2FEmploymentServicesTender%2FVictoriaTasmania
- agency: Australian Bureau of Statistics
  name: Demographic statistics per SA4 (statistical area level 4)
  url: http://stat.abs.gov.au/itt/r.jsp?RegionSummary&region=209&dataset=ABS_REGIONAL_ASGS&geoconcept=REGION&measure=MEASURE&datasetASGS=ABS_REGIONAL_ASGS&datasetLGA=ABS_NRP9_LGA&regionLGA=REGION&regionASGS=REGION
event: melbourne
gid: find-my-future
hackerspace_url: https://2016.hackerspace.govhack.org/node/976
image_url: https://2016.hackerspace.govhack.org/sites/default/files/field/image/FMF-Logo.png
jurisdiction: vic
prizes-entered:
- australia-commerically-viable-hack
- australia-creative-humanities-hack
- australia-data-intelligence-hack
- australia-future-australia-hack
- australia-local-industry-activity
- australia-training-data
project_title: Find my Future
project_url: http://govhackw8nvxqquhx.devcloud.acquia-sites.com
repo:
  name: https://github.com/salsadigitalauorg/govhack2016
  type: github
  url: https://github.com/salsadigitalauorg/govhack2016
team_name: SalsaDigital
video:
  type: youtube
  url: https://youtu.be/mWnls8n8SW0
---

Find my Future - a tool based data that looks at prediciting industry trends into the future.  The tool services job seekers looking to change industry, relocate or enter the workforce.  The tool also is for employment service providers looking to have access to qualified job seeker applications and looking to fulfill these applicants into jobs with the benefit of trend and projection data by location and industry.
Data Sets integrated include:
 
employment regions;
employment service providers
employment projections
other statisitical data
 
A working prototype was built using govCMS as the platform to host the application.  An interactive clickable prototpye also exists.
---
Sample API URL for North Eastern Melbourne: 
Employment Region Data: http://govhackw8nvxqquhx.devcloud.acquia-sites.com/api/views/locations?args[0]=3058
Employment Agencies: http://govhackw8nvxqquhx.devcloud.acquia-sites.com/api/views/employment_agencies?args[0]=3058
Region Statistics: http://govhackw8nvxqquhx.devcloud.acquia-sites.com/api/views/employment_statistics?args[0]=3058
Backend URL: http://govhackw8nvxqquhx.devcloud.acquia-sites.com/user     ..  Go to http://govhackw8nvxqquhx.devcloud.acquia-sites.com/admin/content for the datasets imported.