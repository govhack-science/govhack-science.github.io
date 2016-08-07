---
category: ''
datasets_used:
- agency: Transport and Main Roads
  name: 131940 Traffic and travel information GeoJSON API
  url: https://data.qld.gov.au/dataset/131940-traffic-and-travel-information-geojson-api
- agency: Natural Resources and Mines
  name: Flood extent series
  url: https://data.qld.gov.au/dataset/flood-extent-series
- agency: Queensland Fire and Emergency Services
  name: SES building locations
  url: https://data.qld.gov.au/dataset/ses-building-locations
event: brisbane
hackerspace_url: https://2016.hackerspace.govhack.org/node/1371
image_url: https://2016.hackerspace.govhack.org/sites/default/files/field/image/happycarl.png
jurisdiction: qld
prizes-entered:
- australia-creative-humanities-hack
- australia-fresh-data-hack-(api’s-and-data-services)
- australia-community-resilience-hack
- australia-location-data
- australia-no-boundaries-data-hack
- australia-securing-personal-property
- australia-transport-data
- australia-weather-forecast
- qld-age-friendly-community
- qld-evacuation---help-us-get-away!
- qld-mentoring-the-best-of-queensland
- qld-an-active-and-healthy-brisbane
- qld-engaging-with-brisbane-city-council
- qld-supporting-the-best-of-brisbane
project_title: 'Crikey!: Helping your community'
project_url: http://weigetpaid.timhadwen.com/
repo:
  name: 'Crikey!: Helping your community'
  type: github
  url: https://github.com/Weigetpaid
team_name: weigetpaid
video:
  type: youtube
  url: https://www.youtube.com/watch?v=OE-npkzdsdA
---

Project Description:
Weigetpaid is a Brisbane Govhack group consisting of UQ students and alumni. The team consists of Maddie Kingsley, Lena Ogg, Astrid Farmer, Tim Hadwen, Daniel Fraser, Isaac Hill, John Kent and Ken Yoong Lim. Every year Australia faces many destructive natural disasters that will affect every Australian directly or indirectly. Even though education and media coverage about these disasters is plentiful the majority of Aussies stay at home throughout these disasters. Many think the risk is not high enough to warrant proper preparation or evacuation. Each year many Aussies fall victim to issues that would have be easily avoidable if the proper procedure was followed creating tremendous repair bills and worse yet putting themselves and their families in danger. Our app Crikey is an emergency response app that works on addressing these key issues. Crikey will make it simpler to deduce how much danger you or your family are in along with provide a map with useful resources and critical information when preparing for dangerous conditions.  ​​​​​​​
 
Crikey is built for two primary users,  will be the helper and the helpee. Both Bill (helper) and Tanya (helpee) live in St Lucia and have just heard a weather broadcast about potential heavy rainfall in the coming days. They both realise the dangers of heavy rainfall and possible flooding so they both open Crikey to view where past flooding has occurred in their area. They can see a visual representation of past water levels from flooding on the map of their local area.  They can also toggle other important information like locations of local SES and live road closures. By selecting filters on the navigation they are able to toggle on and off certain data sets they want displayed on the map relevant to their situation. By switching the past floods toggle on, Tanya finds that her house is in a high risk flood zone which enforces her need for a proper evacuation plan. As Tanya does not own a car to make evacuation easier she goes to the “Help Me” page where she can request help from her neighbors. Tanya is directed to a form whereby she can categorise her new problem into transport, add a quick description and state the number of hours and helpers needed to complete her task.
 
Our other typical user Bill lives on top of a hill where the chance of flooding very low risk. He wants to offer his assistance to help others nearby while he still can. Bill looks on the map for icons that denote nearby people requesting assistance. Bill chooses Tanya’s icon at random. He reads her requests and chooses to help Tanya by giving her a lift to a friends house on higher ground incase flash flooding begins. He requests the job and contacts Tanya to arrange the picked up. 
 
Tanya has safely been moved out of harm's way without causing strain on emergency services. By using Crikey like Tanya and Bill, people can come together in a time of need, help eachother out and create a less stressful experience. Crikey will also help promote a healthy community atmosphere but also ensure that damages sustained and chance of loss of life from dangerous weather conditions is minimized. 
 
Crikey is a mobile orientated web app with a front end built on HTML, CSS and Javascript. Frameworks like Bootstrap and JQuery are used to construct the front end and the Google Maps API is the primary API used to get users locations and display data sets on the primary map page. Node.js and  ReSTful API were used to construct the backend.
 
Crikey gathers data from State and National government agencies and user location services to display map data visualisation. All of these datasets can be helpful when showing users if they are in a dangerous area and various resources available to them in their region like SES locations.  
 
Data Story:
 
We wanted to focus on natural disasters for Crikey because we wanted to provide a tool for making preparations and dealing with dangerous weather conditions much easier without relying on SES and emergency services that may be overworked or unavailable. 
 

SES Locations

We knew that our primary datasets would include weather conditions provided by BOM however if we really wanted our app to be a useful tool to people we would need to provide ways to find help from professional support and assistance. This dataset is used in our map and can be toggled on and off to be displayed on the map. 
2. Flood Series
This dataset shows the previous flood locations in the region. Floods are one of the most devastating natural disasters in Australia and especially Queensland. As this is the most likely case that people would be using Crikey we wanted to have a good display of how dangerous floods can be.  This data can be toggled on and off on the map. People can see how their location or entered address was affected by floods in the past.
 
3. Road Closures
When faced with any crisis situation a well organized and executed evacuation plan can be the difference between a potentially dangerous situation and ensuring the safety of you and your family. Dangerous weather especially has the power to close many roads which could possibly be essential to evacuation plans. By including this toggleable information on the map users can see what roads are currently open or closed.
What story does this tell: from start to finish in a disaster
Although there is no particular order that people need to browse the data a typical user situation will most likely use all of these datasets if they are in a disaster situation. A user needing help may first look for local SES locations and seek out their help.  If unavailable the user can request help from their community.
Another typical user case may be a user who instead wants to volunteer their time to help out their community. They may see which areas they live near were affected the most by floods in the past on the map and then search for people in need in those areas.