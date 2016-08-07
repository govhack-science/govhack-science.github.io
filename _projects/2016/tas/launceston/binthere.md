---
category: ''
datasets_used:
- agency: Launceston City Council
  name: Rubbish Bins
  url: http://lcc.launceston.opendata.arcgis.com/datasets/ea26b0215cc04ba49aec0480a61459a8_0
- agency: City of Hobart
  name: HCC Waste bins 2015
  url: http://data-1.hobartcc.opendata.arcgis.com/datasets/9f59ef23d594497faf422d4721d95839_0
event: launceston
hackerspace_url: https://2016.hackerspace.govhack.org/node/2816
image_url: https://2016.hackerspace.govhack.org/sites/default/files/field/image/BinLogo-01_0.png
jurisdiction: tas
prizes:
- australia-location-data
- tas-best-data-visualisation
- tas-best-use-of-tasmanian-local-council-open-data
- tas-design-excellence
- wa-encouragement-award
- tas-most-commercial-potential
- tas-most-disruptive-innovation
- tas-most-outstanding-tasmanian-benefit
project_title: BinThere
project_url: ''
repo:
  name: BinThere Repository
  type: github
  url: https://github.com/bldh/BinThere
team_name: Bin There
video:
  type: youtube
  url: https://youtu.be/Kmnyp_wlHBY
---

BinThere is an iOS application designed to help members of the public find their nearest public bin and is designed to help both members of the general public and council organisations.
Users of the application can open up the app to very quickly find the nearest rubbish bin, recycling bin or dog waste area.  The idea is that if someone has some rubbish that they need to dispose of, but they can't see a bin in the immediate vicinity they can very quickly get directions to the closest bin of the appropriate type.  Also, if someone has some recyclable rubbish, and they can see a general waste bin, but they can't see a recycling bin, BinThere will let them know if there is an appropriate recycling bin nearby.
In addition to helping people find bins, the app also enables users to report bins that are full/overflowing, damaged/vandalised, or dog waste stations that have run out of plastic bags.  This is done within the native map interface.  With a couple of taps, the user can send information about bins that need attention to the appropriate person at their local council.
The application uses datasets on bin location from the Hobart City Council and the Launceston City Council.  The data tells us where bins are located (longitude and latitude) and what kind of bins they are.  We integrate this data with Apple Maps to place pins on the map around the user to represent nearby bins.  While we've only supported the Hobart and Launceston council areas in this version of the project, it would be relatively straightforward to add other council areas to the app where the necessary data is available.
We think that this project has some great potential as a tool that can help ordinary people who want to do the right thing (find a bin/clean up after their dog/put recycling in the appropriate bin), and also as a tool that can help councils to keep on top of issues relating to the bins they manage.  We believe that there's a fair bit of commercial potential for this project as well.  While it's a fairly simple idea, we suspect that the reporting functionality and the ability to brand the app and keep bin location data up to date would actually be quite valuable to local councils and that they would probably be willing to pay an annual licensing fee to use the service.
All in all, we're extremely pleased with how the app has come out.  We've completed a fully functioning iOS app that integrates data from two local council areas and could actually be used live by test users tomorrow if they wanted to.  Not a bad result!