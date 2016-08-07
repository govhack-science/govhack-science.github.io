---
category: ''
datasets_used:
- agency: Park CBR
  name: SmartParking Heat Map
  url: https://www.data.act.gov.au/Transport/SmartParking-Heat-Map/buwr-4ims
- agency: Park CBR
  name: SmartParking History
  url: https://www.data.act.gov.au/Transport/SmartParking-History/grth-myzs
- agency: Park CBR
  name: SmartParking Lots
  url: https://www.data.act.gov.au/Transport/SmartParking-Lots/h5gb-tess
- agency: Park CBR
  name: SmartParking Occupancy
  url: https://www.data.act.gov.au/Transport/SmartParking-Occupancy/fspr-n6cz
- agency: Park CBR
  name: Smart Parking API
  url: https://api.smartparking.com/
- agency: Park CBR
  name: SmartParking Stays
  url: https://www.data.act.gov.au/Transport/SmartParking-Stays/mya7-jn3e
event: canberra
hackerspace_url: https://2016.hackerspace.govhack.org/node/1586
jurisdiction: act
prizes:
- australia-fresh-data-hack-(api’s-and-data-services)
- australia-innovative-ideas-hack
- australia-location-data
- australia-transport-data
- tas-best-data-visualisation
- act-best-in-act
- act-best-use-of-act-government-smart-parking-data
- act-most-fun-use-of-act-government-data
- act-most-innovative-project-for-canberrans
project_title: Health Hack
project_url: http://www.googledrive.com/host/0B41QtSbrek35ZkpfalFQUXExcGM
repo:
  name: Google Drive
  type: google-drive
  url: https://drive.google.com/folderview?id=0BwBxzpU0caFoYnlHV2ZFTVp3aFk&usp=sharing
team_name: Health Hack
video:
  alt_url: https://govhack-storage.s3-ap-southeast-2.amazonaws.com/2016/HealthHack.mp4
  type: unknown
  url: ''
---

Our aim is to use the Smart Parking data to encourage people to consider parking further away and walk to their destinations rather than waiting around for a closer park.
Parking closer to shopping centres is often in high demand and oversubscribed.  Wouldn’t you prefer not to spend 10 or more minutes orbiting a close proximity carpark, getting frustrated when you could park 5 minutes walk further away and actually save time!  Short walks through a day are achievable activities for many people and have significant time and stress relief benefits. Also, these parking spots tend to have longer durations and cheaper parking rates!  Win for exercise and your hip pocket!
The SmartParking data from around the world shows that 30 percent of traffic in business areas are cars looking for car parks.  The City of San Francisco found that SmartParking reduced the search time for parking spots by 43 percent.  In France, the City of Nice found congestion reduced by 10 percent.  Canberra doesn’t have the traffic issues of most of these high density locations, but we do have peak intensity periods and a limited number of major employment and business locations which attract a dispersed population into smaller areas.
In terms of health benefits, future locations for SmartParking sites could be prioritised to those locations that have multiple dispersed sites, which broadens the array of options for users.
 
Data Story
We derived the average wait for a park from both the heatmap (24hr avg wait) and for the working day (0800-1800) and dinner (1800-2230).  This could be worked out dynamically in the future and possibly look at larger trends such as day of the week and take into consideration local sporting events, school holidays, etc.  We combined the derived average wait data and the distance from the chosen point to work out a total wait time including walking time. 
We then displayed this including a list of possible parks as determined by how far someone was willing to walk to a destination that they have selected.  This is sorted by total time (waiting to find a parking spot and walking).  The display uses live data from an API which shows currently available parking spaces.  (Note that we have assumed that this hack is used as a planning tool and ahead of a person's journey, so that spot is not necessarily still going to be available when they arrive in the area.  Accordingly, the time value that is presented for each spot uses the average wait time that is expected in each parking area).
Finally, when a given parking space is chosen the map insert will update and provide the user with the google walking directions to their destination.
 
Note:  for the demo you have to be logged into a google account. Chrome works best for this hack.