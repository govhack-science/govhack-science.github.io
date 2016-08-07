---
category: ''
datasets_used:
- agency: Adelaide City Council
  name: On Street Parking Zones
  url: http://data.sa.gov.au/data/dataset/on-street-parking-zones
- agency: Environment Protection Authority
  name: Recent Air Quality
  url: http://data.sa.gov.au/data/dataset/recent-air-quality
- agency: Adelaide City Council
  name: UPark Car Parks - Available Spaces
  url: http://data.sa.gov.au/data/dataset/upark-car-parks-available-spaces
event: adelaide
hackerspace_url: https://2016.hackerspace.govhack.org/node/1186
image_url: https://2016.hackerspace.govhack.org/sites/default/files/field/image/BT_Logo_Set_Full%20Logo.png
jurisdiction: sa
prizes:
- australia-that-thing-we-all-need
- australia-creative-humanities-hack
- australia-data-intelligence-hack
- australia-entrepreneurial-hack
- australia-fresh-data-hack-(api’s-and-data-services)
- australia-innovative-ideas-hack
- australia-location-data
- australia-transport-data
- sa-adelaide---best-in-location
- sa-adelaide-smart-city-state-champion
- sa-helping-those-who-need-it
- sa-protecting-our-environment
- sa-safe-travel
- sa-smart-lifestyles
- sa-vibrant-adelaide
project_title: A 2 Green
project_url: http://www.a2green.com.au
repo:
  name: A2Green on GitHub
  type: github
  url: https://github.com/kingy68/a2green
team_name: Boomtown Hacks
video:
  type: vimeo
  url: https://vimeo.com/176908386
---

Team Boomtown Hacks is a ad-hoc team made up of some friends from around Adelaide. The team constsis of 4 people:
Jordan King - Developer and a smooth video voice.
Sam Trezise - Graphic Designer, held the ship together.
Haydn Dyer - The UI guy, the only one who has used Angular before...
James Mackay - The data guru, actually spend hours working out the parking data!!
The Application
http://www.a2green.com.au
Profile page materials: https://www.dropbox.com/sh/8qst0mj1gvjbrc6/AAAS49nKiL7PrAJr-QdXKCI_a?dl=0
All of our source materials: http://https://www.dropbox.com/sh/p59vrvwuztssfo6/AACHujmM2l8_zvHz8hJp1ge6a?dl=0
GitHub: https://github.com/kingy68/a2green
Our application, built entirely over the 48 hours, is called A2Green.
Note: the app only works for travelling into the Adelaide CBD!
Essentially the issue which we wanted to solve was what method of transport was the best option taking into account the following factors:
Quickness
Cheapness
Green Friendly
Availability
We all agreed that every time you're about to head into the city, you generally question what the best method of transport is (we even did it during the GovHack weekend). So what if we could provide a simple app, where you enter your start location and desination (only in the Adelaide CBD) and we give you our calculated options. We didnt want to choose the option for you, as you may have specific reasons to take your mode of transport, rather, we just present the options and let you judge it for yourself.
The Transport Options page takes into account the following factors as calculations:
How many car parks are there at the nearest street parking location to your destinations,
The price of driving into the city, this takes into account car usage factors like; tyre wear, servicing, fuel costs and the average cost for a 2 hour car park stay,
The traffic congestion, which is calculated by the distance you have to travel and the time Google tells us it will take, to get an average meters per second calculation.
We also present the nearest metro option from Google, and also a Bike option, which gives you the estimated calorie burn for the ride.
If you then do choose to drive, we then present you with the nearest street parking and U-Parking options and show some details about them. Once you decide which one you want to use, we will then show you it's location on a map. At this point of the app, we also let the user know the current days Air Quality Index for the Adelaide CBD, which might pursuade them to take a more carbon neutral option.
How It's Built
The application is Web Application for mobile, built on the Angular framework and adapted for mobile using http://mobileangularui.com/.
The soulution involves a number of datasets from South Australia:
Adelaide City Council - On Street Parking Zones
Adelaide City Council - UPark Car Parks - Available Spaces
Environment Protection Authority - Recent Air Quality
We also used the following development tools:
Free hosting on Amazon Web Services ($100 GovHack voucher)
Free developers account for Google Maps API
Where to Next?
We think this application has the potential to be expanded for a range of other car parking areas around Australia. All it needs is the parking data available to plug in. It would also be cool to incooporate this application into a full mobile parking solution where you no longer need to get out of your car and buy a ticket. The idea would be to let the user pay for their park on their phone, then a parking sensor would start timing their stay. As they get closer to the end of the stay they would be reminded that they park is to expire soon. It would also have a cost saving and efficiency effect on the Council themselves, as their inspectors could also be notified of soon to expire parks with cars still over the sensor. This would allow them to better decide where to go as an inspector. However, once the sensors are in place, the majority of the ticketing could be automated all together!
What We Didn't Get To
We had hoped to bring in real-time Adelaide Metro arrivals data, however, we were too pressed for time and never got around to it.
We also would have like to provide users with multiple parking options, but we didnt get to that either.
P.S. Jordan would also like to personally apologise to EPA, I called you EMA in our video and never got time to change it!!