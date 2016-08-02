---
datasets_used:
- agency: Transport for NSW
  name: Roads - Realtime Hazards
  url: http://portal.govhack.org/datasets/2016/nsw/transport-for-nsw/roads---realtime---hazards.html
- agency: City of Sydney
  name: Access Features and Barriers in Sydney
  url: http://portal.govhack.org/datasets/2016/nsw/city-of-sydney/access-features-and-barriers-in-sydney-city.html
- agency: Department of Social Services
  name: National Public Toilet Map
  url: https://data.gov.au/dataset/national-public-toilet-map
- agency: Google
  name: Google Maps JavaScript API
  url: https://developers.google.com/maps/documentation/javascript/
- agency: OpenStreetMap Foundation
  name: Open Street Maps
  url: http://wiki.openstreetmap.org/wiki/Planet.osm
event: sydney
hackerspace_url: https://2016.hackerspace.govhack.org/node/1691
image_url: https://2016.hackerspace.govhack.org/sites/default/files/field/image/screen%20shot%202016-07-31%20at%2011.56.51%20am.png
jurisdiction: nsw
prizes:
- australia-commerically-viable-hack
- australia-creative-humanities-hack
- australia-data-intelligence-hack
- australia-entrepreneurial-hack
- australia-future-australia-hack
- australia-innovative-ideas-hack
- australia-community-resilience-hack
- australia-local-industry-activity
- australia-location-data
- australia-new-infrastructure
- australia-smarter-data
- australia-transport-data
- nsw-acceleration-award-govhack-nsw
- nsw-lifting-the-barriers
- nsw-smart-cities-&-collaborative-economy
- nsw-travelling-with-us
- nsw-vibrant-sydney-night-time-economy
- nsw-acceleration-award
- nsw-acceleration-award-govhack-sydney
- nsw-most-fun-and-creative-use-of-data
- nsw-team-encouragement-award
project_title: Access Now
project_url: http://wpo5xc.axshare.com/#g=1&p=home
repo:
  name: Google Drive
  type: google-drive
  url: https://drive.google.com/folderview?id=0B6vUyydrFmzhS3g4SHJoNkFlSkk&usp=sharing
team_name: Access Now
video:
  type: vimeo
  url: https://vimeo.com/176899616
---

Google Doc with proper document formatting: https://docs.google.com/document/d/1knepenbnOS64l9GckSBrE7oRnG4fLpQaPboNxOO7Jrg/edit?usp=sharing Project DescriptionAccess Now, an easy to use, mobile trip planner that informs users of barriers and services on their route, letting them pre-plan and spontaneously change their pedestrian travel throughout their trip. 
On Friday night, a group of 5 competitors came together for the first time to tackle the issue of accessibility in our built environment put forth by the City of Sydney. Our mentors, Anna Rigg and Ann Hoban, filled us in on current technologies - unresponsive static pdfs that are updated infrequently - and the gaps in technology to address these issues. This became our problem. 
Using this as a starting point, we began by defining our users. What does it mean to be mobility impaired and what are the pain points? 
http://i86.photobucket.com/albums/k89/accessnow/2016-07-29%2022.17.42_zpsnulidqou.jpg 
From there, we began to ideate on what we could do to alleviate these pain points and began thinking about a trip planning app that doesn’t only explore transport options but also navigating public spaces. It’s not hard to find accessible train and bus information but getting to the station is only half the journey. 
http://i86.photobucket.com/albums/k89/accessnow/2016-07-29%2022.17.31_zpsk6kl3kcg.jpg 
Saturday morning, we defined the features that our app needed and expanded it to not just a mobile app, but a full solution that we wanted the council to be able to  adopt as a platform. We began as a trip planning app that provided both official and real-time information to the traveller, and evolved into a platform that involved the community. 
http://i86.photobucket.com/albums/k89/accessnow/IMG_1327_zpszs4vppfk.jpg 
We wanted to empower the user, to display the information they would need to be able to get around. We understood that not all people have the same needs and the user knew best what would work for them. 
http://i86.photobucket.com/albums/k89/accessnow/2016-07-30%2014.38.52_zps55a8gioe.jpg
http://i86.photobucket.com/albums/k89/accessnow/2016-07-30%2012.07.52_zpsigtqtklq.jpg 
Taking our feature mapping, we defined what was most important to have in our first product. We looked at three personas and workshopped their user journeys, the way that they would use the product and what it needed to look like for them. 
http://i86.photobucket.com/albums/k89/accessnow/IMG_1345_zpsozhvzv7a.jpg
http://i86.photobucket.com/albums/k89/accessnow/2016-07-30%2016.30.53_zps8tryoq0t.jpg 
http://i86.photobucket.com/albums/k89/accessnow/IMG_1346_zpsmd9jurrh.jpg 
 
