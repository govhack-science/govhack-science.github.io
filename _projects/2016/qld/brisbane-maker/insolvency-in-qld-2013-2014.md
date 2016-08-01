---
datasets_used:
- agency: By Slomox [Public domain], via Wikimedia Commons
  name: SVG-Koort Queensland
  url: https://commons.wikimedia.org/wiki/File%3ASVG-Koort_Queensland.svg
- agency: Australian Financial Security Authority
  name: Personal insolvency by postcode
  url: https://data.gov.au/dataset/personal-insolvency-postcode#
- agency: Australian Bureau of Statistics
  name: '270.0.55.003 - Australian Statistical Geography Standard (ASGS): Volume 3 - Non ABS Structures, July 2011'
  url: http://www.abs.gov.au/AUSSTATS/abs@.nsf/DetailsPage/1270.0.55.003July%202011?OpenDocument
- agency: Department of Natural Resources and Mining
  name: Local Boundaries - QLD
  url: http://www.dnrm.qld.gov.au/mapping-data
- agency: Australian Bureau of Statistics
  name: Local Government Areas ASGS Non ABS Structures Ed 2011 Digital Boundaries in ESRI Shapefile Format
  url: https://drive.google.com/folderview?id=0B0sRFS8JqdFKck1UT1Zib2ZlWEE&usp=sharing
- agency: Australian Bureau of Statistics
  name: NRP, Industry, LGA, 2010-2014
  url: http://www.abs.gov.au/AUSSTATS/abs@.nsf/DetailsPage/1379.0.55.0012010-14?OpenDocument
event: brisbane-maker
hackerspace_url: https://2016.hackerspace.govhack.org/node/3106
jurisdiction: qld
prizes:
- australia-that-thing-we-all-need
- australia-creative-humanities-hack
- australia-data-intelligence-hack
- australia-machine-learning-hack
- australia-storytelling-hack
- australia-location-data
- australia-no-boundaries-data-hack
- australia-smarter-data
- qld-best-innovative-use-of-data-sets
- qld-brisbanes-art-and-heritage
- qld-best-visualisation-of-data
project_title: Insolvency in QLD 2013-2014
project_url: https://drive.google.com/drive/folders/0B0sRFS8JqdFKSnlGa1B6YjFzTmM
repo:
  name: Kitty and Keema's Insolvency Make
  type: google-drive
  url: https://drive.google.com/open?id=0B0sRFS8JqdFKSnlGa1B6YjFzTmM
team_name: Kitty and Keema
video:
  type: youtube
  url: https://youtu.be/q90K8FHw9Oc
---

This being the first time either of us had attended GovHack, we came with big plans. Especially when there's so. much. data!
Initially we had an idea of telling a story using the data we had to tie everything to each other, kind of like a diary of our hacking experiences, combined with the end results of our hacks. By chance we stumbled onto the insolvency data and wondered how we could tie this with the geospatial data we'd looked over for another project. As we are both "Makers", we wanted to see in what ways we could translate the digital data into a physical representation. A picture is worth a thousand words, afterall.
The project evolved significantly several times in less time than the space of a day. From a story, to a conceptual artistic representation of the reported insolvencies, to a 3D printed "exploded" Q1 tower, to a 3D printed and sliced Q1 tower and a laser cut representation of the proportion of insolvencies of the Gold Coast and QLD.
Here is a brief summary of what we did:
1. Created the file: https://docs.google.com/spreadsheets/d/16cMjfXuUqV_VpCH4OoqbrUBcP9BdYpod...
2. Extracted the 2013/2014 insolvency data out for that year by postcode.
3. We then obtained geospatial data with relevance from the postcode to suburbs for further analysis.
4. Upon allocating the postcodes to suburbs we again filtered and sorted in descending order, founding that a large number of insolvencies were from the Gold Coast region.
5. We accessed more Geospatial data to find the post codes only from the Gold Coast.
6. We then did a figured out the ratio of the insolvlencies with postcodes from the Gold Coast City Council area in comparison to the rest of QLD.
7. These ratios were then used to create a physical 3D printed representation of the ratios... one being the Q1 Tower, a physical representation of the Gold Goast, which represents the Total number of Insolvencies. We then spilt the building into the 3 different types of insolvency types: # of Bankruptcies, # of Debt Agreement Debtor and # of Personal Insolvency Agreement Debtors for the Gold Coast.
8. To further illustrate the ratios visually, we decided to laser cut the shape of QLD to display the state percentages in proportion to the Gold Coast statistics.
We certainly had bitten off more than we could chew for our first GovHack, with constant revisions to our project based on what data we could obtain and possibly link together, which didn't always lead down the road we originally envisioned. 
We were astounded at the percentage of insolvencies in the Gold Coast region alone, particularly the number of Personal Insolvency Agreements, especially when taking into account the accepted socioeconomic stereotype of the area. If only we had time to extract all the data nationally, that would definitely have been equally interesting to see translated into a visual representation.
 
Other tools used:
​​​​​​​
The primary tool used to convert the ERSI shapefile data is Mapshaper:
https://github.com/mbloch/mapshaper
 
The primary tool used to convert the dataset data to GeoJSON files (for further processing with Python scripts) is ogr2ogr, which is part of GDAL:
http://www.gdal.org/