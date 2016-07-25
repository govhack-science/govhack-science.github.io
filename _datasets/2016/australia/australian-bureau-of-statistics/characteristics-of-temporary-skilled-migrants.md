---
dataset_url: http://govhack.abs.gov.au/Index.aspx?DataSetCode=ABS_COTSM
excerpt_separator: <!--more-->
gid: characteristics-of-temporary-skilled-migrants
jurisdiction: australia
name: Characteristics of Temporary Skilled Migrants - GovHack Only Dataset
organisation: australian-bureau-of-statistics
title: Characteristics of Temporary Skilled Migrants  - GovHack Only Dataset
mentors:
  - 
---
__WARNING - GOVHACK QUALITY ONLY - NOT FOR PRODUCTION USE__

The Characteristics of Temporary Skilled Migrants test dataset is based on an experimental linked dataset. The test dataset mimics the structure of the real dataset (with the same data items and allowed values), however, all data in the test dataset is false, created through a randomisation process.

__As such, the dataset should NOT be used for analytical, decision or policy making purposes.__

The purpose of this test dataset is to allow GovHack participants to develop applications and other proof of concept products, with the understanding that any output is not suitable for analytical purposes.

<!--more-->

The Characteristics of Temporary Skilled Migrants Test Dataset is based on an experimental linked dataset that combines information on the migration characteristics of temporary skilled migrants (those holding a subclass 457 visa) with demographic, geographic, employment and education information from the 2011 Census. This test dataset has undergone a process of statistical randomisation and as such, should not be used for analytical or decision making purposes.

This dataset was created using information from the ABS Census of Population and Housing which was held on August 9, 2011, and the Department of Immigration and Border Protection's (DIBP) administrative data pertaining to temporary skilled migrants (visa subclass 457) in Australia on 31 July, 2011 (the closest available date to Census night).

For metadata regarding the Census data items displayed in this dataset, see the [2011 Census Dictionary](http://www.abs.gov.au/ausstats/abs@.nsf/mf/2901.0).

Data items available are State/Territory, Statistical Area Level 2, Age Group, Sex, Country of Birth, Industry, Occupation, Income and Highest Educational Attainment.

**Data Explorers**
* [Datacube explorer and API Query Building tools](http://govhack.abs.gov.au) under GovHack

**Explanatory Notes**
* [2011 Census Dictionary](http://www.abs.gov.au/ausstats/abs@.nsf/mf/2901.0)

**API Endpoints**
* SOAP: [http://stat.abs.gov.au/sdmxws/sdmx.asmx]
* ReST (XML): stat.abs.gov.au/restsdmx/sdmx.ashx

**Dataset Codes**

* __ABS_COTSM__

**ReST Call pattern**

```
stat.abs.gov.au/restsdmx/sdmx.ashx/[METHOD]/ABS_COTSM/[DIMENSIONS]/ABS(?startTime=YYYY&endTime=YYYY)
```

**Example call (ReST (XML) via CORS proxy**

*Question*

```
http://cors.io/?u="http://stat.abs.gov.au/restsdmx/sdmx.ashx/GetData/ABS_COTSM/[DIMS]/ABS?startTime=2014&endTime=2014"
```
(Note the use of quotes so that the ```&endTime=2014``` isn't passed as part of the cors.io argument but as part of the target URI.)