From here, wireframes were built. 
And finally, a clickable prototype. 
How we used the dataSince we were tackling the problem of accessibility in the built environment, the dataset from the City of Sydney was the one of greatest benefit to us. We were able to get a strong understanding of the meaning of the data by talking to Anna and Ann from the City of Sydney who were able to provide content and comment on the completeness of the data. 
As a team, we completed an activity on Saturday morning where we brainstormed all the possible datasets we thought would be of use to us. We categorised them into barriers and services and had about 20 item listed all together. We then developed a scale to rate each item, with 1 meaning the data is easily available and 5 indicating that it would be very hard to acquire the data in our 46 hour timeframe. As Ian and Royston were going through the datasets on Friday night, we were able able to identify and rate each item. We then decided to take the items rated between 1 to 3 and work with them to create proof of concepts and shape our solution. 
We focused on location based data for our technical proof of concept. The City of Sydney Access Barriers dataset had information on stairs, secure taxi ranks and mobility parking spaces. Notably, it was missing information on accessible toilets and accessible bus stops. We found data on toilets from the National Public Toilet Register and we acquired bus stop locations and accessibility information fromt the Transport for NSW data catalogue. We were able to augment the primary dataset with these two additional datasets to create a more comprehensive dataset that would of use to our user community. 
The Transport for NSW data catalogue also has real-time information on hazards including roadworks. This is useful to people with mobility issues as streets with roadwork often have disrupted access for pedestrians. Access Now would integrate the real time information to give users the option to avoid roads with roadwork so that minimal disruption is experienced on their journey. 
One type of data that we found hard to acquire was data on incline and slopes. This is significant because people with mobility issues may not be able to rise up steep slopes, especially in crutches or in a wheelchair. Prior information on the slope of a street would help people plan their journey to avoid steep slopes. Our research indicated that Google Maps was able to provide data for elevation for a given route, but this functionality was only free for a limited number of calls. Our research into Open Street Maps showed that it had the capability to capture information on inclines through user contributions being tagged. We were able to successfully tag 3 streets near Circular Quay with incline tag. OSM allows for the data to be downloaded from the platform as well and therefore if we are able to capture information on inclines on OSM, we would be able to present it visually in Access Now if the user preference is to avoid slopes.
Technical proof of conceptWe were blessed with a rich set of data specific to the built environment in Sydney CBD. This data consisted of location points of stairs, mobility parking and secure taxi ranks among other points of interests relevant to access and barriers. We took the data in its raw form and brainstormed around how we could make it more accessible to a wider audience. We made an assumption that the primary audience for our data would be people with mobility issues and their carers. The wide reach of the internet and the prolific nature of smartphones lent itself to the solution being one that will be used on a desktop or mobile device. The advantage of using these platforms is that they connect to the internet and hence we can leverage the vast amount of internet resources that already exist to realise our idea into a viable solution.
The result of our brainstorming for visualising the location coordinates was to represent it on an electronic map. The two contenders in the mapping space that are simplest to implement are Google Map Maker and Open Street Maps. For our first proof of concept, we created a new ‘My map’ on Google Maps to experiment with importing our data and displaying it on an interactive map. This can be done on http://google.com.au/mymaps. We segmented the data points into 10 categories that were identified in the data. Examples of these are train stations, stairs and secure taxi ranks. We created 10 csv files with one category of data each. On My Maps, we created a new layer on the map and imported a single category csv file. Once we identified which column contains the latitude, longitude and facility name, we were immediately able to see the point on our map. We repeated this process to create and import all 10 categories into our custom map. To enhance the usability, we defined custom icons for each category so that they could be distinguished easily. Our ability to complete this concept in a short period of time (under 2 hours) increased our confidence in the viability of Access Now as a solution.
When looking at the primary dataset on city barriers, we noticed that information on accessible toilets was not particularly comprehensive. We came across the dataset on public toilets available at the National Register of Public Toilets. We downloaded this dataset and using Microsoft Excel, we were quickly able to filter the toilets in the Postcode 2000 region. We exported this data to a csv file and imported it into our ‘My Map’ so that it was enhanced with Toilet information as well. We were able to successfully complete this concept and the result can be viewed at this link: https://www.google.com/maps/d/viewer?mid=1UM2o7nuVkvUKFarjn1tusyXZrIk 

