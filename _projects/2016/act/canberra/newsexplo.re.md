---
datasets_used:
- agency: Australian Broadcasting Corporation
  name: ABC Gateway API
  url: http://portal.govhack.org/datasets/2016/australia/australian-broadcasting-corporation/abc-gateway-api.html
- agency: National Library of Australia
  name: Trove
  url: http://trove.nla.gov.au/
- agency: IBM
  name: IBM Watson AlchemyLanguage
  url: http://www.alchemyapi.com/
event: canberra
hackerspace_url: https://2016.hackerspace.govhack.org/node/2446
jurisdiction: act
prizes:
- australia-abc-news-content
- australia-commerically-viable-hack
- australia-creative-humanities-hack
- australia-data-intelligence-hack
- australia-fresh-data-hack-(api’s-and-data-services)
- australia-innovative-ideas-hack
- australia-machine-learning-hack
- australia-storytelling-hack
- act-most-innovative-project-for-canberrans
project_title: newsexplo.re
project_url: https://newsexplo.re
repo:
  name: GitHub
  type: github
  url: https://github.com/tsujamin/govhack2016
team_name: News Junkies
video:
  type: youtube
  url: https://youtu.be/wd-blfJF4PQ
---

The world is complex and fast moving. When news is breaking, a single article isn't enough for the complete picture.
newsexplo.re gives you the full story. Using the resources of the Australian Broadcasting Corporation, combined with the National Library of Australia's Trove service and the IBM Watson platform, newsexplo.re links together related stories, topics and locations, allowing you to connect the dots.
newsexplo.re presents a graph/network view of relationships between news stories, locations, topics and people. Using the ABC's live gateway API, it can analyse any story published on the ABC News platform within minutes of publication, mapping related stories and categories from the ABC's taxonomy and adding further relationships using the Watson AlchemyLanguage service. The Trove API is used to further augment this with historical insights.
For example, during an election campaign, an interested citizen sees a story about a new government policy. By simply looking up the story in newsexplo.re, they can quickly find multiple articles that are relevant to the policy in question, discover historical information about similar proposals, see the relationships with the key actors involved, and develop a clearer understanding of the policy than if they relied on just a single story.
Our aim is for newsexplo.re to be a useful platform for interested readers to see the whole picture, not just a single headline, and to provide analysis capabilities that are useful to a wide variety of policy makers, citizen journalists, researchers and others. Future extensions include additional data sources (such as News Corp), and more advanced techniques to improve the quality of linkages.
We believe our proof of concept strongly demonstrates the usefulness and strong commercial viability of this idea. With its wide appeal, newsexplo.re could easily be delivered as an inexpensive subscription service targetting people not already served by existing, larger media monitoring companies. Commercial revenue would allow the service to license more content and use more advanced techniques to discover more insights from news and government data.
newsexplo.re is Free Software under the GNU Affero General Public License (v3 or higher), and is built on a Free Software stack powered by Python, Flask, nginx and PostgreSQL.