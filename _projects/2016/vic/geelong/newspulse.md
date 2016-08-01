---
datasets_used:
- agency: Australian Broadcasting Corporation
  name: Views of ABC News Digital Content (May 2016)
  url: https://data.gov.au/dataset/abc-news-may-2016
- agency: Australian Broadcasting Corporation
  name: ABC Gateway API
  url: https://content-api-govhack.abc-prod.net.au/v1/6946348
event: geelong
hackerspace_url: https://2016.hackerspace.govhack.org/node/806
jurisdiction: vic
prizes:
- australia-abc-news-content
- australia-creative-humanities-hack
- australia-data-intelligence-hack
- australia-fresh-data-hack-(api’s-and-data-services)
- australia-storytelling-hack
project_title: NewsPulse
project_url: http://govhack.nextstudio.com.au/
repo:
  name: GitHub Source Code
  type: github
  url: https://github.com/newspulse/abc
team_name: Settlers of Cremorne
video:
  type: unknown
  url: http://govhack.nextstudio.com.au/govhack-submission.mov
---

This is the Settlers of Cremorne presentation of their entry for GovHack 2016.  Our hack is called NewsPulse and our entry is from GovHack Geelong.
The Settlers of Cremorne is made up of 6 team members:
James Macpherson – who is the Technical Lead of startup company SalesPreso.  James is a JavaScript expert, and has been coding web applications for over 15 years.  James has a degree in Bachelor of Science with a major of computer science. 
Liz Honing - Liz joined SalesPreso 2 years ago after graduating from an Information Technology degree at Monash.  Liz is a frontend/client side developer and works predominantly in JavaScript and some PHP.
Ben Graham.  Ben is a programmer at Sales Preso, and has been coding for 15 years and is a python specialist with a love for data structures.  Ben also has degree in Robotics from Swinburne.  Liz joined SalesPreso 2 years ago after graduating from an Information Technology degree at Monash. 
Lauren Rui (Loz) is a creative technologist from SalesPreso.  She has a passion for design and animation, and has been creating beautiful frontend web design for over 10 years and has a Bachelor of Information Technology with a major in Multimedia.
David Louis (Smouie) has been a software engineer for 10 years with a mathematics degree from Melbourne.  He works for a small medical software company.  He also has a passion for data structures and complex problems.
Amanda Ward is a Masters of Data Science student at Monash, but has 15 years experience as a Business Analyst/Consultant in the telecommunications space.  She has an undergraduate degree in Environmental Science, and a graduate certificate in Technical Communication.
​​​​​​​Our Idea
The idea of NewsPulse spawned from several discussions over our team slack during the week.  Amanda used to work for Telstra, and a few weeks ago, she actually found out about a National NBN/Broadband Network Outage from Social Media before the outage information hit Telstra's call centres, technical teams or the newspapers.  We were wondering how often this happens with other news events.  Is Social Media the new “Mass Reporter”?   Is traditional print media and digital news potentially going to be replaced?  How can we link Social Media, News Stories and other information to provide people with an educated and fully formed story?
What does the hack do
Our hack shows a fun and innovative data visualization demonstrating ABC News Data over location and time.  This is just a starting point – we believe that the power of representing the data in this way and connecting the news to other open data sources is the way of reporting in the future.
What data sets did we use
Before we get onto the demonstration we will just run you through the boring stuff. 
Datasets - We used the data sources provided from the ABC for GovHack, including both the May 2016 hit data records and the content API.  We wrangled the data using Python, and then converted into a JSON file.  The hits per day from all technology platforms (web and mobile based) were combined into one data set.  Then the hit data was combined with the content, by calling the content API.
The articles were then rendered onto a map of Australia, using OpenGL.   Each article was represented using Google Maps and latitude and longitude of the news story.  Hits were represented an hourly breakdown over time by the magnitude of the pulse rendered onto the screen. 
The Front end application – is scripted using JavaScript, React and Cerebral.  We are also using amCharts for the charting.
The application is hosted on Amazon Web Services.
Missing features:
We spent some time trying to get Twitter to work, but quickly discovered that the May data from Twitter is not included in their API.  Our next release would look at getting realtime feeds from Twitter and combining it with realtime feeds from the ABC API.
We have included the a mockup article that shows how we would connect it to data sources about the local government area where the news article was published, plus showing information from Wikipedia about newspaper keywords.
Other enhancements will include a news ticker which passes a header across the top of the map with the biggest news articles at the time and connections to other social media sources such as Facebook, Reddit and LinkedIn.
The Benefit of our Hack
We are hoping that NewsPulse will bring a fresh look at the news, and allow students and researchers to easily link information from the news, with social media and with other open data sets.  Thank you for watching, and we hope you enjoyed the demonstration of NewsPulse!