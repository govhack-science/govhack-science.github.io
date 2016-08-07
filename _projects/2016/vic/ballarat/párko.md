---
category: ''
datasets_used:
- agency: City of Ballarat
  name: Ballarat CBD Car Parking Occupancy
  url: http://data.gov.au/dataset/0fa308f2-20d2-4480-8c20-46cbc132be04/resource/6f2a571f-3a06-4047-be24-c40531b133d4/download/Ballarat-CBD-Parking-Occupancy.csv
event: ballarat
gid: párko
hackerspace_url: https://2016.hackerspace.govhack.org/node/2181
image_url: https://2016.hackerspace.govhack.org/sites/default/files/field/image/parko.png
jurisdiction: vic
prizes-entered:
- australia-commerically-viable-hack
- australia-innovative-ideas-hack
- vic-best-use-of-ballarat-data
- vic-smart-parking-in-ballarat
project_title: párko
project_url: http://parko.bhack.in
repo:
  name: Source Code
  type: github
  url: https://github.com/ballarat-hackerspace/parko
team_name: bHack Delta
video:
  type: youtube
  url: https://youtu.be/NlxkDuOg9hU
---

Our Idea
We were inspired by the Ballarat CBD Car Parking Occupancy data to produce an app/website that could both be used by residents to find the best times to find car parks and by local government to plan when more car parking is required in an area. We found that the data only covered a single 24 hour but we could see the potential of the data and so wanted to use it. To help supplement the data our project has two parts, one was to develop a small and cheap IoT device that could be installed in carparks to collect occupancy data over much longer time periods so that more data could be collected to make better predictions in the future. We also hope that the sensor device could be used to gather near real time data and have prototyped that on a breadboard with a Particle Photon device combined with a LDR to detect the presence of a car by detecting the shadow it projects on the carpark.
We also began working on a native Android app that would allow for a more rich experience that can collect a user's physical location and provide rich in app directions on how to find the nearest carpark that is likely to have a free spot. In future we would hope to be able to include more metadata about each park that includes the maximum period of time you can park there (e.g. 15min park, 2hr, 4hr, all day) and the cost of parking there so that visitors can chose a park the best meets their needs.
The data that our sensor collects would also be invaluable for future planning by local governments, we could setup automated alerts that trigger when carparks are full for very long periods of time which would indicate that people could be finding it hard to find parking.
How our prototype works
We created a simple circuit and program for a Particle Photon that used an LDR to detect the shadow of a car, when a change in shadow is detected (light to shadow or shadow to light) an event is triggered that is sent to the IFTTT.com service. IFTTT then adds a record to a Google Spreadsheet that records the time and if the carpark is occupied or free. This data is then exported to the web as a JSON data source which is then read by our example realtime web app and our Android app. We did not get time to present historical data in our apps but the final product would have this feature and would present to the use a histogram that highlights when a carpark is mostly empty and when it is mostly full letting the user make an educated decision on which carpark to choose. We would also make it possible for the app to choose the best carpark at any time for the user and present them with a route to get there with the click of a button.

Hardware
Our prototype hardware was very simple and uses an LDR to detect shadows, we tested this at night in a lit room and feel confident that this solution would also work well at night in well lit car parks but in dark car parks the LDR sensor could be replaced with a LED time of flight sensor or an ultrasonic sensor or even an induction sensor. We ran our prototype hardware on a pair of AA batteries for several hours and believe that a suitable solution to powering the sensor could be a combination of a LiPO battery pack combined with a small solar panel to keep it charged. Communications of our prototype is done over WiFi and we think for local governments that have free public WiFi this would be a good choice for them to use, and using WiFi would encourage more free WiFi to be deployed in our cities. If WiFi isn't available we could also use a 3G solution (e.g. use the Particle Electron) or perhaps a Zigbee mesh network. This might indicate that we need to produce several versions of the sensors with different network capabilities.
The physical design of the sensor could be similar to the cats eyes that exist on roads with the sensor in the area where the reflector is and the electronics between the sensor and under the solar panel (the sensor would look similar to a flat topped pyramid). By angling the sensor and solar panel and covering the sensor in an oleophobic coating it will then allow rain to wash away any oil or dirt that falls on the sensor helping them stay clean and operating.
We have aimed to keep the cost of the device to a minimum and don't expect the total cost of each sensor to exceed $100.
Some ideas
We don’t think there is any need to install a sensor in every single car park to collect useful data. We wanted it to be possible to install them in all spots because then we could also offer users with real time data of individual car park occupancy states. We estimate that even if only 10% or 20% of the spots in a lot have sensors we can still extrapolate occupancy percentages in a useful way for users and for government.