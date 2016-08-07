---
category: ''
datasets_used:
- agency: Science, Information Technology and Innovation
  name: Toowoomba prison records 1864 to 1906
  url: https://data.qld.gov.au/dataset/indextoprisonerstriedtoowoomba1864-1903-csv
- agency: Queensland Government
  name: Datasets contained within QLD Government Challenge Website
  url: https://data.qld.gov.au/static-content/data-event/govhack/2016/challenge-wally
event: toowoomba
hackerspace_url: https://2016.hackerspace.govhack.org/node/1431
image_url: https://2016.hackerspace.govhack.org/sites/default/files/field/image/DYDincLogo.png
jurisdiction: qld
prizes:
- australia-commerically-viable-hack
- australia-entrepreneurial-hack
- australia-hiding-wally
project_title: De-Identify Your Data Inc
project_url: http://whereswally-prod.ap-southeast-2.elasticbeanstalk.com/
repo:
  name: Github Code Repository
  type: github
  url: https://github.com/GreasyBacon/whereswallygovhack2016
team_name: Makin' Bacon Flapjacks
video:
  type: youtube
  url: https://www.youtube.com/watch?v=qQKNAgVAKTs
---

"De-Identify Your Data", or "DYD" for short, has been created by the Toowoomba team "Makin' Bacon Flapjacks" over the last 2 days to provide a proof of concept of how the de-identification of datasets can be achieved in a timely and stress-free manner. Through utilizing an easy to use web application running on a nodeJS web server users can, in four straightforward steps, de-identify their datasets as well as view visualisations to address any specific queries of the data contained within. 
It has been built using the following technology:- nodeJS- express - bootstrap- jquery- d3plus
Step 1: Open the "DYD" app and upload your dataset in spreadsheet form. The app has not been developed with one specific spreadsheet dataset in mind, it was designed to work as long as your spreadsheet column headers define the respective rows of data contained within (hopefully!). 
Step 2: Select the columns of data that are 'identifing', and choose to remove or pseudonymise their contents. "DYD" provides suggestions of which columns of data appear to be a 'low' or 'high' risk category based on their names and their cell contents. Visualisation options (including field counts, averages and ranges) can also be selected at this stage, which are displayed in the next screen.
Step 3: View the generated visualisations, noting any statistics of potential note or importance. 
Step 4: Download the de-identified dataset, exported in spreadsheet form, and share with those that require it! Any spreadsheet column with the remove option selected will be deleted from the de-identified spreadshseet, while any column with pseudonymise selected will have the cell contents hashed. This is useful if you want to retain the frequency of similar values (such as a last name or similar identifier) but want the contents hidden when viewing the raw data.
​​​​​​​If this product were to be taken further, the following product features would be suggested for the product roadmap:- Additional file support (csv, txt etc)- Combining multiple uploaded datasets for visualisation purposes- Securely storing uploaded data and generating dynamic API endpoint for sharing de-identified information- User profiles/sign-on for tracking previously uploaded datasets