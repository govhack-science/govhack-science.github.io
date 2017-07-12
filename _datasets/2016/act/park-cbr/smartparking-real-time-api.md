---
dataset_url: 'https://api.smartparking.com/ '
events:
- canberra
excerpt_separator: <!--more-->
gid: smartparking-real-time-api
jurisdiction: act
name: SmartParking real time API
organisation: act-chief-minister-treasury-and-economic-development-directorate
title: SmartParking real time API
mentors:
  - roger-rooney
---

The SmartLot API v1 lets you query for most locations and returns:

<!--more-->

â¢	Lot details
â¢	Lot operating hours
â¢	Lot tariffs
â¢	Lot occupancies
â¢	Unavailable bays
Lots are customer-defined groupings of parking bays within an overall site, and can include bays in multiple and non-contiguous sectors so long as they are all the same type; i.e. disabled, paid, residential etc. Each Lot's spatial GPS co-ordinates are provided as a single central point and not by each individual bay.
The APIs are RESTful; they are URLs with parameters submitted via HTTP. The APIs provide two different ways to get the data back to you, XML and JSON. Full help documentation on the API can be found at http://api.smartparking.com/Help