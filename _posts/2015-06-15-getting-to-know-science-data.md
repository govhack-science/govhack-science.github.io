---
layout: post
tags: ideas
title: Getting to know scientific data
---

A lot of the science datasets can feel a bit intimidating because they sometimes require a lot of specialist knowledge to interpret, and it can be difficult to know how to interrogate them correctly.

It's often a good idea to steer clear of the field that the data was originally collected for - the scientists have probably already covered this stuff.

You should think about how this information could be used in a field you're more familiar with, or with a dataset that you know more about - data mashups are definitely the way to go. And really, this is a hack so scientific rigour is not primarily what we're after (although telling us that your hack will reverse gravity won't really cut the mustard).

If you have still have questions about the details of a scientific dataset, or how to interpret it. your best bet is to ask around at the event - there will be data mentors or even other competitors who may be familiar with your selected data or something similar, even if they're not from CSIRO or GA. Otherwise try me on [Twitter](http://twitter.com/jesserobertson) and I might be able to help.

![A CSIRO scientist in the lab](http://www.scienceimage.csiro.au/images/cache/detail/976_0_BU5147.jpg)

### Geospatial data

A lot of scientific datasets (especially the geoscientific ones) involve a geospatial component. But try to think about doing more than just 'we plotted this data on a map' - is there a cool mashup with some other data that you can use to add value to your map? Can it be used as a gateway for some other dataset?

There's a really good introduction to geospatial data in the [GovHack hackers guide](http://govhack-toolkit.readthedocs.org/technical/geographic-data/) with a ton of hints and tips, but here's a few more from us:

- Geospatial data can be a bit tricky to get used to on the fly. One thing to keep in mind is whether you're dealing with a raster coverage (usually something like an array of numbers given at gridded pixel locations) or vector data (more like polygons, lines or individual points at arbitrary (x, y) locations, usually with some kind of metadata).
- Probably the easiest way to get started with a mash up (if you're not wanting to program heaps) is to load stuff into a GIS package. [QGIS](http://www.qgis.org/en/site/) is fantastic and well worth a look if you don't have a license for ArcGIS or MapInfo, and is able to slurp data directly from providers like Geoscience Australia.
- [**Natural Earth**](http://www.naturalearthdata.com/) is a fantastic resource for getting nicely curated vector geospatial data with decent metadata, available at 1:10 million (1 cm = 100 km), 1:50 million, and 1:110 million map scales. This data comes in shapefile format, but Mike Bostock (of protovis/d3 fame) has a good post on using this data with a bit of `ogr2ogr` munging to generate nice d3 maps: [http://bost.ocks.org/mike/map/](http://bost.ocks.org/mike/map/).
- On the topic of geojson, there are a bunch of really good libraries in most languages for dealing with geospatial data in that format - aside from the usual suspects in js (as well as Mike's tutorial above, see [here for a tutorial on choropleth mapping](http://blog.visual.ly/how-to-make-choropleth-maps-in-d3/), and any of the examples on the [d3 gallery](https://github.com/mbostock/d3/wiki/Gallery)), Python has libraries like [shapely](https://github.com/Toblerity/Shapely) for dealing with vector data, and [rasterio](https://github.com/mapbox/rasterio) for raster coverages.
- Another issue (which will be especially important for data mashups) will be having to deal with different projections etc. Make sure you have a good idea of what libraries you're going to use for this - you don't want to be debugging a hand-rolled transform function in the middle of the hack.
- If you are producing javascript maps and want to make it look a bit more unique then the usual google maps/openstreetmap styling take a look at [Mapbox](https://www.mapbox.com/), which allows you to design and serve up really pretty map styles over the web. Most decent mapping libraries will let you slurp in tiles from Mapbox.
- [Cesium](http://cesiumjs.org/) is another really cool project for WebGL-accelerated 3D globes with good support for visualising geospatial data. In fact, that's what [the National Map](http://nationalmap.research.nicta.com.au/) uses.
