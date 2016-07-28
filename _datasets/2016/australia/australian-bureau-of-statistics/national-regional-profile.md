---
dataset_url: http://www.abs.gov.au/ausstats/abs@.nsf/mf/1379.0.55.001
excerpt_separator: <!--more-->
gid: national-regional-profile
jurisdiction: australia
name: National Regional Profile 2010-14
organisation: australian-bureau-of-statistics
title: The National Regional Profile 2010-14
mentors:
  - 
---
The National Regional Profile (NRP) provides insight into the socio-economic and environmental characteristics of regions. Data are arranged under the broad themes of Economy, Industry, People, and Energy and Environment.

<!--more-->

The NRP presents data for 2010-14 for Local Government Areas, Australian Statistical Geography Standard regions (Statistical Areas 2, 3 and 4, and Greater Capital City Statistical Areas), States/Territories and Australia.

**Data Explorers**

* [Geospatial Visualisation](http://abs.gov.au/databyregion)
* [Datacube explorer and API Query Building tools](http://govhack.abs.gov.au) under General Statistics -> Regional

**Explanatory Notes**

* [Data Items A-Z](http://www.abs.gov.au/AUSSTATS/abs@.nsf/Lookup/1379.0.55.001Explanatory%20Notes12010-14?OpenDocument)
* [Explanatory Notes](http://www.abs.gov.au/AUSSTATS/abs@.nsf/Latestproducts/1379.0.55.001Explanatory%20Notes22010-14?opendocument&tabname=Notes&prodno=1379.0.55.001&issue=2010-14&num=&view=)
* [Glossary](http://www.abs.gov.au/AUSSTATS/abs@.nsf/Latestproducts/1379.0.55.001Glossary12010-14?opendocument&tabname=Notes&prodno=1379.0.55.001&issue=2010-14&num=&view=)

**API Endpoints**

* SOAP: [http://govhack.abs.gov.au/sdmxws/sdmx.asmx]
* ReST (XML): govhack.abs.gov.au/restsdmx/sdmx.ashx

**Dataset Codes**

* __ABS_REGIONAL_ASGS__ - by Australian Statistical Geography Standard regions (SA2 and above)

* __ABS_REGIONAL_LGA__ - by Local Government Area (2010-14), States/Territories and Australia)

**ReST Call pattern**

```
govhack.abs.gov.au/restsdmx/sdmx.ashx/[METHOD]/ABS_REGIONAL_ASGS/[DIMENSIONS]/ABS(?startTime=YYYY&endTime=YYYY)
```

**Example call (ReST (XML) via CORS proxy**

*What was the total value (in $AU millions) of construction for the City of Newcastle in 2014?*

```
http://govhack.io/?u="http://stat.abs.gov.au/restsdmx/sdmx.ashx/GetData/ABS_REGIONAL_LGA/BUILDING_10.LGA2014.15900.A/ABS?startTime=2014&endTime=2014"
```
(Note the use of quotes so that the ```&endTime=2014``` isn't passed as part of the cors.io argument but as part of the target URI.)
