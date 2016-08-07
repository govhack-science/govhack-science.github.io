---
category: ''
datasets_used:
- agency: Australian Broadcasting Corporation
  name: ABC Local Online Photo Stories 2009-2014
  url: https://data.gov.au/dataset/abc-local-online-photo-stories-2009-2014
- agency: LINC Tasmania
  name: LINC Tasmania Digitised Archives
  url: https://data.gov.au/dataset/linc-tasmania-digitised-archives
- agency: Australian Broadcasting Corporation
  name: ABC News Gateway API
  url: http://portal.govhack.org/datasets/2016/australia/australian-broadcasting-corporation/abc-gateway-api.html
- agency: Australian Broadcasting Corporation
  name: Views of ABC News Digital Content (May 2016)
  url: http://portal.govhack.org/datasets/2016/australia/australian-broadcasting-corporation/views-of-abc-news-digital-content-(may-2016).html
- agency: NewsCorp
  name: News Corp NewsAPI
  url: http://www.newsapi.com.au/
- agency: National Portrait Gallery
  name: National Portrait Gallery (NPG) Portraits and People
  url: https://data.gov.au/dataset/portraits-and-people
- agency: CSIRO
  name: CSIRO Science Images
  url: http://www.scienceimage.csiro.au/
event: hobart
hackerspace_url: https://2016.hackerspace.govhack.org/node/781
image_url: https://2016.hackerspace.govhack.org/sites/default/files/field/image/SplashFourbyuathreewithaborder%20copy.png
jurisdiction: tas
prizes-entered:
- australia-abc-news-content
- australia-commerically-viable-hack
- australia-creative-humanities-hack
- australia-data-intelligence-hack
- australia-entrepreneurial-hack
- australia-fresh-data-hack-(api’s-and-data-services)
- australia-future-australia-hack
- australia-innovative-ideas-hack
- australia-inspired-by-research-hack
- australia-machine-learning-hack
- australia-storytelling-hack
- australia-no-boundaries-data-hack
- tas-best-data-visualisation
- tas-design-excellence
- tas-most-commercial-potential
- tas-most-disruptive-innovation
- tas-most-outstanding-tasmanian-benefit
project_title: Beat The Press
project_url: http://www.secretlab.com.au/govhack2016
repo:
  name: GitHub Repository
  type: github
  url: https://github.com/admiraldolphin/govhack2016
team_name: When Badgers Go Bad
video:
  type: youtube
  url: https://youtu.be/c6VViaprY0I
---

Beat the Press is a frenetic action game that challenges players to match news headlines, science data, descriptions of artwork, and other data descriptions to their corresponding images.
Players take control of colourful news broadcasters and their rocket-powered news desks, competing against each other to collect images from the level and throw them onto the correct headline or description in the news ticker. Various datasets are used, pairing descriptions and names to images.
"You remember that time when Lee Lin had the by-election and was just about to win when Tony Jones threw a sex scandal at her throwing her off course and ending the game on a tie?!"
Based on research into neural plasticity, Beat the Press uses data from the ABC news Gateway API, the National Portrait Gallery, CSIRO Science Images, ABC local news photo stories, the Linc Tasmania Digitised Archives, and the News Corps News API. We also use a machine learning generated fake headlines trained on a corpus of over 65,000 genuine headlines; these are included in the game as wildcards. 
The basic approach relies on the mnemonic technique of surrealist events, combining visuals, audio, and a self-directed narrative to better remember events and data. Research suggests that the human brain automatically associates strange moments with the memories, in this case news headlines, science imagery, art, and so on. We are hardwired to better remember these surrealist moments, and our brain remembers the connected fact far better than if you just tried to remember, or study a list of the information used. This style of memory training has far reaching benefits, beyond just allowing people to better remember the news and facts.
To get the data into the game, we wrote a intermediary gateway API in Go, which fetches the various data sources, standardises them, and outputs them via JSON for the game to consume. The game is written in C#, and is designed for any platform that supports game controllers. We prototyped it using a Mac. The game is set in a frenetic news desk environment where players are news anchors who need to match the story items to the headlines moving along the news ticker at the bottom. We created the music, sound effects, and all of the art work over the GovHack weekend, using a variety of tools including Procreate, Logic Studio, Photoshop, Unity 3D, Go, Swift, Python, Final Cut Pro, and spreadsheets.
The game is extensible to any dataset that contains a pairing of images and descriptions. We also include Lee Lin Chin.
For more information check out our website: http://www.secretlab.com.au/govhack2016