---
category: ''
datasets_used:
- agency: Australian Bureau of Statistics
  name: Local Government Areas ASGS Non ABS Structures Ed 2011 Digital Boundaries in ESRI Shapefile Format
  url: http://www.abs.gov.au/AUSSTATS/abs@.nsf/DetailsPage/1270.0.55.003July%202011?OpenDocument
- agency: Australian Bureau of Statistics
  name: NRP, Industry, LGA, 2010-2014
  url: http://www.abs.gov.au/AUSSTATS/abs@.nsf/DetailsPage/1379.0.55.0012010-14?OpenDocument
- agency: Australian Bureau of Statistics
  name: '270.0.55.003 - Australian Statistical Geography Standard (ASGS): Volume 3 - Non ABS Structures, July 2011'
  url: http://www.abs.gov.au/AUSSTATS/abs@.nsf/DetailsPage/1270.0.55.003July%202011?OpenDocument
- agency: Department of Natural Resources and Mining
  name: Local Boundaries - QLD
  url: http://www.dnrm.qld.gov.au/mapping-data
event: brisbane-maker
hackerspace_url: https://2016.hackerspace.govhack.org/node/1676
image_url: https://2016.hackerspace.govhack.org/sites/default/files/field/image/IMG_0354c.jpg
jurisdiction: qld
prizes-entered:
- australia-commerically-viable-hack
- australia-creative-humanities-hack
- australia-data-intelligence-hack
- australia-entrepreneurial-hack
- australia-exploring-underground
- australia-community-resilience-hack
- australia-local-industry-activity
- australia-location-data
- australia-no-boundaries-data-hack
- australia-securing-personal-property
- australia-student-dropout-rates
- australia-training-data
- australia-weather-forecast
- qld-best-innovative-use-of-data-sets
- qld-brisbanes-art-and-heritage
- qld-create-a-cutting-edge-concept---the-science-sandpit!
- qld-educate-us!
- qld-getting-around-brisbane
- qld-linking-logan---getting-people-out-of-their-cars
- qld-open-data-and-higher-education-award
- qld-best-visualisation-of-data
- qld-engaging-with-brisbane-city-council
- qld-make-your-hack-a-thing
- qld-supporting-the-best-of-brisbane
- qld-supporting-the-best-of-brisbane
project_title: Vectoring Brisbane
project_url: ''
repo:
  name: Vectoring Brisbane Google Drive
  type: google-drive
  url: https://drive.google.com/open?id=0B0sRFS8JqdFKck1UT1Zib2ZlWEE
team_name: Crafty Hackers
video:
  type: youtube
  url: https://youtu.be/i55bI2y1dhI
---

For this project we were interested in seeing what we could create using geographical data from the Australian Bureau of Statistics.
We started with the local government areas for Queensland, looking at how we could use the shapes of the various districts to create a puzzle of our state.  We then ‘zoomed in’ to make a pendant of the Brisbane City Council area (river included!)
Using a different dataset, we also made a puzzle of the different postcode groups within the greater Brisbane area.
 
Other tools that were used:
​​​​​​​
The primary tool used to convert the ERSI shapefile data is Mapshaper:
https://github.com/mbloch/mapshaper
 
The primary tool used to convert the dataset data to GeoJSON files (for further processing with Python scripts) is ogr2ogr, which is part of GDAL:
http://www.gdal.org/
 
Challenges:
Our first challenge was in converting the currently available shp files into svg files so that we could manipulate them more easily.  
Our second challenge was matching up the geo data with other interesting data to be able to ‘colour code’ the districts.  Within the ABS data set we were able to match against Local Government Area (LGA) code, however this field wasn’t necessarily available in other local government datasets.
 

Applications:
By converting the geo data into svg, this opened up a whole heap of different possibilities for us.  Some ideas that we came up with include:
Jigsaw Puzzles - we produced one based on queensland, but there is nothing stopping the concept used from being scaled up (eg map of Australia, split by State), or scaled down (eg LGA split into suburb or postcode etc).  By utilising shp files for other countries, there is the opportunity to expand this concept globally which could make a great tool for learning geography.
Jewellery - we produced one based on the Brisbane City Council, highlighting the unique path of the Brisbane River.   As with above, this can be scaled up or scaled down as required and could make a really unique souvenir to keep or give to friends and/or family.
Pet Tags - personalise the experiences for pet owners in each LGA by having pet tags issued in the shape of the suburb, (or having the shape of the suburb pre-printed on the tag).  As an added extra on the pet tags, could have 'x marks the spot' to give an indication in the suburb where the pet is based (helpful for if someone finds your pet, to know which area to post the found pet posters.
Fridge Magnets - shaped like your LGA, containing key contact numbers (eg council, police station etc).
Cutting Boards - shaped like your State, LGA, Suburb or Postcode etc.
Vector files that people can use/manipulate to create their own 3d designs easily.
Where can we go with this:
Basically the shp files form a great way to visually represent data, so by overlaying other information against the LGA’s you can represent subsets by both colour and shape.
Eg using Carto, we were able to create a heat map showing the data by LGA for Light Commercial Vehicles, Passenger Vehicles etc
https://carto.com/
 
What we learned:
In the process of creating the visual representations of the data, not only did we become better educated on some of the specfics of the informatiton we were using, but we became better acquainted with the machinery used to make our data visualisations a reality. As the machines in question were also attached to computers, the opportuity to become more skilled in the use of the file formatting programs was realised, to the point that we are able to take that knowledge forward to further enrich other projects and "maker" opportunities in future.