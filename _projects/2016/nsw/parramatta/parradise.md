---
datasets_used:
- agency: Parramatta City Council
  name: CoP Service Requests 2015.07-2016.06
  url: https://drive.google.com/drive/u/0/folders/0B9iAn5sxT0i8TzdjZGxmMkIzMFU
- agency: Parramatta City Council
  name: Parramatta Parcels Points
  url: https://drive.google.com/drive/u/0/folders/0B9iAn5sxT0i8TzdjZGxmMkIzMFU
- agency: Transport for NSW
  name: Facilities & Operators
  url: http://portal.govhack.org/datasets/2016/nsw/transport-for-nsw/public-transport---facilities-and-operators.html
- agency: Transport for NSW
  name: Full Greater Sydney GTFS Static
  url: https://opendata.transport.nsw.gov.au/app/dashboard.html
event: parramatta
hackerspace_url: https://2016.hackerspace.govhack.org/node/2686
jurisdiction: nsw
prizes:
- australia-creative-humanities-hack
- australia-location-data
- australia-securing-personal-property
- nsw-smart-cities-&-collaborative-economy
- nsw-city-of-parramatta-civic-hack
project_title: Parradise
project_url: http://52.65.95.141/
repo:
  name: GovHack2016 - Parradise
  type: github
  url: https://github.com/sutantyo/GovHack2016
team_name: KanyeSwift2020
video:
  alt_url: https://govhack-storage.s3-ap-southeast-2.amazonaws.com/2016/COMBINED_720P.mov
  type: youtube
  url: https://www.youtube.com/watch?v=4T5KZFUw7Y8
---

The Story of The Data
The data that we used is the Parramatta City Council's Records of Service Requests from July 2015 to June 2016. These are a list of requests, complaints, and notifications that were received by the council in the past year, such as waste service (waste bins and collection), pollution report, illegal dumping, police attendance, etc. The spreadsheet contains around 25,000 lines, with about 200 different request types. Each row contains the service request, the date it was reported and acted upon, and the address related to the event or incident.
We also used another spreadsheet supplied by the Parramatta City Council, the Parcel Points, which contains information about lot numbers of Parramatta addresses, and most importantly, the latitude and longitudinal coordinates of each address, which we needed to project these reports on the map. We also used a few other open data, including transport information for NSW, to obtain locations of public transport amenities.
We had to spend a few hours fixing the data to suit our need. In particular, as to be expected from manually recorded data, a lot of the addresses (about 20%) in the service request spreadsheet did not match the addresses in the second spreadsheet, making it impossible to obtain a proper geo-coordinates for the service requests. A simple example would be one address containing unit or flat number, e.g. 1/535 Victoria Rd, whereas the other spreadsheet only contains the street number, e.g. 535 Victoria Rd. We managed to fix the majority of the data, leaving about 500 addresses unresolved, so we are still using about 98% of the service request data. The updated CSV is on our GitHub page should anyone is interested to use it.
The Inspiration for The Project
At the start, we thought it would be interesting to present this data visually so that someone who is thinking of moving into a Parramatta City Council area can have an idea of the neighbourhood. It would also be interesting to see if there are correlations between various events and other available statistics such property value or crime rates. As we started to do the project, we realise that this is a very useful too for city planning. Our inspiration comes from city simulation games such as SimCity where you have a very detailed view of the neighbourhoods. 
It is easy to find economic or demographic data about our neighbourhood, e.g. income rates or crime rates, but the data that we have is quite distinct in that they feel very personal. For example, these are some of the reports that you can find in the data:
Removal of illegally dumped rubbish, furnitures, mattresses
Food borne illness report, food poisoning, food shop hygiene
Dog barking, animal attack, stray animals
Non-compliant development
and these kind of data doesn't seem to be readily available otherwise. I personally had fun just snooping around the neighbourhoods and finding out what had happened. It feels very personal, and it is certainly fun to explore the neighbourhood!
The Application
To present this information, we group the various requests to a dozen or so categories (from 200 different types), and represent each incident with an icon that we then display on a google map overlay. If the user click on a particular point on the map, it will place a marker on the nearest property and then place an icon for each incident that happened with a certain radius of this property (about 1km radius). The address will be listed at the top, and at the bottom of the map you will see some information about the closest public transport.
To see the exact event that had happened, the user can hover on the icon for more information. Note that we had to group various events together in an arbitrary way, and sometimes it is not very clear how the events should be grouped, thus there can be some inconsistencies from now and then (should stolen waste bin be a police matter or a waste service matter?)
The application is self-explanatory, and should be very intuitive to use. I won't bore you with the details of the implementation, but I wil just mention that we only used simple webtools, using node.js and postgres for the back-end and Google APIs, Bootstrap, and d3.js for the front-end. We will update the  GitHub page so that anyone interested can have a better idea of what we used.
The Future?
Given the time that we had, we certainly did not do half the stuffs that we wanted to do. Here are a list of some of the things we would have wanted to implement:
A filter so that we can focus only on one or two types of events,
Adding various public amenities, such as schools, day-care centre, 
Suburbs summary, or report by regions​​​​​​
and many others!