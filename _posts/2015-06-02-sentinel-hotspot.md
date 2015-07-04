---
layout: post
tags: datasets portals
title: Sentinel HotSpot Data
photo_url: http://www.scienceimage.csiro.au/images/cache/detail/976_0_EM2208.jpg
---

Sentinel Hotspots provides an important and consistent overview for management of fires across the country. The system was developed in the mid-2000 through a collaborative effort between Geoscience Australia, Australian Geospatial-Intelligence Organisation and CSIRO Land and Water. The system monitors hotspots nationally and provides timely hotspots information to its end-users. Sentinel has been a valuable input into the tools used by government and private agencies managing fires in Australia. 

Sentinel hotspots are point data, derived from (a growing number of) satellite-born instruments that detect light in the thermal wavelengths. Typically, the satellite data are processed with a specific algorithm that highlights areas with an unusually high temperature.

[![Sentinal Hotspots homepage]({{ site.url }}/resources/sentinel-portal.png)](http://sentinel.ga.gov.au/#/announcement "Sentinal Hotspots homepage")

A number of land management and emergency response agencies have taken data feeds from the Sentinel system to imbed into their routine fire management operations enhancing their situational awareness programs to assist staff, managers and the community. Hotspots data when merged with other spatial information provide a strategic picture to land managers; which allows them to understand the implications of a particular fire as well as to target resources.

Overall the Sentinel Hotspot Dataset goes back to August 2002 (27th) and contains more than 4.4 _million_ records, with data from a range of satellites including MODIS (from 27 August 2002) AVHRR (from 19 October 2006) and VIIRS (from December 2013).

### Accessing the data

GA provides documentation on the Sentinal Hotspot products [here (PDF)](http://sentinel.ga.gov.au/resources/img/help/Sentinel_Hotspots_Product_Desc.pdf). There are different ways and formats to access and visualise the actual hotspot data:

1. **OGC Web Services** - Sentinel allows data to be accessed via OGC Web Map Service (WMS) – which allow data to be accessed as image formats such as PNG, JPEG, and so on; and Web Feature Service (WFS) services – which allow data to be accessed as “feature” (text records). The WMS is located here: [http://sentinel.ga.gov.au/geoserver/wms?service=wms&version=1.1.1&request=getcapabilities](http://sentinel.ga.gov.au/geoserver/wms?service=wms&version=1.1.1&request=getcapabilities), and the WFS endpoint is located here: [http://sentinel.ga.gov.au/geoserver/wfs?service=wfs&version=1.1.1&request=getcapabilities](http://sentinel.ga.gov.au/geoserver/wfs?service=wfs&version=1.1.1&request=getcapabilities)
2. **Geoscience Australia FTP Server** - This contains a rolling “last 10 days” of the hotspots in text file format.  The data is “grouped” by satellite pass; there are 2 files for each satellite pass – the hotspots themselves (in CSV format) plus a metadata file containing some information about the satellite pass from which the hotspots were identified. The FTP endpoint is here: [ftp://ftp.ga.gov.au/outgoing-emergency-imagery/sentinel](ftp://ftp.ga.gov.au/outgoing-emergency-imagery/sentinel)
3. **User Interface** – GA also provides an online visualization and download tool to displays hotspots and other contextual information. There are two versions of the Sentinel UI: “Public”, which is accessible to the general public and “Secure”, which is accessible via a secure login. The Secure UI is primarily used by Emergency Management and contains hotspots produced by “others”. You can check this out here: [sentinel.ga.gov.au](http://sentinel.ga.gov.au/) 

### Still got questions?

<a href="mailto:nmgis@braidweb.net.au?Subject=Sentinel%20for%20GovHack%202015">Norman Mueller</a> is GA's data mentor for GovHack 2015 - you can contact him with any questions about accessing these services.
