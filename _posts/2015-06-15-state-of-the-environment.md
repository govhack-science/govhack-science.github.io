---
layout: post
tags: ideas
title: Human impacts on Australian Biodiversity
photo_url: http://www.scienceimage.csiro.au/images/cache/detail/976_0_JM3856.jpg
---

How does the human world impact Australia's natural biodiversity? Do our protected areas actually protect our threatened species? How can we visualize this? A State of the Environment Dynamic Dashboard could mash up human impace data (eg Australian Bureau of Statistics population data, SLIP roads and buildings) and vulnerable species data from the Atlas of Living Australia. ([Here's an example](http://www.buzzfeed.com/peteraldhous/these-maps-reveal-how-the-us-is-failing-to-protect-its-wildl) that suggests American protcted areas aren't located where they're needed).

A hack could include information on protected areas vs vunerable specied distributions, or other representations of ALA occurrence data – e.g. changes in species conversation status; adjusted representations of presence-only occurrence data weighted for likely biases in observer effort e.g. proximity to roads, population centres.

![Australian King Parrot](http://www.scienceimage.csiro.au/images/cache/detail/976_0_JM3856.jpg)

**Datasets and tools**

The Atlas of Living Australia contains a massive amount ([nearly 56 million records](http://dashboard.ala.org.au/)) of biodiversity data collated by [Australian scientific communities](http://www.ala.org.au/about-the-atlas/atlas-background/atlas-partners/partner-profiles/) and [citizen scientists](http://www.ala.org.au/get-involved/citizen-science/). You can use the ALA APIs to pull live data from their portal and serve it up for your analysis.

The [AdaptNRM project](http://adaptnrm.csiro.au/biodiversity-impacts/key-measures-of-ecological-change/disappearing-environments/) has a bunch of info on climate modelling and species habitats and how these are calculated. Georeferenced datasets from this modelling are available through the [CSIRO Data Access Portal here](http://dx.doi.org/10.4225/08/53FE5401D3CC8). 

ABS and SLIP data could be used to assess human impact, including proximity to roads, and development applications. When it comes to tools, anything goes really! Geospatial analysis would be crucial for this project though, so the info on that in the [hackers pack might be useful](http://govhack-toolkit.readthedocs.org/technical/geographic-data/).