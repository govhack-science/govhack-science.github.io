---
category: ''
datasets_used:
- agency: Govhack
  name: Hackerspace
  url: http://2016.hackerspace.govhack.org
event: canberra
hackerspace_url: https://2016.hackerspace.govhack.org/node/2316
image_url: https://2016.hackerspace.govhack.org/sites/default/files/field/image/logo-new.png
jurisdiction: act
prizes:
- australia-that-thing-we-all-need
- australia-fresh-data-hack-(api’s-and-data-services)
- act-best-data-wrangling
- act-best-in-act
- act-best-tertiary-hacker-team
project_title: Hackanation
project_url: http://hackanation.tk
repo:
  name: Github
  type: github
  url: https://github.com/andrew-m-h/govhack-webcrawl
team_name: Alpha Hawk Magnum
video:
  type: youtube
  url: https://youtu.be/byJl5SFDino
---

Hack A Nation: Govhack becomes the data
Overview
Our hack is a meta-hack of sorts, we have spend the weekend writing a web crawler to crawl the hackerspace and prize descriptions website, in order to gather data about the sorts of prize categories that teams are targeting.
Target Audience
We aim to help gov-hackers diversify and explore the various prize categories that go unclaimed each year. This is good for the hackers since they increace their odds of winning prizes, and good for data sponsors because they increase the takeup of their hard gathered data. 
The hope is that, when a team gets to 9pm Friday night, they will be able to access our website and look for prizes that are being overlooked by the large number of teams who declare their prize categories early. Over the weekend, the website will become a facinating insight into the govhack community and ongoing hacks. After the event, data mentors will be able to utilise our data, which is published in JSON format as well as the website, to analyse how to best advertise their data in future.
Method
Hackanation is centered around a django (python) web server, alongside a scrapy (python) web crawling application. These sit atop a mysql database that is updated every 5 minutes to give a real time picture of how teams are picking their prizes.  We collect a plethora of data, however due to the limited schedule, we were unable to fully realise it's potential, however the data is sitting in an easily accessable MySql database for future usage.
Collaborative Analysis
We are passionate about enabling open data, and have teamed up with the Dash project to assist their goal in reaching out to non-programmers. How have we done this? Each team provided their data and mentoring to the other in able to make the most each other's reasources (as seen at hackanation.tk). You can find their project here: -Dash-
Business Model
With collaboration from the govhack team, this website could become an invaluable reasource in future hacks, the data is useful both during and after the hack and can be used for a variety of purposes.
Data
Our data is available online in JSON form from out github or explore it online at hackanation.tk.