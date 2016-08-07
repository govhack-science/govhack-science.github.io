---
category: ''
datasets_used:
- agency: IP Australia
  name: Intellectual Property Government Open Data 2016
  url: http://portal.govhack.org/datasets.html#ip-australia
- agency: Department of Industry Innovation and Science
  name: SA3 Region Innovation Data 2009-15
  url: http://portal.govhack.org/sponsors/department-of-industry-innovation-and-science.html
- agency: Global Innovation Index
  name: Global Innovation Index 2015
  url: https://www.globalinnovationindex.org/
- agency: Universities Australia
  name: 'Universities Australia: University Profiles'
  url: https://www.universitiesaustralia.edu.au/australias-universities/university-profiles#.V52AfaLbR26
event: sydney
hackerspace_url: https://2016.hackerspace.govhack.org/node/1761
jurisdiction: nsw
prizes:
- australia-creative-humanities-hack
- australia-data-intelligence-hack
- australia-fresh-data-hack-(api’s-and-data-services)
- australia-future-australia-hack
- australia-innovative-ideas-hack
- australia-inspired-by-research-hack
- australia-storytelling-hack
- australia-ip-rights
- australia-location-data
- australia-new-infrastructure
- australia-no-boundaries-data-hack
- australia-smarter-data
- nsw-acceleration-award-govhack-nsw
- nsw-smart-cities-&-collaborative-economy
- nsw-vibrant-sydney-night-time-economy
- nsw-most-fun-and-creative-use-of-data
project_title: Mapping Innovation - from Local to Global in Time and Space
project_url: http://tomvalorsa.github.io/
repo:
  name: Mapping Innovation
  type: github
  url: https://github.com/tomvalorsa/govhack2016
team_name: Gov, Sweat and Tears
video:
  alt_url: https://govhack-storage.s3-ap-southeast-2.amazonaws.com/2016/GovHack_360p.mp4
  type: vimeo
  url: https://vimeo.com/176907534
---

The printing press, the pencil, the flush toilet, the battery--these are all great ideas. But where do they come from? What kind of environment breeds them? What sparks the flash of brilliance? How do we generate the breakthrough technologies that push forward our lives, our society, our culture? 
                                                                                                                                  - Steven Johnson, Where Good Ideas Come From
