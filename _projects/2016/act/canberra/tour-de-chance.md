---
category: ''
datasets_used:
- agency: data.act.gov.au
  name: Graffiti Sites
  url: https://www.data.act.gov.au/Infrastructure-and-Utilities/Graffiti-Sites/wdpz-r2ns
- agency: data.act.gov.au
  name: ACT Public Art List
  url: https://www.data.act.gov.au/Education/ACT-Public-Art-List/j746-krni
event: canberra
hackerspace_url: https://2016.hackerspace.govhack.org/node/1046
image_url: https://2016.hackerspace.govhack.org/sites/default/files/field/image/TourDeChance_POSTER.png
jurisdiction: act
prizes:
- australia-commerically-viable-hack
- australia-entrepreneurial-hack
- australia-innovative-ideas-hack
- australia-location-data
- australia-no-boundaries-data-hack
- act-best-data-wrangling
- act-best-in-act
- act-best-youth-hacker-team
- act-most-fun-use-of-act-government-data
- act-most-innovative-project-for-canberrans
project_title: Tour de Chance
project_url: https://canberra.TourDeChance.net
repo:
  name: tourdechance
  type: github
  url: https://github.com/skyrocketcafe/tourdechance
team_name: SkyrocketCafe
video:
  type: youtube
  url: https://www.youtube.com/watch?v=34sbBccB6WY
---

Tour de Chance
Take a Chance and Explore the Unexpected!There's more to do in Canberra than you ever imagined...
PROMO BLURB:Can't think of anything to do today or bored with your same old destinations? Have you ever been surprised and delighted by an unexpected discovery? Not sure what hidden treasures might be hidden around town that you would never even think to go looking for?
Then "Tour de Chance" is for you!
Rather than a simple A-to-Z list of attractions, "Tour de Chance" provides a random selection of things to do around town, from Museums and Galleries through fabulous street art, exciting tourist attractions, fun for the family, and much, much more.
You are sure to find something in Canberra to surprise and delight you using Tour de Chance!
But why not simply go to the places you know, or why not look up a boring list and choose? Because so often we only choose the "safe" things, the things we think we know about already. Nothing wrong with that, of course, but by taking a chance, by rolling the dice (or spinning the wheel in this case!) you might just discover something you never knew existed... about Canberra... about yourself.
Spin the wheel and visit what turns up... and we'll also present you some nearby alternatives to add to your experience.
Off course, if you don't like what the wheel gives you can always spin again. Or, you could just go do it anyway and see what eventuates... 
That is taking a chance... That is exploring the Unexpected!
TECHNICAL DETAILS:
"Tour de Chance" uses publicly available data sets from the ACT Government merged with other tourism related data to provide a single tourism destination database for the Canberra region suitable for use in this project. The specific data used is the "ACT Public Art List" and the "Graffiti Sites" list from data.act.gov.au .
From this combined database we developed a unique "spinner" randomiser for selection of specific tourism targets within a selected topic category and use the user's random selction to display a range of destination specific information including Google map features (location, travel directions etc.) and a randomly selected selction of nearby alternatives.
The spinner is a heavily modified version of a freely available javascript model tailored for the large amount of data this project included and is dynamically generated to that it can automatically encompass database updates and, eventually, multiple cities.
The project involved the use of Microsoft Excel, phpMyAdmin, Adobe Photoshop and the Sublime Text Editor.  The web programming aspects included HTML, PHP and Javascript, and a mySQL database. We are hosting it at "canberra.TourDeChance.net" on a Digital Ocean apache server.
BENEFITS:
This particular way of presenting tourism data is viewed by us as a way to show off some of the more unexpected and smaller tourism features of our city, features often overlooked or unknown about to most of us. It is seen as a particular benefit to smaller galleries and tourism enterprises and the people and businesses in the vicinity of the features included in our project.
DIFFICULTIES:
The Public Art database proved a difficult dataset to handle due to extensive "weird" character encodings in it, and the non-provision of a "tab delimited" CSV export option on the data.act.gov website (which would have been helpful due to the large tracts of text in the "DESCRIPTION" field that also included numerous commas, apostrophes and quotation marks... the enemy of simple CSV!).