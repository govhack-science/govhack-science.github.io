---
datasets_used:
- agency: Department of Social Services
  name: Settlement Data Extract
  url: https://data.gov.au/dataset/http-www-dss-gov-au-settlement-and-multicultural-affairs-programs-policy-settlement-services
- agency: Department of Employment
  name: Jobs Services Australia Vacancy Data 2009-2015
  url: https://data.gov.au/dataset/jobs-services-australia-vacancy-data/resource/cd69ad9b-428b-46b2-9edc-368fdd4daea6
event: canberra
hackerspace_url: https://2016.hackerspace.govhack.org/node/2886
image_url: https://2016.hackerspace.govhack.org/sites/default/files/field/image/application.PNG
jurisdiction: act
prizes:
- australia-creative-humanities-hack
- australia-data-intelligence-hack
- australia-future-australia-hack
- australia-inspired-by-research-hack
- australia-storytelling-hack
- australia-local-industry-activity
- australia-location-data
- australia-training-data
- tas-best-data-visualisation
- act-best-data-wrangling
project_title: Migrant Settlement and Job Australia Data Visualiser
project_url: https://github.com/jasonralston1/GovHack2016/raw/master/FinalApplicationSubmission.zip
repo:
  name: GitHub - Evidence of coding work
  type: github
  url: https://github.com/jasonralston1/GovHack2016
team_name: Spots on a Map
video:
  type: youtube
  url: https://www.youtube.com/watch?v=mPz5sZUITxQ
---

The application was written in C#, with GMap used to access the Google API. The application uses the Department of Social Services "Settlement Data Extract" data and the Jobs Services Australia "Jobs Services Vacancy Data" data, which it loads when the application is opened.
The data is focused on identified regions, and displayed on a Google map. Markers display where information (migrant data or job information) is availabile, and the information is displayed on the left-hand side of the screen.
For migrants, the markers are colour coded based on the number of migrants in that region. A key at the bottom of the application displays these values. This makes it easy to identify areas that have migrants, and where migants are more likely to be located.
For job vacancies a blue pin displays a region where job vacancies have been offered in a region. By clicking the pin, information on the role type and the number of positions available is displayed for viewing.
I focused on two different use cases for the application:
1. For government and Job Services Australia to look at where jobs are been offered in Australia, and see whether this matches where migrants are located. The visualisation shows a focus of jobs on the east coast, and this could mean migrants (both skilled and unskilled) on the west coast could be disadvantaged when it comes to getting jobs. Government could use this data to work out regions with low job availability, and create programs that assist migrants in either creating their own businesses or finding work in other ways (e.g. teleworking).
2. Education providers could use this visualisation and the data to identify areas where there are a large number of migrants that have low-level English skills or are unskilled. By looking at regions, they could then seek to offer services tailored to migrants in that area, with the view to helping them getting a job and to ensure they have a good standard of living in Australia.
This project was started by myself as a way to test some of the available open data while my main team was scoping. My main team, Australias Next Top Hacker, felt the initial prototype had potential, and encouraged me to work on it on the side of the main project. The ANTH main project can be viewed at https://2016.hackerspace.govhack.org/content/diis-project-jobs-and-growth. It was a fun challenge to develop this application by myself from concept to end product, particularly creating a video to highlight its functions and communicate the application's potential uses.