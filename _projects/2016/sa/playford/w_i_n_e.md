---
category: ''
datasets_used:
- agency: 'Unleashed 2014 Industry and Community Data (originator: Adelaide University)'
  name: Regional, national and global winegrape bearing areas, 2000 and 2010
  url: http://data.sa.gov.au/data/dataset/regional-national-and-global-winegrape-bearing-areas-2000-and-2010
- agency: ABS
  name: Vineyards
  url: http://data.sa.gov.au/data/dataset/vineyards
- agency: DEWNR
  name: Soil Sodium Toxicity (depth to toxic layer)
  url: http://data.sa.gov.au/data/dataset/sodium-depth
- agency: Department of premier and cabinet
  name: International Exports, ABS customised data
  url: http://data.sa.gov.au/data/dataset/international-exports-abs-customised-data
- agency: Playford Council
  name: Historic Places - Playford LGA
  url: https://data.sa.gov.au/data/dataset/historic-places-in-playford-lga
- agency: NCRIS Research Data and Infrastructure Group
  name: Atlas of Living Australia
  url: http://portal.govhack.org/datasets/2016/australia/ncris-research-data-and-infrastructure-group/atlas-of-living-australia.html
event: playford
hackerspace_url: https://2016.hackerspace.govhack.org/node/2836
image_url: https://2016.hackerspace.govhack.org/sites/default/files/field/image/Capture_0.PNG
jurisdiction: sa
prizes:
- australia-abc-news-content
- australia-that-thing-we-all-need
- australia-data-intelligence-hack
- australia-fresh-data-hack-(api’s-and-data-services)
- australia-innovative-ideas-hack
- australia-inspired-by-research-hack
- australia-local-industry-activity
- australia-location-data
- australia-ncris-data
- australia-no-boundaries-data-hack
- australia-paddock-to-plate-hack
- australia-weather-forecast
- sa-connecting-across-sa
- sa-supporting-sa-economy
- sa-playford---best-in-location
project_title: W_I_N_E
project_url: https://pastcompute.github.com/w_i_n_e
repo:
  name: Github repository
  type: github
  url: https://github.com/pastcompute/w_i_n_e
team_name: Ideation Generation
video:
  type: youtube
  url: https://youtu.be/LMnlcLQnDdc
---

Wine Industry National Explorer
Grape growing and wine production are key elements of the Australian economy.
The Wine Industry National Explorer provides growers, potential employees, students, policy makers, investors and researchers a valuable, intuitive visual tool for analysis of open datasets of relevance to grape growing.  W.I.N.E collates and aggregates information from a variety of disparate open data sets, previously inconveniently saved in spreadsheet form, and further provides an API to assist further development using the information.
With sufficient development and incorporate of a number of disparate datasets, including transformation of data from legacy formats such as spreadsheet into available interfaces with well designed API, the Wine Industry National Explorer  will become a valuable decision making tool.
Data Overview
Geographic information.
Wine and grape growing in Australia is organised by regions. The tool allows regions to be discovered and explored, drilling down into relevant statistics.
Variety information.
There are many grape varieties, the tool allows varieties to be discovered and explored, drilling down into relevant statistics.
The relationship between varieties and regions can be explored.
Economic information.
Statistics such as number of grape growing business can be explored.
The value of exports from wine products can be explored.
Resources.
By overlaying data such as the location of bores, soil and salinity profiles, and water sources, and climate data, the availability of resources and impact of threats on wine regions can be explored.
Inspiration.
The idea was to search of wine industry in the news via the ABC dataset, however the API does not allow searching, so please consider extending the API to be searchable.
API Preliminary Design
The proof of concept includes an API design document describing a simplified model for accessing consolidated wine industry data.
We used wine regions as a simple beginning.
The W_I_N_E s intended to be supported using a backend providing this API, and code for extracting and transforming the underlying data which is currently saved in spreadsheets on data.sa
This API is documented at https://github.com/pastcompute/w_i_n_e/blob/master/api.md
Open Data Issues
We had to by hand plot out the regions using google earth, because the data has not been made available on data.sa or elsewhere! Please consider adding this as a data set.
The ABC dataset API has no search facility!
We found an error in the Playford LGA historical places geographic data and were able to inform their unleashed volunteer of this.