Innovation is a key measure of a country's success and one that is of key importance to Australia in our current climate. In 2015, Australia was ranked number 17 in the Global Innovation Index with a score of 55.2 for 2015. Australia has maintained its 17th position from the Index in 2014 and increased two ranks from 2013 where Australia was ranked 19.
This project allows the user to journey through the innovation datasets available to Govhack and explore the trademarks, patents and design applications that have been submitted.  
This tool will take you on a journey from the national level, where we explore the country and the innovation hubs as they have emerged through time, and then stepping into the state level datasets and exploring the spatial positioning of these innovations over time Finally, we step down further into an individual scale where we have developed Australian word cloud mapping that highlights the key innovations as they occurred throughout each decade.
At a National Scale:
Australia has been ranked number 17 in the Global Innovation Index with a score of 55.2 for 2015. Australia has maintained its 17th position from the Index in 2014 and increased two ranks for 2013 where we were ranked 19.
The Global Innovation Index is a culmination of various aspects of the economy including property, human capital, infrastructure, market sophistication, business sophistication, knowledge and technology outputs and creative outputs. Australia excels at a number of these sub-indices and our key strengths include:• Regulatory quality• Ease of starting a business• School life expectancy• Tertiary enroelment• QS university ranking• Overall Infrastructure• Information and Communications technologies• Environmental Performance• Ease of getting credit• Intensity of local competition• Global entertainment and media outputs• Printing and publishing outputs• Online creativityTo view how Australia ranked in each category- the data can be viewed here:
https://www.globalinnovationindex.org/analysis-economy
This showcases 100 years of innovation using Patent, Design and Trademark data across Australia. On a global scale, you can see Australia emerging with famous ideas such as the Hills Hoist, wifi, Cochlear implants. These ideas are joined by hundreds of thousands on other IP applications. As you watch this application, you can see the Innovation market explode throughout Australia, clearly identifying the city areas as the key place for the Innovative Economy.
We have also geocoded the list of Australian Universities as the correlation between Universities and innovation is a key relationship that has been highlighted.
In this data, trademark data did not have a exact spatial location so the postcode field was used to geocode these postcodes and determine a latitude and longitude for each point. To create the actual variance across the suburb that would occur in the real environment, a variance calculation was used to adjust the spatial location within the suburb to be able to physically see some of the hotspots. Many joins had to be made to relate each of the IP data set, and millions of calculations using our toolkit below. 
Datasets used:
Intellectual Property Government Open Data 2016
Global Innovation Index 2015
Universities Australia: University Profiles
At a State Scale:
This map allows you to explore the datasets on a state level for Patents, Designs and Trademarks. This map plays through time and shows the innovative ideas as they emerge. 
The Patent and Design datasets are shown as points on the map, whilst due to the huge number of trademarks being registered every year, these are shown as a chloropleth map in the background. This was a conscience decision to highlight the patents and design applications to show their location across NSW.
Datasets used:
Intellectual Property Government Open Data 2016
SA3 Region Innovation Data 2009-15
On a Projects Scale:
This data set lets you explore the Trademark, Patent and Design database key words, as mentioned in the application description. As you step through time from the 1990s for the trademark data, these word clouds highlight the most common elements of innovation throughout that decade right up to 2015 datasets.
The trademark data sets span over 100 years with the first application for trademark within this dataset being from 1906.
The design datasets span over 50 years, ranging from 1972 through to 2015.
The Patent dataset only spans for 2 decades, with the first data available to download being from 2003.
Method:
This project started by exploring the IP Australia datasets where we explored the trademark, patent and design applications that have been created over the past 100 years. There was enormous amounts of data to explore so our first was to explore what it contain and how we could use it. 
Mapping this data quickly became a method that we could easily display the data and enable insights to be drawn. From here, we went to work sorting through the data and extracting the informative information. We divided our project into 3 scopes at this section and set to work creating the final product.
National Scale:
These datasets were cleaned and using D3 and Cartodb, worked on creating an informative and interesting map of Australian Innovative history.
In this data, trademark data did not have a exact spatial location so the postcode field was used to geocode these postcodes and determine a latitude and longitude for each point. To create the actual variance across the suburb that would occur in the real environment, a variance calculation was used to adjust the spatial location within the suburb to be able to physically see some of the hotspots.
State Scale:
The datasets we wanted to explore here were at an SA3 level, however we wanted to also overlay this with more fine grained project coordinates. This culminated in a D3 map and the data.
Project Scale:
This project wanted to explore the individual projects and extract meaningful analysis about the trends of projects. The Trademark and Design application descriptions were a great resource to extract all of the project titles and run a correlation. This involved processing of millions of individual words. 
Tools Used across the whole Project:
·         D3
·         Python
·         React
·         Processing and various libraries
·         FME
·         QGIS
·         Animoto
·         Topojson
·         Canopy and Jupyter
Open Datasets Used:
Intellectual Property Government Open Data 2016
The Intellectual Property Government Open Data (IPGOD) includes over 100 years of Intellectual Property (IP) rights administered by IP Australia comprising patents, trademarks, designs and plant breeder’s rights. The data is highly detailed, including information on each aspect of the application process from application through to granting of IP rights. We have published a paper to accompany IPGOD which describes the data and illustrates its use, as well as a technical paper on the firm matching. Links to these papers can be found in the Data Dictionary.
http://portal.govhack.org/datasets.html#ip-australia
 
SA3 Region Innovation Data 2009-15
This dataset reports on innovation activities (R&D expenditure, patent and trademark counts) and business creation (new businesses) across SA3 regions in Australia.
http://portal.govhack.org/sponsors/department-of-industry-innovation-and-science.html
 
Global Innovation Index 2015The Global Innovation Index (GII) aims to capture the multi-dimensional facets of innovation and provide the tools that can assist in tailoring policies to promote long-term output growth, improved productivity, and job growth. The GII helps to create an environment in which innovation factors are continually evaluated.
https://www.globalinnovationindex.org/
Universities Australia: University ProfilesUniversities Australia lists the number and location of all universities and the various campuses within Australia as part of the Australia University Profiles 2016.
https://www.universitiesaustralia.edu.au/australias-universities/university-profiles#.V52AfaLbR26