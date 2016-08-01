---
datasets_used:
- agency: Main Roads, Western Australia
  name: Crash 2011 to 2015 MRWA
  url: http://catalogue.beta.data.wa.gov.au/dataset/crash-2011-to-2015-mrwa
- agency: Main Roads, Western Australia
  name: Incidents and Events MRWA
  url: http://catalogue.beta.data.wa.gov.au/dataset/incidents-and-events-mrwa
- agency: Main Roads, Western Australia
  name: Network Operations Traffic Data MRWA
  url: http://catalogue.beta.data.wa.gov.au/dataset/network-operations-traffic-data-mrwa
- agency: Insurance Commission of Western Australia
  name: ICWA Motor Injury Insurance Accident Data
  url: http://catalogue.beta.data.wa.gov.au/dataset/icwa-motor-injury-insurance-accident-data
- agency: Coan Harvey, Department of Treasury, Western Australia and Western Australian Police
  name: 2015-286 KPMG Police Data
  url: ''
event: perth
hackerspace_url: https://2016.hackerspace.govhack.org/node/1306
jurisdiction: wa
prizes:
- australia-data-intelligence-hack
- australia-fresh-data-hack-(api’s-and-data-services)
- australia-community-resilience-hack
- australia-machine-learning-hack
- australia-new-infrastructure
- australia-transport-data
- wa-big-data-and-analytics-prize
- wa-the-keep-western-australia-moving-prize
- wa-western-australian-entrepeneurial-prize
- wa-western-australian-innovation-prize
- wa-western-australian-solution-prize
project_title: The Transac Initiative
project_url: http://transac.xyz/
repo:
  name: All the GitHub Evidence
  type: github
  url: https://github.com/CrashTestGovhack
team_name: Crash Test Dummies
video:
  type: youtube
  url: https://youtu.be/t5FBPPdD_K4
---

Big data analysis has often been encouraged at GovHack events over the past few years, but finding the data and sanitizing in preparation for a hack typically consumes the majority of the weekend and leaves little time for creating a finalized product, hack or prototype. This makes us sad, especially as university students who often go through this mindless and unproductive leg work as part of the typical research process. We love the open data policy the Government is championing, but like wingy kids, we're always complaining for more. Yeh, sorry.
 
The Government has a lot of data, but it doesn't always know where it all is..
~ Opening Keynote of GovHack WA 2016
 
This comment stood out to us and has driven the core component of our hack, a unified API and data portal that combines traffic data from numerous sources – including MRWA, ICWA, PTA of WA and SLIP. We also met with some kind gentlemen from the Insurance Commission who represent the resulting challenges faced from not having all traffic and traffic incident data available in a unified way. The ICWA struggles to process insurance claims due to inefficient access to inter-department data and claimant user experience suffers as a result. These are already vulnerable people who are injured, some who are not certain if they will be able to maintain their livelihood or not. These people deserve better. They deserve a Government that has the tools to create an experience that will comfort and support them the entire way in a time of need. And importantly, this is something we can create together.
 
The Core of Our Hack  (The Transac Initiative Homepage)
A data portal. How original... Boo! Yeh okay, it's not sexy. But it is vital to many Government departments and could be vital to encouraging Australian Innovation. Imagine one portal, for all traffic data. No, not just the flow of traffic, no, Main Roads has that, not just injuries, the Health Department has that, but unified access to unified traffic data from many sources.  
 
The Humanitiy of Our Hack  (New Crash Report Website Concept)
Why is this important? Two members of our team, Alex & Ben, were in a single vehicle accident on Mitchell Freeway around this time last year. The driver thought they saw something about to cross the Freeway that wasn't there, but applied the brakes and lost control due to wet roads. Their car was totalled after plummeting through light poles and having one of the large poles come crashing down on top of their car. The crash wreaked havoc on their lives, which was compounded by the uncertain feelings that came whilst filling out the online crash report.
The API that powers the data portal above could be used to power a revamped crashreport.com.au online form (see the concept link above). We have designed the user experience in a way that would allow respondents to know that they are in the right place online to submit their details, and would help them feel secure about the way their data is being handled. If the preliminary details entered by the respondent correlated with information stored by the Government (navigate to the second page of the concept form), and allowed the system to pre-fill the form and the user to verify the existing data (third page concept), then there would be an increase in the accountability of all parties and the end user would feel safer.  This is just one example of how this API can be used to help various government processes and affect real lives.
 
