---
category: ''
datasets_used:
- agency: NCRIS Research Data and Infrastructure Group
  name: Advanced Ecological Knowledge Observation System data (Australian plant and animal data)
  url: https://portal.aodn.org.au/search
event: camperdown-games
gid: home-sweet-home
hackerspace_url: https://2016.hackerspace.govhack.org/node/2831
jurisdiction: nsw
prizes-entered:
- australia-commerically-viable-hack
- australia-fresh-data-hack-(api’s-and-data-services)
- australia-innovative-ideas-hack
- australia-inspired-by-research-hack
- australia-machine-learning-hack
- australia-storytelling-hack
- australia-location-data
- australia-no-boundaries-data-hack
- wa-sustainable-coastlines-prize
- nsw-acceleration-award-govhack-nsw
project_title: Home Sweet Home
project_url: http://cptblack.cf/herefishyfishyfishy/web/demo.html
repo:
  name: Home Sweet Home
  type: bitbucket
  url: https://bitbucket.org/govhack_/herefishyfishyfishy
team_name: Underscore
video:
  alt_url: https://govhack-storage.s3-ap-southeast-2.amazonaws.com/2016/Final.mp4
  type: youtube
  url: https://youtu.be/y2e6x_gko94
---

Team Members: 

Lauren


Tom


Veronica

The Dataset: Advanced Ecological Knowledge Observation System data (Australian plant and animal data) [NCRIS Research Data and Infrastructure Group]
 
The ÆKOS system is primarily focused on systematically collected terrestrial ecosystem data using plot-based collection methods. These data are useful for reliable testing of fundamental ecosystem hypotheses. Ì KOS stores the plot-based data and Information that describes the data and its collection context. This information can be obtained from field manuals, notebooks, scientific papers, and reports.
 
More information: http://ecoinformatics.org.au/ecological_datasets
 
Home Sweet Home: Keeping up with the theme of "Games for Learning”, our team has decided to come up with a fun game to make learning interactive using the vast data sets available for all species. The intent of the game is to geographically place the species on a specific location (throughout Australia) based on their scientific names. Another cool idea we are implementing is to do a Flickr image search to receive the images for each scientific species name.
 
The technical tools used:

Html


Css


Javascript


Bootstrap


Jquery


Google maps api


Flickr image search


Python

 
The objective of the game: As a team we agreed that we need to have a significant learning experience from this game. Since some species are found only in certain regions, it would be fun to have a point based game where you can match a particular scientific name to one of its locations on the Australian Map. This is where the Google API comes handy.
To have just the species names, would be boring, so we figured out a way to use Fickr Image search to pull up a picture of the species, as a hint to aid the player in making a guess.
When you click on a location on the Australian Map, you would get points, based on how near/far you are from the location that species is found. Also all the locations on the map would briefly light up (like a heat wave) showing all the locations, and the intensity of the glow would depend on number of sightings of that species in that area.
How to Play: To begin with you would have a random set of species listed down on the left of the screen, and the Google map in the center of the screen. You would have the scores displayed on the right hand bottom corner of the map.

The first species name on the list, would be selected by default.


The picture (pulled from Flikr) would be displayed just on top of the species list. This would change as you move down the list based on which species name is selected.


Take a guess if you don’t already know! Click anywhere on the Map.


If you are way off, I am afraid you wouldn’t get many points, the closer you are to the sighting, the more points you get.


As soon as you click all the locations on the map with sightings of the species will light up (heat wave) .The glow of the heat wave would indicate how many instances of the sightings are reported in an area.


After your click the second species name would be selected and highlighted on the left hand panel, and you can just click anywhere on the map for your second try.


After you are done with the whole list, you would be shown your aggregate results. Here you can share your score on Facebook to brag.