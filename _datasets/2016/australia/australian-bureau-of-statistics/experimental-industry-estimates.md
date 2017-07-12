---
dataset_url: http://govhack.abs.gov.au/Index.aspx?DataSetCode=ABS_EIE
excerpt_separator: <!--more-->
gid: experimental-industry-estimates
jurisdiction: australia
name: Experimental Industry Estimates by Geographic Area
organisation: australian-bureau-of-statistics
title: Experimental Industry Estimates by Geographic Area for 2004-05 to 2013-14 - Govhack
mentors:
  - oliver-berry
  - andrew-lalor
  - melissa-eaton
---

An collaborative experimental dataset by the [ABS](http://portal.govhack.org/sponsors/australian-bureau-of-statistics.html) and the [Department of Industry, Innovation and Science (DIIS)](http://portal.govhack.org/sponsors/department-of-industry-innovation-and-science.html).

<!--more-->

It contains estimates of annual business turnover, value added and full time equivalent for the financial years 2004-05 to 2013-14, classified by industry (ANZSIC 2006 - Division and Subdivision) and geographic region (ASGS 2011 - SA2).

__Please note that the purpose of this dataset is to allow GovHack participants to develop applications and other proof of concept products, with the understanding that any output is not suitable for analytical purposes. Due to the experimental nature and limitations of these data, the dataset should NOT be used for analytical, decision or policy making purposes.__

These estimates have been compiled using Business Activity Statement (BAS) and Pay As You Go (PAYG) data supplied to the ABS by the Australian Taxation Office. Industry data are based on the ABS's Business Register. Location data are based on the postcode of a business as reported to the ATO, which may represent the address of a Tax Agent, or, for businesses with multiple locations, the head office of that business. No attempt has been made to model business data for multiple locations, or to confirm actual location data. This may misrepresent the true location of a business. 

**Quality Statement - IMPORTANT!**

Limited quality assurance has been undertaken on these estimates. Some data have been suppressed to maintain statutory confidentiality requirements, others have been suppressed where estimates are likely to misrepresent true values. 

Location data are based on the postcode of a business as reported to the ATO, which may represent the address of a Tax Agent, or, for businesses with multiple locations, the head office of that business. No attempt has been made to model business data for multiple locations, or to confirm actual location data. This may misrepresent the true location of a business. 

Further, postcode data have been concorded to SA2s where possible. Where a postcode maps to multiple SA2s, data have been distributed based on population estimates. This methodology has NOT been endorsed or adopted by the ABS and should NOT be treated as a reliable indicator of business location. 

These estimates have been compiled using Business Activity Statement (BAS) and Pay As You Go (PAYG) data supplied to the ABS by the ATO. 

Complex business structures where a Type of activity unit (TAU) is created for business entities within an enterprise group may not be accurately represented in this data. Some TAUs have multiple ABNs and at the individual ABN level, the ANZSIC classes may be different to the TAU. This is not accounted for in these data. Please note that the ANZSIC classes in the BAS and PAYG data are based on self coding. The estimates should therefore be treated as experimental. 

In some cases, BAS data may be partially missing for an individual business (for example, data may be available for three out of four quarters). In other instances BAS data may be complete but PAYG data are missing (and vice versa). No imputation is applied for missing data. 

Users should take into consideration that any discussion of the data limitations or weaknesses is in the context of using the data for statistical purposes, and is not related to the ability of the data to support the ATO's core operational requirements.

Refer to the [ATO website](http://www.ato.gov.au) for more information about BAS and PAYG reporting requirements.

Limited quality assurance has been undertaken on these estimates. Some data have been suppressed to maintain statutory confidentiality requirements, others have been suppressed where estimates are likely to misrepresent true values. 

The purpose of this dataset is to allow GovHack participants to develop applications and other proof of concept products, with the understanding that any output is not suitable for analytical purposes

**Related or Complimentary Datasets**

* [SA3 Region Innovation Data 2009-15](../australia/department-of-industry-innovation-and-science/sa3-region-innovation-data-2009-15.html)
* [Characteristics of Temporary Skilled Migrants](../characteristics-of-temporary-skilled-migrants.html)

Please contact the data mentors for further inquiries.

**Data Explorers**

* [Datacube explorer and API Query Building tools](http://govhack.abs.gov.au/Index.aspx?DataSetCode=ABS_EIE)

**Explanatory Notes**

* TBC

**API Endpoints**

* SOAP: [http://govhack.abs.gov.au/sdmxws/sdmx.asmx]
* ReST (XML): govhack.abs.gov.au/restsdmx/sdmx.ashx

**Dataset Code**

* __ABS_EIE_SA2__

**ReST Call pattern**

```
govhack.abs.gov.au/restsdmx/sdmx.ashx/[METHOD]/ABS_EIE/[DIMENSIONS]/ABS(?startTime=YYYY&endTime=YYYY)
```

**Example call (ReST (XML) via CORS proxy**

*Question*

```
http://cors.io/?u="http://govhack.abs.gov.au/restsdmx/sdmx.ashx/GetData/ABS_EIE/DIMENSIONS/ABS?startTime=2014&endTime=2014"
```
(Note the use of quotes so that the ```&endTime=2014``` isn't passed as part of the cors.io argument but as part of the target URI.)
