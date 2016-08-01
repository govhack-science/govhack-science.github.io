---
datasets_used:
- agency: Adelaide City Council
  name: Outdoor dining permits - Adelaide City Council data provided via data.sa
  url: https://data.sa.gov.au/data/dataset/outdoor-dining-permits
- agency: Adelaide City Council
  name: 3D Model of the City of Adelaide data provided by data.sa
  url: https://data.sa.gov.au/data/dataset/3d-model
- agency: Dept for Health and Ageing - SA Health
  name: 'Hospital locations in SA (SA Public and Private Hospitals Locations):'
  url: https://data.sa.gov.au/data/dataset/sa-health-hospitals-locations
- agency: Adelaide City Council
  name: Events RSS feed
  url: https://data.sa.gov.au/data/dataset/events
event: adelaide
hackerspace_url: https://2016.hackerspace.govhack.org/node/1751
jurisdiction: sa
prizes:
- australia-commerically-viable-hack
- australia-creative-humanities-hack
- australia-entrepreneurial-hack
- australia-innovative-ideas-hack
- australia-community-resilience-hack
- australia-local-industry-activity
- australia-location-data
- australia-smarter-data
- sa-adelaide---best-in-location
- sa-adelaide-smart-city-state-champion
- sa-connecting-across-sa
- sa-helping-those-who-need-it
- sa-jemsoft-technology-development-prize
- sa-neighbourhood-and-community-confidence
- sa-premiers-prize-co-sponsored-by-business-sa-and-chiliad-consulting
- sa-premiers-prize-co-sponsored-by-microsoft
- sa-smart-lifestyles
- sa-supporting-sa-economy
- sa-vibrant-adelaide
project_title: R U Open
project_url: https://github.com/Unleashed2016/ruopen
repo:
  name: R U Open
  type: github
  url: https://github.com/Unleashed2016/ruopen
team_name: Bob's gang
video:
  type: youtube
  url: https://youtu.be/al08lttiCS0
---

Why R U Open
Our aim is to help a user find food and entertainment services in the immediate vicinity. The heart of the service is an Augmented Reality (AR) app which would use business and dining permits datasets (we have used Outdoor dining permits - Adelaide City Council found at data.sa.gov.au for proof-of-concept) to determine which business locations are open at the time the app is being used in the user's immediate vicinity.
The app would also allow relevant businesses to subscribe and provide information on menu and current campaigns (e.g. special offers) which can be displayed when the user taps on the marker designating the business location on the AR app.
Augmented reality based geolocation, routing and navigation:
We have developed the proof-of-concept of a browser-based Augmented Reality app to locate services which are open at the time of use (of the app) around the user. This kind of app would be normally developed using native APIs of the mobile phone OS (Android/iOS/Windows Mobile) and is extremely complex. The key concept is to use the mobile device sensors, mainly accelerometer, magnetometer, GPS, camera to establish the current location, orientation and point-of-view (in terms of camera viewport) of the device. On top, of the camera feed on the phone screen, data is superimposed in transparent/semi-transparent layers. This is done by creating virtual markers based on geolocated dataset(s) and using algorithms to determine the approximate distance and direction of heading for the marker in relation to the user's (and phone camera's) point-of-view. Navigation features can be added by using the phone's motion sensors to determine direction of movement as well.
Since our proof-of-concept has been developed within the time constraints of Unleashed 2016, Adelaide and Govhack, it has been developed using HTML5 geolocation (GPS), the orientation API (accelerometer) and WebGL (GPU). This PoC currently requires a standards compliant mobile browser (e.g. Firefox on Android). iOS does not currently support WebGL or WebRTC and has not implemented the DeviceOrientation API correctly. Please see this post to the W3C GeoLocation Working Group link for more detailed information. Awe.js link has been used for building the app. A transparent overlay of Google Maps has been used to display roads and locate markers on top of the camera feed for simplicity.
 
APIs Used

Awe.js: Used to simplify using HTML5 geolocation, orientation and WebGL


Three.js: Used as a cool WebGL library


Google Maps JS API: Used to superimpose a layer of Roads and Streets with names on top of the camera feed.


Google Maps Directions API: Used for routing and navigation from user's current location to destination (location of restaurant, club, etc.)


Backendless: mBaaS service for storing business related data (e.g. for subscribing businesses to provide details of the business, special offers, campaigns, etc). Ideally a custom developed backend service would be used.