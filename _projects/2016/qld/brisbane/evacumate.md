---
category: ''
datasets_used:
- agency: Brisbane Lifestyle
  name: Community Halls
  url: https://www.data.brisbane.qld.gov.au/data/dataset/community-halls
- agency: BOM
  name: Queensland Warning Feed
  url: http://www.bom.gov.au/rss/?ref=ftr
- agency: Brisbane City Council
  name: Wifi hotspot locations - Libraries and Parks
  url: https://www.data.brisbane.qld.gov.au/data/dataset/wireless-hotspot-sites-libraries-and-parks/resource/9851b9fd-8a46-4268-9ece-4e45b143e8c9
- agency: Queensland Fire and Emergency Services
  name: SES building locations
  url: https://data.qld.gov.au/dataset/ses-building-locations
- agency: IAG
  name: IAG Flood Risk Data
  url: https://github.com/iag-edge-labs/flood-data
event: brisbane
hackerspace_url: https://2016.hackerspace.govhack.org/node/2946
jurisdiction: qld
prizes-entered:
- australia-fresh-data-hack-(api’s-and-data-services)
- australia-iag-flood-risk
- australia-innovative-ideas-hack
- qld-best-innovative-use-of-data-sets
- qld-evacuation---help-us-get-away!
- qld-getting-around-brisbane
- qld-mentoring-the-best-of-queensland
- qld-open-data-and-higher-education-award
- qld-best-visualisation-of-data
- qld-engaging-with-brisbane-city-council
- qld-supporting-the-best-of-brisbane
- qld-supporting-the-best-of-brisbane
project_title: EvacuMate
project_url: http://evacumate.xyz
repo:
  name: EvacuMate
  type: github
  url: https://github.com/ScriptSmith/EvacuMate
team_name: SoloBolo
video:
  alt_url: https://govhack-storage.s3-ap-southeast-2.amazonaws.com/2016/out.mp4
  type: unknown
  url: ''
---

EvacuMate is a friendly Facebook messenger bot, built on a platform that changes how we think about managing natural disasters.
It does this by:
Making community members aware of the possibility of a natural disaster and their responsibilities during an evacuation.
Helping disaster managers to better plan for and make smart choices during evacuations.
Giving the members of community informed options and the ability to establish a direct line of communication.
It's build using javasript in the back and front end. One file is deployed to Heroku and this is the foundation for bot itself which does most of the querying of public APIs. There is another server that maintains and visualises its own JSON data store that contains theoretical information about potential natural disasters like floods, storms and bushfires.
The Heroku bot queries datasets pertaining to Community Centres that are useful for recovery processes an temporary housing, BOM weather warning feeds that provide alerts about potentially dangerous weather, WiFi hotspot locations to get seperated and disconnected people back in contact with eachother, and SES building locations that provide opportunities for volunteering and rescuing during the recovery proccss.
I had a lot of fun with these geographic APIs because it was a bit of a challenge to think of an algorithmic way (in javascript) that I would be able to find the place that is closest to any given location.
The bot takes English phrases like "Adelaide Street" or your home address, converts this information into a GPS coordinate, and determines whether the location you have specified is safe according to a mock database it has maintained.
You can see this database visualised here: http://evacumate.xyz/map.html
And here in raw JSON: http://evacumate.xyz/locations.json
In a real world scenario, this database would be maintained by the people responding to natural disasters, continually being updated with fresh information and tweaked to better reflect the geographical locations that are being affected by the disaster.
This page is also connected to the IAG flood risk database. It which collects samples of coordinates as you move around the page, and over time builds up a heat-map visualisation of areas that it has deemed are at risk during floods.
You can click on the polygons that have been defined in the JSON file and then draw on the map, and a window will pop up providing context to the natural disaster or event that the shape pertains to. This system mirrors the textual information provided by the Facebook messenger bot, and thus it should be used to establish communication with those that need it and are seeking the pairing of textual information with rich interactive media.
Because the bot deals with a number of API sources, it has to interact with them in various ways. Over the course of this project I've learned to deal with JSON, XML, CSV and PSV files within Javascript, which has been a real challenge due to my unfamiliarity and aversion with asynchronous code, but I've really enjoyed the challenge and I'm confident that I've learned a lot because of this choice.
It's also been very interesting building the messenger bot itself. Having a bunch of functions deployed to a 'serverless' environment where I'm not even interacting with the computer fully, let alone the person at the other end, because Facebook acts as a proxy in this circumstance. The most challenging thing about this experience was having to deal with this situation because it is very difficult to debug errors and try new things because there is no way to mirror the way that Facebook was interacting with my bot locally, so debugging relied on deploying the bot and then picking apart the error log afterwards.
I'm very happy with the result I have achieved. I feel like I've accomplished what I set out to do which was to create a novel and usefull application that will actually provide real value during a natural disaster. People are becoming more an more connected to their mobile phones and I think bots like this are of such great use because of how streamlined and to-the-point they are. In what other situation would you be more frustrated by websites that you have to zoom in with your fingers on and click tiny links with. The facebook messenger platform is simple, but powerful in it's ability to deliver information.
I'm also very happy with the way that I leveraged its capabilities https://developers.facebook.com/docs/messenger-platform/. I was able to cover some advanced things like making use of buttons, callbacks and I was able to complete the extremely complicated setup process which is definitely not something I'd recommend to new programmers. Another thing that I'm proud of is that I managed to retain data when it is all too easy to lose it because Javascript is such a funtional language and it can be a big pain point passsing paramaters around all the time. In saying that, if I had a chance to do it again, I'd like to try python on the backend because I feel a bit more comfortable with its more rigid nature.