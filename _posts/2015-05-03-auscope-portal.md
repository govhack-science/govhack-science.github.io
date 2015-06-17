---
layout: post
tags: datasets portals
title: AuScope Portal
---

The AuScope portal contains a variety of Australia-wide geospatial and geoscientific datasets from the CSIRO, Geoscience Australia, the state Geological Surveys and several Australian universities.

[![AuScope portal homepage]({{ site.url }}/resources/auscope-portal.png)](http://portal.auscope.org/ "AuScope portal")

Some of the cooler datasets include:

- **National gravity and magnetic anomalies** - mineral exploration companies use these to locate deposits, but they also give you information about the local structure of the earth's crust.
- **Mineral and Mine Occurence data** - gives the locations of known mineral occurences, and active and inactive mine sites. This might be useful
- **ASTER spectral data products** - give you a range of mineral occurences at a 30 m pixel resolution for the entire continent of Australia, so you can see what dirt your house is sitting on.
- **National Virtual Core Library** - contains a range of spectral and image data for a large fraction of the geological cores held by Geoscience Australia and the State Surveys. Similar to the ASTER dataset, the spectral data tells you about what minerals are present in the core (with a pretty high resolution on the tens of centimetre scale), while the imagery is available both in high resolution core segments and also as entire core tray mosaics which might be interesting for image analysis.

You can turn on layers on the left hand side of the portal, and select portions of the datasets for download in various formats. As well as downloading data from the portal directly, most of the datasets are sitting behind Open Geospatial Consortium-compliant services (Web Feature Services and Web Coverage Services). This means you can pull them into anything that knows how to talk to these endpoints (hello [QGIS](http://www.qgis.org/en/site/), commercial offerings should work as well).

The exceptions are the mineral occurence and National Virtual Core Library (NVCL) data, which have their own special APIs. A how-to for the [mine location/mineral occurrence data is here](https://twiki.auscope.org/wiki/CoreLibrary/ERMLGovHackOerview) and there's one [here for the NVCL borehole APIs](https://twiki.auscope.org/wiki/CoreLibrary/NVCLGovHackOverview).