The other major alternative to My Maps from Google is Open Street Map (OSM). The Open Street Map project is a community build platform for mapping the world through user contributions. The benefit of using OSM is all the data and mapping information can be used with an open source licence and without limitation. It can also be enhanced and modified with user contributions and is highly extensible. The team agreed that OSM was a strong contender for our Access Now platform and any user contributions would be available for use by external communities as well.
We found a service called uMap which allows users to create custom maps in a similar way to My Maps from Google. Link: https://umap.openstreetmap.fr/en/ . We were able to create our custom map and import data from csv files as we did with My Maps. This was achieved in a similar timeframe and we concluded that both OSM and Google Maps would be strong contenders for our backend platform, which OSM being slightly favoured due to its openness and focus on user contribution.
Our Open Street Map: https://umap.openstreetmap.fr/en/map/access-now_96326#16/-33.8587/151.2093 

One key point to note is that both OSM and Google’s My Maps are solutions that can be implemented in the very near future and provide greater usability compared to existing solutions available to our users. 
 

 
Demo websiteSandbox server
https://myskillsmanager.com/sandbox/outlet.biz?pid=60000&i1=39
 
Usernames access1@indxn.me pw Access1
Usernames access2@indxn.me pw Access2
Usernames access3@indxn.me pw Access3
Mapping MenuThis is the main customer interface to the system and it will main interface for customers.

Planning  MenuThis is a methodology that for the authoring, collaboration,distribution and sharing of the Disability Access Plan
This system could be customer specific ie “Sydney City Council” will have their own work space.  This produces a series of  fully customisable documents or sub document that can be linked, packaged and distributed quickly and easily within the workspace.
 
However the plan documents can be copies and shared between workspaces.  Therefore the the finalised (or preliminary)   for the Disability Access Plan (DAP) for any Council or State agency   could be copied to and customised by another Council or agency.
 
This method would allow any particular section of the DAP to be directly linked directly to the spatial data that is associated with it.
 
Same spatial data can be shared between any different work spaces.
Documents  MenuList of links
This section of the app/web console is conceptually links directly to the paper/ pdf based  that the some users may prefer.  This is a method that will allow a targeted list to prioritise the digitalisation of data moving forward.  
Community  MenuAll data
The method has been created that allows any textual data from any dataset  to be converted to a spatial map view.  
 
These list of data are categorised according the validity of the data

Registered formally validated data 


Documented data that not been formally.  ( the conformation of this data should be prioritised to move it into category No 1.


Crowd sourced data from expert users such as your existing rangers and staff (doing their normal work)


User generated content  (UGC  where the users history with reference to a accuracy with reference to other users UGC for similar routes.  Statistical analysis should be  allow very rapid rating of all UGC.  

An options has been provided so that uses could mash together and represent spatially any of our combinations of data.
 
Google Maps directions API will be used to deliver turn by turn directions from and to any locations.
 
Addition datasets ( bus stop, trains, schools, universities and other destination) were prepared but not uploaded to our server that will allow us to filter a where the user want to come and go to.
 

Accreditation Register
The idea has only been prepare and conceptually design.  The object was to provide an audit type accreditation that potentially rates all businesses and restaurants with references to their access friendliness and compliance. 
 
Description of Crowd Data Collection methodology ( Route Register)
The method allows any user to complete the safe access route for for an unique Route ID.  The routeid managed in a register to be completed. This register notes a start location and an end destination target.  The user simply collects starts walking a safe way between the two locations (multiple users can complete the route).   

Figure Crowd sourced data capture using our click and walk methodology
 
Leader board
And an actual leader board has been created to allow a quick overview of Community Contributions.