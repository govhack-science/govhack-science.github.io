---
category: ''
datasets_used:
- agency: Queensland Data Set
  name: Events Managed by the Queensland Reconstruction Authority API
  url: https://data.qld.gov.au/dataset/events-managed-by-the-queensland-reconstruction-authority/resource/3a1a022c-909f-44b2-b2a9-addeb82ad865
- agency: Queensland Government
  name: 2011-2014—Townsville Berth 1 Pumphouse tide gauge archived interval recordings
  url: https://data.qld.gov.au/dataset/townsville-tide-gauge-archived-interval-recordings/resource/b7b8dc88-86ef-495f-b501-604e902496d4
- agency: BOM
  name: Weather Station Directory
  url: http://www.bom.gov.au/climate/data/stations/
- agency: BOM
  name: Latest Weather Observations for Brisbane
  url: http://reg.bom.gov.au/products/IDQ60901/IDQ60901.94576.shtml#other_formats
- agency: Queensland Government
  name: Environment Agency Real Time flood-monitoring API
  url: http://environment.data.gov.uk/flood-monitoring/doc/reference,
- agency: Queensland Government
  name: Coastal Data System – Near real time storm tide data
  url: https://data.qld.gov.au/dataset/coastal-data-system-near-real-time-storm-tide-data
event: sunshine-coast
gid: safenet
hackerspace_url: https://2016.hackerspace.govhack.org/node/2081
image_url: https://2016.hackerspace.govhack.org/sites/default/files/field/image/dangerzonelogo_big_1.png
jurisdiction: qld
prizes-entered:
- australia-creative-humanities-hack
- australia-fresh-data-hack-(api’s-and-data-services)
- australia-iag-flood-risk
- australia-inspired-by-research-hack
- australia-community-resilience-hack
- australia-no-boundaries-data-hack
- qld-advance-queensland!
- qld-best-innovative-use-of-data-sets
- qld-educate-us!
- qld-evacuation---help-us-get-away!
- qld-open-data-and-higher-education-award
- qld-sunshine-coast---community
project_title: SafeNet
project_url: http://safenet.net23.net/
repo:
  name: SafeNet
  type: bitbucket
  url: https://bitbucket.org/Jaynesh_Vanmali/govhack-safenet
team_name: SafeNet
video:
  type: youtube
  url: https://www.youtube.com/watch?v=3-CfwHnlROE
---

Part I : The first is a general tool to assist with doing inferential statisticl analysis
The idea is to make it trivial to combine data from multiple datasets. It is wonderful to see how much data has been made available at the local, state and federal level as part of the open data initiative, and the orginsation of them and existing visualisation tools are impressive. What is missing, however, is the ability to combine datasets. So the first part of this project addresses that gap. It is designed to be fun and engaging to use; making it a valuable educational tool.
 
Part II : The other part of this project is an early warning mechanism for potentially disaster situations
Using the statistical analysis tool from part 1 we combine data about disasters (eg. when flooding has occured historically) with other possibly related data (eg. rainfall levels in an area). Where a corellation is found and we can infer that the releated data can be used to predict a disaster outcome, we can create a "warning table" which has precise numbers about how the data predicts the disaster. We then combine this warning table with live data sources (eg. current rainfall from the Beaureu of Meteorology) and now we have a system that is able to automatically alert and warn in a scenerio where some live data that we collect suggests historically that the result would be a disaster outcome.
We used the example of rainfall and flooding, obviously there are other data correlations available, such as tempreture and humidity as predictors for bushfires, but the idea is that with the educational tool we can start to discover correlations that are perhaps not as intuitively obvious.