---
datasets_used:
- agency: Australian Institute of Health and Welfare
  name: General Record of Incidence of Mortality (GRIM) books
  url: https://data.gov.au/dataset/grim-books
- agency: Australian Institute of Health and Welfare
  name: Premature mortality in Australia 1997–2012
  url: http://www.aihw.gov.au/deaths/premature-mortality/source-data/
- agency: Department of Education and Training
  name: Higher Education Attrition rate data 2005-2013
  url: https://data.gov.au/dataset/higher-education-attrition-rates-2005-2013/resource/9c1156be-cc9f-42a9-a3bc-41ed46fa97ef
- agency: Bureau of Infrastructure, Transport and Regional Economics
  name: Australian Road Deaths Database June 2016
  url: https://data.gov.au/dataset/australian-road-deaths-database/resource/fd646fdc-7788-4bea-a736-e4aeb0dd09a8
- agency: Australian Institute of Health and Welfare
  name: Australian Cancer Incidence and Mortality Combined Counts
  url: https://data.gov.au/dataset/australian-cancer-incidence-and-mortality/resource/7fbac314-4bf9-4601-b812-0307316ef5a4
- agency: Australian Bureau of Statistics
  name: Household Income and Income Distribution, Australia, 2009-10
  url: http://www.abs.gov.au/AUSSTATS/abs@.nsf/DetailsPage/6523.02009-10?OpenDocument
- agency: Australian Institute of Health and Welfare
  name: Youth Justice Detention Data
  url: https://data.gov.au/dataset/youth-justice-detention-data
- agency: Australian Institute of Health and Welfare
  name: National Drugs Strategy Household Survey
  url: https://data.gov.au/dataset/national-drugs-strategy-household-survey
event: canberra
hackerspace_url: https://2016.hackerspace.govhack.org/node/1666
image_url: https://2016.hackerspace.govhack.org/sites/default/files/field/image/logo_d.jpg
jurisdiction: act
prizes:
- australia-aihw-visualisation
- australia-creative-humanities-hack
- australia-inspired-by-research-hack
- australia-community-resilience-hack
- australia-storytelling-hack
project_title: Walks of Life
project_url: http://107.170.255.134/project205
repo:
  name: GitHub used for code versioning, link to team's google drive in the Git Readme
  type: github
  url: https://github.com/gakelly/project205
team_name: Project 205
video:
  type: youtube
  url: https://www.youtube.com/watch?v=Uc3L9mxHUEQ
---

Summary
The Walks of Life Project is a multiple choice quiz game to challenge and intrigue high school students with some surprising and interesting facts arranged by significant period of life derived from open data sets. The aim is to be informative about content and the range of open data available. 
 
The problem: When you know what you are looking for, open data tells a vivid and complex story about what life is like in Australia. For men and women, people who are: young, old, rich, poor, live in rural areas or cities and so much more. However, for those unfamiliar with a content area or how to access and interpret data, the huge volume of open data can be paralysing or daunting.
 
“Walks of life” is a cross-platform compatible webapp that allows for small, digestible pieces of open data to become stories, to help young people to start learning about what data is available and what it might mean for them. “Walks of Life” takes you through the lifespan of Sam, our virtual man or woman and challenges you to think about statistics from different life stages. 
 
As Sam progresses through his or her life, the user is quizzed on various questions, derived from open data sources, mainly from the Australian Institute of Health and Welfare. A correct answer progresses you to the next life stage. If the answer is incorrect, a life is lost, with 3 lives given before Sam dies, the game is over and you must begin again from birth. Once the game has ended, the user is presented with the most common cause of death and some interesting statistics about the age at which Sam died.
 
The questions in the quiz are based on descriptive statistics from the data. As the quiz progresses the questions are based on certain age ranges starting at 0-4 years to 75+ years. The questions are not aimed at being a comprehensive educational resource but rather to aid in framing and revealing the current possibility space presented by open data. For example: “What time of the day saw the most road deaths in 2010?” reveals that we have road death data down to the time of day. The question “For 15 to 19 year olds, what was the leading cause of death in 1909?” shows how far back the data goes in some datasets, in this case the GRIM books.
 
We used many different data sets to come up with multiple choice questions and fun facts on a range of issues by investigating and interpreting data and using analytics and pivot tables to uncover interesting statistics. These included:
 

General Record of Incidence of Mortality (GRIM) books


Premature mortality in Australia


Higher Education Attrition rate data 2005-2013


Australian Road Deaths Database 


Australian Cancer Incidence and Mortality Combined Counts


Household Income and Income Distribution, Australia, 2009-10


Youth Justice Detention Data


National Drugs Strategy Household Survey

 
The question database is an open ledger with a simple question format, updates to this are automatically available to be pulled and used as a question when the webapp is used. This makes walks of life flexible and a good place to showcase new data sets, new data variables or other innovations.
 
Release notes detailing these updates and changes is a concise and easy to use format for those familiar with the content area or data. Walks of Life’s value lies in delivering existing and emerging data and data capabilities to early high school students in a way that gives new data a narrative and makes it relatable to them. While the Project 205 team created questions from our own analysis, data and content experts can write their own questions to the ledger.
 
From a data owner or custodian's perspective, if you have ever wanted to get younger students engaged or involved in your data or research, Walks of Life gives you the capability to challenge or inspire students, rather than trying to force students into data a well designed, relatable question can lodge in your mind and foster intrinsic motivation. 
 
Currently questions are grouped and displayed by age, the next goal is adding indigenous status and simple location data, e.g. state. This will allow for students to navigate to lifestages of interest and be presented with targeted questions that are of significance to that particular life stage, further linking datasets to a relatable core system.