The Business End of Our Hack  (A Sample JSON API Request of an Incident)
Our API, which is written in Python but could be rewritten in any language, powers the Transac Homepage and can incorporate various sources of data to drastically decrease the incidences of fraudulence, duplication and errors. Wider assess to inter-department Government data can no doubt help the community, especially the vulnerable involved in motor vehicle insurance claims. Arguably though, of equal importance is the ability to use this data to drive business decisions and to help drive data backed policy decisions, such as the expansion of public infrastructure, financial cost benefit analysis that are able to easily take into account the Bigger Picture Data, and improve accessibility, efficiency and accountability.
 
Prize Categories
Community Resilience Hack: Natural disasters, sharks and flying is scary for lots of people, but in Australia, the chance for each individual to be involved in a motor vehicle accident is much higher. "You're more likely to die from a car accident than be bitten by a shark!" Where a natural disaster often affects a community who can turn to each other for support and assistance in rebuilding, motor vehicle accidents can leave individuals in life altering situations and often without the wider support of their community. This is why it is important that individuals affected by situations like this are made to feel safe, and as looked after as possible. The process often starts with the local Police and Insurance Commissions. We have reconsidered the user experience of the reporting website in WA with a focus on reassuring claimants that their details are available to the relevant authorities already, and they are being looked after by using our data portal API.
Machine Learning Hack: One of the things we are most excited about by our hack is the opportunity it provides for data analysis and machine learning. The example we have demoed is the ability to tap into wider data to drive fraud detection algorithms for insurance claims. Equally exciting to being able to save the Government money (and our tax money?) is to be able to drive academic research using a unified API endpoint. It is reassuring to know you have all of the data at your fingertips and not worrying if you have missed anything vital.
Data Intelligence Hack: Unable to find all the data you need to justify whether you should build a new highway link or not? What about whether it is financially responsible to modify an intersection? What about analyzing the flow of traffic from airports to the city? And even walkways and cycle paths? This API can and should be developed further to enable large datasets to be analysed to drive government decisions. But that's not all, by making it public, innovative startups can capitalize on the data being made available. Uber for example could use the data to help ensure demands are met (to lower surge pricing opportunities). What else could clever Australians create with the data at their fingertips? We are keen to find out.
Fresh Data Hack: We had a weekend to load in existing data. Our dream is that the official portal will start with real time data that is stored in a way that is suitable for as many departments as possible, and allows the flexibility to be adapted for others as needed. As an example, we were able to tap into the Main Roads RSS feed to display the incidents they have available to them. One of the limitations we found was they had to be verified by police before they could notify patrons of WA Roads. Let's change this together and find a way to provide real time traffic data without affecting ongoing legal concerns?
Bounties and Team Prizes:
Transport Data: This hack has been developed to encourage the official development of a national data portal for traffic and transport related data. We hope the API will be made available for public access, with some private authenticated calls available for government departments.
New Infrastructure: We believe that this incredibly large collection of data, and the ability for the dataset to continue to grow in a sustainable and usable way, will allow for very smart infrastructure planning decisions to be made going forward.
Best Higher Education Team: Many of the team members are students from UWA who have joined GovHack after attending a few hackathon themed workshops run by a fellow student. The enthusiasm has been fantastic.
Various Local Prizes have been nominated and will be advocated for at the local judging event on Sunday afternoon and evening.
 
The Team and Our Gratitudes:
 
Ancil Thomas
Alexandra Black
Ben Jennings
Daniel Sheward
Jason Chao
Kimberly Larking
Shaun Leong
YiYang Gao
 
We would like to extend a special thanks to our team members Daniel and Kim who have used their industry experience and patience to help the entire team build a project we are very proud off.
Another HUGE shoutout goes to the mentors from Main Roads WA and Insurance Commision of Western Australia for their assistance in understanding their unique challenges and datasets.
Thanks to Amazon and the AWS mentors for both providing credit to power our hacks, and the technical assistance to implement it.
A final thanks to the kind participants and event organizers who took time out of their hack and duties running the event to help assist with a few technical problems we faced.