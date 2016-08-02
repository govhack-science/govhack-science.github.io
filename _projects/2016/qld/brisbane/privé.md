---
datasets_used:
- agency: Science, Information Technology and Innovation, Queensland Government
  name: Brisbane Hospital registers of deaths 1933 to 1963
  url: https://data.qld.gov.au/dataset/brisbane-hospital-registers-of-deaths-1933-to-1963/resource/aa0c1fd9-297a-44e1-b032-adc563d3b646
event: brisbane
hackerspace_url: https://2016.hackerspace.govhack.org/node/2001
jurisdiction: qld
prizes:
- australia-commerically-viable-hack
- australia-entrepreneurial-hack
- australia-hiding-wally
- australia-machine-learning-hack
- qld-best-innovative-use-of-data-sets
- qld-mentoring-the-best-of-queensland
- qld-best-brisbane-or-queensland-oriented-business-related-application
project_title: Privé
project_url: ''
repo:
  name: Privé
  type: github
  url: https://github.com/joegov/prive.git
team_name: Da Washing Machine
video:
  alt_url: https://govhack-storage.s3-ap-southeast-2.amazonaws.com/2016/Prive007.mp4
  type: unknown
  url: ''
---

____________________________________
Black Hat hackers using mash-ups and sophisticated algorithms are already using online social data to reconstruct accurate personal profiles and commit identity theft. The newly available Government data should not contribute to this activity. 
Securing data on the web is a global problem; our submission is to suggest processes that address some of the bigger challenges, in an effort to ensure such that unauthorized personal data cannot be accessed. 
____________________________________
Our Project Name is Privé
And we are the “Da Washing Machine“ Team
To start we would like to address a suggested database in the  “Where’s Wally” Competition. This links to Brisbane Hospital registers of deaths 1933 to 1963
https://data.qld.gov.au/dataset/brisbane-hospital-registers-of-deaths-1933-to-1963/resource/aa0c1fd9-297a-44e1-b032-adc563d3b646
With this we discover that Michael OBrien died at 107, however we probably only wish to verify that the oldest recorded death during that period was 107.
In that instance the data washing algorithm is very simple, names are unimportant; the first two columns should be deleted. Ordinal numbers would also need deletion if they referenced to another database. 
____________________________________
As online transactions and backend databases grow, they become a vector for illegal activities that may infringe Australia’s privacy laws.
____________________________________
Existing privacy legislation prevents participants at GovHack from accessing live data that might be subject to privacy restrictions. Consequently it’s not possible to resolve a real Data Wash problem, as our online data has already been obfuscated.
So let’s consider a real challenge…….
Australia is about to undergo a nationwide census which requires that online users reveal their full identity. Even though the government insists that this data will be ultimately stripped, it still exists in an unencrypted form before the verification/purge takes place.
To allay the concerns of privacy advocates, we propose the following for the census and online voting:
An online user would need to use three browser sessions:
Firstly they would logon to a portal where they would select a public and private key pair. A privacy advocate would notice that they could press the online control several times to ensure that the number was random.
The key would be a standard key pair with a seeded government checksum to confirm the issuing authority.
The online user would then load and fill in two online forms. 
The first form registers the voter for the Vote or Census (using a private key).
The second allows the voter to fill in the Vote or Census form (using a public key)
Managing the privacy of recording voting and census data is a global challenge; further work on these concepts could provide a global solution for this otherwise expensive manual process.   
____________________________________
EXTRA INFO:
To obfuscate data for later release online the following algorithms should be applied:
Data totals would have max and min levels such that exceptions would be grouped as “below-low” or “above-high”.
Data levels would be grouped so that similar totals would report as belonging to a range. 
The low/high levels will have a learn function (machine learning) so that public trends will be accommodated.
____________________________________