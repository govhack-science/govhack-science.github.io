---
datasets_used:
- agency: Australian Bureau of Statistics
  name: Experimental Industry Estimates by Geographic Area
  url: http://govhack.abs.gov.au/Index.aspx?DataSetCode=ABS_EIE
- agency: Department of Industry, Innovation and Science
  name: SA3 Region Innovation Data 2009-15S
  url: https://data.gov.au/dataset/sa3-region-innovation-data
- agency: Department of Employment
  name: Job Services Vacancy Data
  url: https://data.gov.au/dataset/jobs-services-australia-vacancy-data
- agency: Department of Employment
  name: Job Services data
  url: https://data.gov.au/dataset/job-services-australia-data
- agency: IP Australia
  name: Location of Australian Patent Applicants
  url: https://data.gov.au/dataset/patent-applicants
- agency: Australian Financial Security Authority
  name: Personal Insolvency by Postcode
  url: https://data.gov.au/dataset/personal-insolvency-postcode
event: melbourne-open-raster
hackerspace_url: https://2016.hackerspace.govhack.org/node/1891
image_url: https://2016.hackerspace.govhack.org/sites/default/files/field/image/Capture.PNG
jurisdiction: vic
prizes:
- australia-commerically-viable-hack
- australia-creative-humanities-hack
- australia-data-intelligence-hack
- australia-entrepreneurial-hack
- australia-future-australia-hack
- australia-innovative-ideas-hack
- australia-inspired-by-research-hack
- australia-ip-rights
- australia-local-industry-activity
- australia-training-data
- vic-how-can-city-of-melbourne-data-be-used-to-help-businesses-make-better-decisions?
project_title: Paranormal Distribution
project_url: http://avanauts-govhack2016.azurewebsites.net/
repo:
  name: Team Avanauts GitHub
  type: github
  url: https://github.com/RamondHaynes/GovHack2016_VIC_Team_Team-Avanauts
team_name: Team Avanauts
video:
  type: youtube
  url: https://youtu.be/rhYTX2qPP-4
---

Over the years, technological innovation has always caused shifts in employment. New processes and tools replace work previously done by people who must move on to find other productive ways to contribute to society. We are now on the cusp of an revolution that will dramatically change the employment landscape within our lifetimes: Robots, automated computer processing, artificial intelligence - whatever you call it - will reshape tasks from driving trucks to completing your tax return. 
So what advice do you give to a young person contemplating their career opportunities today?
Our hypothesis (or "hackothesis") is that ultimately, innovation drives growth, and the areas (both geographically, and in terms of specialization) where it drives that growth become the most lucrative points for people seeking employment.
We analyzed a range of datasets as proxies for innovation, industry activity and employment to determine whether the data supports our hackothesis. 
We used Microsoft Azure, Microsoft Azure SQL Database and Microsoft Power BI for the majority of the data processing, cleansing, storage and analysis. Larger data sets (in particular, the ABN lookup dataset) were pre-processed in Hadoop to extract the necessary attributes.
Our findings suggest our hackothesis has some merit. With some data wrangling, we were able to compose data sets with both location and time-series data, but found that there was little data offered that included additional attributes (e.g. Industry) that could be used to further refine the analysis. More granular data sources would have helped both to prove the result with more confidence and to provide additional lenses on the outcomes.
We had initially planned to leverage Azure Machine Learning as part of our analysis, and still have hope for a model that would provide a prediction based on a young person's preferences of priority areas and industry in which they would be advised to further their careers.