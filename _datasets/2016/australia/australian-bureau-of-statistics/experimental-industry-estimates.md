---
dataset_url: http://govhack.abs.gov.au/Index.aspx?DataSetCode=ABS_EABLD
excerpt_separator: <!--more-->
gid: experimental-industry-estimates
jurisdiction: australia
name: Experimental Industry Estimates by Geographic Area for 2004-05 to 2013-14 - Govhack
organisation: australian-bureau-of-statistics
title: Experimental Industry Estimates by Geographic Area for 2004-05 to 2013-14 - Govhack
mentors:
  - oliver-berry
  - andrew-lalor
  - melissa-eaton
---

This experimental dataset is a collaboration between the [Australian Bureau of Statistics (ABS)](http://portal.govhack.org/sponsors/australian-bureau-of-statistics.html) and the [Department of Industry, Innovation and Science (DIIS)](http://portal.govhack.org/sponsors/department-of-industry-innovation-and-science.html). It contains estimates of annual business turnover, value added and full time equivalent for the financial years 2004-05 to 2013-14, classified by industry (ANZSIC 2006 - Division and Subdivision) and geographic region (ASGS 2011 - SA2).

<!--more-->

__Please note that the purpose of this dataset is to allow GovHack participants to develop applications and other proof of concept products, with the understanding that any output is not suitable for analytical purposes. Due to the experimental nature and limitations of these data, the dataset should NOT be used for analytical, decision or policy making purposes.__

These estimates have been compiled using Business Activity Statement (BAS) and Pay As You Go (PAYG) data supplied to the ABS by the Australian Taxation Office. Industry data are based on the ABS's Business Register. Location data are based on the postcode of a business as reported to the ATO, which may represent the address of a Tax Agent, or, for businesses with multiple locations, the head office of that business. No attempt has been made to model business data for multiple locations, or to confirm actual location data. This may misrepresent the true location of a business. 

Limited quality assurance has been undertaken on these estimates. Some data have been suppressed to maintain statutory confidentiality requirements, others have been suppressed where estimates are likely to misrepresent true values. 

Please refer to the [quality statement](#) which resides with the data for more information or contact the data mentors for further inquiries.

**Data Explorers**
* [Datacube explorer and API Query Building tools](http://govhack.abs.gov.au) under GovHack

**Explanatory Notes**
* 

**API Endpoints**
* SOAP: [http://stat.abs.gov.au/sdmxws/sdmx.asmx]
* ReST (XML): stat.abs.gov.au/restsdmx/sdmx.ashx

**Dataset Code**

* __TBC__

**ReST Call pattern**

```
stat.abs.gov.au/restsdmx/sdmx.ashx/[METHOD]/[DATASET_CODE]/[DIMENSIONS]/ABS(?startTime=YYYY&endTime=YYYY)
```

**Example call (ReST (XML) via CORS proxy**

*Question*

```
http://cors.io/?u="http://stat.abs.gov.au/restsdmx/sdmx.ashx/GetData/DATASET_CODE/DIMENSIONS/ABS?startTime=2014&endTime=2014"
```
(Note the use of quotes so that the ```&endTime=2014``` isn't passed as part of the cors.io argument but as part of the target URI.)
