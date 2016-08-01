---
event: adelaide
hackerspace_url: https://2016.hackerspace.govhack.org/node/2431
jurisdiction: sa
prizes:
- australia-that-thing-we-all-need
- australia-commerically-viable-hack
- australia-creative-humanities-hack
- australia-data-intelligence-hack
- australia-entrepreneurial-hack
- australia-fresh-data-hack-(api’s-and-data-services)
- australia-innovative-ideas-hack
- australia-inspired-by-research-hack
- australia-community-resilience-hack
- sa-smart-lifestyles
- sa-supporting-sa-economy
project_title: Touch
project_url: http://mishraanoop6.wix.com/touchdoctorrole, http://mishraanoop6.wix.com/copy-of-touchalarm
repo:
  name: Touch
  type: github
  url: https://github.com/mishra123/Touch
team_name: Connect
video:
  type: youtube
  url: https://www.youtube.com/watch?v=T2S3_jd-tL0
---

Problem Statement:
Australian Bureau of Statistics reported the population of elderly people in Australia which is expected to be risen by 4 million in 40 years. However, the dataset about population who are needing assistance which shows that there is 5.5% population in SA. This is where the problem of bed sores starts. From 1993 to 2003, there was increase of 63.3% recorded worldwide. During the last decade, 56% people are affected by this. In Australia, 2,70,000 elderly people has suffered from pressure ulcers. The elders are particularly at risk – simply because they tend to suffer more with poor circulation and because they are less mobile.  
Studies and investigations has proved that the key to the pressure sore is the basic care and repositioning at right time and in right manner. Peter Walsh, from charity Action Against Medical Accidents says "In this day and age, no one should acquire a pressure sore in hospital - it demonstrates the lack of basic nursing care". David Kerry, one of the specialists in Medical negligence cases says “With proper attention and care, there pressure sores should not occur”. At the moment, we have no database to store the information which can be used to monitor the condition and severity of pressure sore. In addition to that, in the negligence cases, department doesn’t have any information to investigate. Therefore, we design the technological solution which will help nursing homes, hospitals, family members, and doctors to pay the required attention to the patient/elderly people/bedridden people. 
Solution:
Touch is a web based and mobile based solution to resolve the problem of pressure sores/bed sores especially for bedridden and elderly people. Touch will transform the way the Health Department deals with pressure sores with the help of “Enterprise Patient Administration System” (EPAS) Id. This will bring an advancement and pace in health system while maintaining the privacy and confidentiality of the individuals using different user roles for different stakeholders to access the mobile or web based system. These user roles will be set up by health department which means that the health department can alter the privileges on the user roles as required by the legislations and different act to comply with them.
Objectives:
-       Reforming the current procedures to deal with pressure ulcers.
-       Help family members, hospitals, and doctors to pay more attention without any delay.
-       Store the information on movements to be more attentive about the care our bedridden people get in the nursing homes.
-       Keep everyone informed about the condition of their loved ones because even though you are not suffering from pressure ulcer but you still suffer when you find them suffer with intolerable pain.
-       Send analytics to the stakeholders to notify the severity of the wound.
Touch is a platform which will record the patient's movement information using the sensors installed under the mattress. These sensors update the APIs deployed on IBM Softlayer based cloud platform with real time movement information of the patient. All the information on the cloud will be stored using EPAS Id as an identification of the patient and is made available to different stakeholders with their user roles. The system stored information in Sql database which has been deployed on IBM cloud based platform.
Different access levels:
Family Member will be able to access the real time information on when the patient was last moved, and the average time gap during that day. This information can then be compared with the doctor's prescribed gap between the movements to check the condition of the patient. They will also be able to extract the weekly movement data sheet which will detail the movement of every day. The app allows them to send the weekly reports on their email address to keep the record.
Doctor will be allowed to access the patient's data using EPAS Id. Using the platform, they will be allowed to view patient's medical history on different diseases related to pressure ulcers and immunity like blood infections, surgeries, kidney diseases, fits and faints etc. The security will limit the doctor to view only the past medical information of the patient based on the speciality of the doctor. Based on that information, doctors can add audio, video or text advises which will be sent to the respective nursing home/hospitals. Doctors are also allowed to upload any test reports related to the patient on the system so that it can be used as future references.
Nursing Home/Hospitals will also be able to access the similar information as doctors and additionally they will also be able to leave an audio, video, and text replies to the doctor.
Alarm role is designed to enable the nursing homes/hospitals to be regular with the repositioning on time. Based on the doctor’s prescriptions, they need to be reposition on time to save them from the tissue damage on the pressure areas. Nursing homes can save the alarms based on EPAS Id and duration, which will blow to notify the staff to reposition on time.
Internet of Things:
Touch uses IBM Bluemix Internet of Things (IoT) which will send reports and analytics on the patient’s condition based on the frequency desired by user. These can be setup as daily, weekly, monthly reports. However, the platform will automatically sent the reports to all the stakeholders when the condition of the pressure ulcers is too severe and the proper medical attention is not there. This consent will be collected from the user while signing up with touch.
Data Set Re-use
NATIONAL DATASET: Australian Bureau of statistics data
http://www.abs.gov.au/AUSSTATS/abs@.nsf/DetailsPage/4430.02012?OpenDocument
NATIONAL DATASET: Hospital Statistics
http://data.gov.au/dataset/australian-hospital-statistics-2012-13
EPAS dataset: SA Health
This dataset is not open dataset, but I have consulted with SA Health department where I got the structure and the legislations on using EPAS Id.
Technologies Used
App Development: iOS, Android and Windows programming
Front End: HTML5/JavaScript/CSS, jQuery Mobile, JSON/XML, Wix, Eclipse
Backend: REST Web Services using JAX-RS framework, Annotations,  
Cloud Platform: IBM Softlayer for app and database deployment, IBM Bluemix Internet of Things