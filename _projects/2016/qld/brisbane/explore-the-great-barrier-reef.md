---
datasets_used:
- agency: National Parks, Sport and Racing
  name: Great Barrier Reef coast marine park zoning
  url: https://data.qld.gov.au/dataset/great-barrier-reef-coast-marine-park-zoning
- agency: National Parks, Sport and Racing
  name: Geographic features - Queensland series
  url: https://data.qld.gov.au/dataset/geographic-features-queensland-series
- agency: National Parks, Sport and Racing
  name: Marine islands - Queensland
  url: https://data.qld.gov.au/dataset/marine-islands-queensland
event: brisbane
hackerspace_url: https://2016.hackerspace.govhack.org/node/1981
image_url: https://2016.hackerspace.govhack.org/sites/default/files/field/image/logo_5.png
jurisdiction: qld
prizes:
- australia-innovative-ideas-hack
- australia-location-data
- qld-best-innovative-use-of-data-sets
- qld-create-a-cutting-edge-concept---the-science-sandpit!
- qld-educate-us!
- qld-mentoring-the-best-of-queensland
- qld-best-visualisation-of-data
- qld-supporting-the-best-of-brisbane
project_title: Explore the Great Barrier Reef
project_url: http://greatbarrierreef.io/
repo:
  name: GitHub
  type: github
  url: https://github.com/scottdejonge/great-barrier-reef/tree/gh-pages
team_name: Bigfish
video:
  type: youtube
  url: https://www.youtube.com/watch?v=16aYr5jRjdc
---

About Explore the Great Barrier Reef
The Great Barrier Reef is the largest living ecosystem on Earth comprised of 2,900 unique reefs and 600 continental islands with 1,625 species of fish – 10% of the world’s fish species. Explore the Great Barrier Reef is an interactive education tool to better understand the scale and diversity of this natural wonder.
Explore the Reef
Learn the scale of the Great Barrier Reef by navigating through the 2,300km-long ecosystem, thousands of reefs, and hundreds of islands.
Dive In
Get up close to the reef structures that make up the Great Barrier Reef through virtual dives, keep an eye out for unique coral structures and sea life up close.
Reefs
Discover the 2,900 unique individual reef structures spread across the Great Barrier Reef that together make up the Great Barrier Reef.
Islands
The Great Barrier Reef includes over 600 continental islands, see the difference in size, location, and geology between them.
Marine Park Zoning
See how the Great Barrier Reef is being preserved by marine park zoning, protecting waters along the Great Barrier Reef coast.
Data Story
Explore the Great Barrier Reef uses geolocation datasets from the Queensland Government, mainly displaying KML onto Google Maps. During the process of getting the KML to display correctly it was clear that the size of the KML data would pose a problem.
To overcome issues with KML display and rendering, data was stripped of excess CDATA tags and empty XML markup, then the KML files were parsed into Google's Fusion Tables for map visualisation checks removing excess tabular data not required for the display on the map.
After cleaning the XML of any unnecessary markup, the KML was exported from Fusion Tables, reducing file size by top to 20%.
Larger KML datasets such as Island data was chunked into smaller KML files selecting fragments of Island data by alphabetical chunks (e.g. A-L, L-Q, Q-Z).
The purpose of displaying the KML data into a Google Maps interface is to inform the public to location of significance within the reef, including larger reef structures, main islands, and marine park zone boundaries. This highlights the scale and diversity of reef and islands as well as illustrates the main shipping travel routes through the reef into main ports such as Townsville.