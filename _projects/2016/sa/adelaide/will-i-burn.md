---
category: ''
datasets_used:
- agency: ''
  name: Bushfires and Prescribed Burns History
  url: https://data.sa.gov.au/data/dataset/e5434c77-9815-48e6-8ea7-fb35c78f6786
- agency: Dept of Environment, Water and Natural Resources
  name: Goyder Institute for Water Research downscaled climate projections for South Australia
  url: https://data.sa.gov.au/data/dataset/goyder-institute-for-water-research-downscaled-climate-projections-for-south-australia
- agency: SA Country Fire Service
  name: South Australian Bushfire Safer Settlements
  url: https://data.sa.gov.au/data/dataset/38361477-6054-4bb4-abde-39f2b3982254
event: adelaide
hackerspace_url: https://2016.hackerspace.govhack.org/node/946
jurisdiction: sa
prizes:
- australia-creative-humanities-hack
- australia-data-intelligence-hack
- australia-fresh-data-hack-(api’s-and-data-services)
- australia-inspired-by-research-hack
- australia-community-resilience-hack
- australia-machine-learning-hack
- australia-storytelling-hack
- sa-adelaide---best-in-location
- sa-protecting-our-environment
project_title: Will I Burn?
project_url: http://www.will-i-burn.xyz
repo:
  name: GitHub repository
  type: github
  url: https://github.com/alexg-hacks/will-i-burn
team_name: Red Hot
video:
  alt_url: https://govhack-storage.s3-ap-southeast-2.amazonaws.com/2016/Team%EF%80%A2%20Red%20Hot%20-%20Will%20I%20Burn%EF%80%A5.mov
  type: youtube
  url: https://www.youtube.com/watch?v=qwEP27blgDI
---

---
 
If you live in or take a (long) holiday in an area, what are your chances of being in a bushfire?
This hack uses past bushfire and backburning data combined with the fantastic Goyder Institute climate change prediction models to generate a prediction of overall fire risk for specific areas. 
Initial Findings...
So far we have looked at the fantastic bushfire and backburn history data put up by DEWNR that tells us some interesting things, such as - National forests seem to mostly burn out, but bushfires are stopped at the edges. We think this is due to a lack of important buildings/property, inaccessibility to firetrucks and the difficulty of creating fire breaks through a forest.- The risk of property damage in bigger regions (the outback) is less, so a larger outback fire has a human impact on a similar scale to a smaller one in a more built-up area. As a result, we've classed fires as 'major' based on the percentage of a region burnt, rather than the raw number of hectares.- There are lots of fires burnt in the large northern region of SA, where the APY lands are - there aren't listed as official DEWNR burns but we wondered whether they might be part of a recognised and intentional indigenous land management strategy- Using R, We (well, Tim) looked at using temperature as a correlation for the likelihood of bushfire events, but there doesn't appear to be a strong enough correlation to use this as a predictor (at least, not on its own). Other factors were wind speed, trans-evaporation, and vegetation density; unfortunately, data on these weren't available. In some cases, this is because it doesn't exist.
As the data we have found and looked over stands, we have the following factors: - historical prediction based on # of fires previously- the size of past fires is known, so we are able to calculate what # of a region was burnt in any given month- BOM historical weather station data allows us to look for correlation between temperatures and bushfires- We are using the number of days over 35 and temperature projections as a factor in the R query analysis to incorporate the potential effects of climate change; a full analysis of the fantastic Goyder Institute climate model data would provide this (the user would be asked for a year instead). The correlation between average temperatures, very hot days, and bushfires isn't bulletproof-strong but it still exists.
This hack (especially with accurate climate projections) could be useful to: 
 - Individuals/businesses considering building property in a fire-affected region;  - Individuals/businesses considering staying in a regional area longer term (Is it worth renting in the bush or should I stay in a Safer Place/Town?) - Anyone interested in the bushfire history of a given area  
If we had lots more time...
- It would be great to look at the effect of winter rainfall on summer bushfire frequency and severity.
- It would make a LOT of sense if we are looking at chances of being caught in a bushfire in the *current* month, to check for current bushfires/burns in the area as well as checking for current fire danger warnings, strong wind or storm (lightning) warnings. 
- Potentially we could expand the input choices to look at data by quarter or fire season (1 Sept to 30 april) instead of per month
- Data on areas where known individuals who start fires (firebugs) live and work is not publicly available. Knowing that a large number of firebugs live in a particular area would be helpful but unlikely to happen. Potentially, analysis of where convictions for arson have been recorded could shed some light on this.
- We would love for this to be a national project, although we are constrained by time limitations and data available. DEWNR and the SA CFS have provided some fantastic long-term history data sets on burns and fires in SA, however, these don't seem to be matched nationally or in other states to allow data analysis on the same lines.  We are using relevant parts of some national BOM data sets (e.g. historical weather) to correlate with other data sets, however.
- We would like to be able to use smaller areas for the chance-of-being-in-a-bushfire predictions, particularly differentiating between different planning areas (town/residential, farming/agriculture, national park). We would also like to take into account the Safer Places database (we have the Safer Bushfire Places dataset loaded, it's a matter of time whether we can incorporate it this weekend).
The BOM obviously has some fantastic data which forms the basis of the pretty pictures on their climate models/projections pages. However, the raw data isn't freely available for analysis anywhere we could see.
Prize Categories we've applied for... 
Data Intelligence Hack - because the bushfire data and climate data both have lots of fascinating insights in them!
Creative Humanities Hack - by taking a lot of really complex data (weather, bushfires, maps) and combining them into simple terms (fire risk) we have made some very complex long-term weather and climate data accessible. 
Fresh Data Hack - the fresh data used in this project is the current real-time bushfires, warnings, and temperature displayed on the front page. It will use 'demo' data at this stage but the real data is available and here is how we plan to use it.
Inspired By Research hack - the results for each region have changed and how we use the various data sets has changed as we've seen the correlations and effects of each. The raw findings from looking at the data are listed above (see 'initial findings') as well as the data-mining queries learning about factors predicting bushfires by analysing the data using R predict functions.
Community Resilience Hack: our hack is all about helping communities understand the risks they face, both now and longer term, from bushfires. 
Machine Learning Hack: We used a single layer back-propagated neural network implemented in R to analyse the data. 
Protecting Our Environment - Climate change will have a very real impact on bushfires. We may not get to it this weekend, but it is our plan to have two projected bushfire risk results for any given query - one based on recent historical averages and one that takes into account climate change models
Adelaide Spirit Prize - because we've loved, loved, LOVED being part of GovHack this year! With a strong collaborative spirit, lots and lots of data analysis, insights and discussion, and a team of strangers working together, this has been a very fun and productive team to be part of. 
Adelaide: Best in Location - because we have created something educational, which uses lots of open data and makes the data interactive
Image Credits... 
Fire photo is Public Domain, from https://commons.wikimedia.org/w/index.php?curid=455182
Tree image is by Terpsichores - Own work, CC BY-SA 3.0, https://commons.wikimedia.org/w/index.php?curid=21012360