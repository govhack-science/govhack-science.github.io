---
category: ''
datasets_used:
- agency: IP Australia
  name: Intellectual Property Government Open Data 2016
  url: https://data.gov.au/dataset/intellectual-property-government-open-data-2016
event: melbourne
hackerspace_url: https://2016.hackerspace.govhack.org/node/2536
image_url: https://2016.hackerspace.govhack.org/sites/default/files/field/image/89f1f5d6-7bb7-4d05-b50e-215a76157b89.png
jurisdiction: vic
prizes:
- australia-data-intelligence-hack
- australia-entrepreneurial-hack
- australia-machine-learning-hack
- australia-ip-rights
project_title: IPGODMODE
project_url: ''
repo:
  name: BitBucket Code &amp; Asset Repository
  type: bitbucket
  url: https://bitbucket.org/avinium/ipgodmode
team_name: Team Avinium
video:
  type: youtube
  url: https://www.youtube.com/watch?v=5kh1LDHTC_s&feature=youtu.be
---

IPGODMODE
IP Australia (IPA) is the Commonwealth authority for intellectual property rights in Australia. IPA maintains a comprehensive, highly detailed database - appropriately named IPGOD - with over 100 years of data on patents, trade marks, designs and plant breeder's rights.
For GovHack 2016, we used this dataset to create "IPGODMODE", a software package to analyse and visualize IPGOD patent data. 
IPGODMODE uses machine learning analytics to estimate, for any pending patent application, when a decision on that application will be made.
IPGODMODE also lets an applicant/agent view their patent portfolio in 3D/virtual reality as a "spider web" of nodes and connections.
Machine learning
With its incredibly granular level of detail, the IPGOD dataset is a perfect candidate for making predictions with machine learning.
What is Machine Learning?
Fundamentally, "machine learning" lets us dive into big datasets to find trends and make predictions.
In basic terms, we convert a set of "known" data into numbers, use computers to find the correlations and statistics between those numbers, and generate a model that can be used to make predictions on a future set of "unknown" data.
Why would we use it?
With the right data, machine learning can be an incredibly powerful tool. Organizations like IP Australia can speed up patent assessment and decision making, optimize resource allocation and preempt disputes. In addition to improving overall customer satisfaction, this also boosts IP Australia as the preferred international destination for patent registration.
What can it do?
As a small demonstration of what is possible with machine learning, we ran a linear regression analysis over the historical patent metadata in IPGOD.
The objective is to give applicants/agents an estimate of the length of time remaining until a decision is made on a particular unresolved patent.
When an applicant or agent selects a patent in IPGODMODE that has not yet been determined, IPGODMODE provides an estimate of the number of weeks remaining until a decision is made. The estimate was made using certain characteristics (or "features") of all patent applications approved after 2000 (category, class, group, country, and so on). 
Given time constraints, we chose these features if we felt they were prima facie relevant to the length required for a patent decision to be made. We made no attempt to analyse the significance of correlations with these features (or whether other features would provide better correlations). No analysis of coefficient of determination/residuals was made.
In addition, the year 2000 was chosen as the start year as it was assumed that post-2000 patent examinations would be more representative of current-day practices than pre-2000.
In other words, these estimates are for demonstration purposes only and should not be considered accurate. However, with realistic time periods and resources, we are confident that a more accurate model could be developed.
The regression was modelled using the following features:
ipgod101.AUSTRALIAN_APPL_NO
ipgod101.APPLICATION_DATE
ipgod101.COUNTRY
ipgod104.SECTION_CODE
ipgod104.CLASS_CODE
ipgod104.SUBCLASS_CODE
ipgod104.MAIN_GROUP_CODE
ipgod104.SUBGROUP_CODE
ipgod107.PATENT_TYPE
ipgod107.PCT_APPLICATION_IND
ipgod107.EXAM_REQUEST_DATE
ipgod107.EXAM_REQUEST_FILING_DATE
ipgod107.DEFERMENT_REQUEST_DATE
ipgod107.FIRST_REPORT_ISSUE_DATE
ipgod107.EARLIEST_PRIORITY_DATE
ipgod107.ACCEPTANCE_PUBLISHED_DATE
ipgod107.EFFECTIVE_PATENT_DATE
3D/Virtual Reality
Machine learning provides countless opportunities for the public and private sectors to improve service delivery. 
However, raw data is only one side of the equation. Data still needs to be transformed and presented in a simple, friendly way. 
IPGOD metata contained an enormous number of hidden connections - between patent holders, patent classifications, agents, geography, and many others.
Presenting these in traditional 2D/tabular format can be difficult to interpret for those unfamiliar with the system or database being used.
3D virtual reality, on the other hand, is a much more intuitive experience requiring practically no learning curve. We therefore chose to implement a prototype interface for using IPGODMODE with virtual reality headsets like the Oculus Rift or Samsung GearVR. The interface could also be accessed through a web browser for those without the specific hardware.
The interface allows lets patent applicants (IPGOD x02 tables) or agents (IPGOD x06 tables) to visualize view all current and past patent applications in their portfolio. The user can navigate this information as a 3D "mind-map" of interconnected nodes, each expanding to represent a particular IPC hierarchy, patent applicant, or patent application.
Combined with the machine learning predictions, IPGODMODE gives users fast, easy access to the information they need. 
Miscellaneous
We started using Australian Patent Office decisions scraped from AUSTLII to analyze which patents were more likely to end up before the APO. However, we decided early that we were unlikely to complete this before the deadline. The Clojure scraper and tf-idf code are still available in the repository under analysis\src\clojure\com\avinium\govhack
Logo created at http://www.freelogodesign.org/
Special thanks to Alica Daly, Emma Francis and Matthew Johnson from IP Australia for their mentoring during GovHack 2016.
For those interested in learning more, Avinium is our Melbourne big data and machine learning company. Check us out or hit us up on Twitter: @NickFisherAU https://au.linkedin.com/in/nifisher or LinkedIn https://au.linkedin.com/in/anthony-brcan-66990054