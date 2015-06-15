# Some other useful hints

### Science data

A lot of the sciency datasets can feel a bit intimidating because they sometimes require a lot of specialist knowledge to interpret, and it can be difficult to know how to interrogate them correctly. 

My advice would be to steer clear of the field that the data was originally collected for - the scientists have probably already covered this stuff. Instead, think about how this information could be used in a field you know more about - data mashups are definitely the way to go. And really, this is a hack so scientific rigour is not what we're after. :)

If you have requests about the details of a scientific dataset or how to interpret it then ping me a message and I might be able to put you in touch with the scientists that collected it. 

### Geospatial data

Geospatial data can be a bit tricky to get used to on the fly. One thing to keep in mind is whether you're dealing with a raster coverage (usually something like an array of numbers given at gridded pixel locations) or vector data (more like polygons, lines or individual points at arbitrary (x, y) locations, usually with some kind of metadata). 

Probably the easiest way to get started with a mash up (if you're not wanting to program heaps) is to load stuff into a GIS package. [QGIS](http://www.qgis.org/en/site/) is fantastic and well worth a look if you don't have a license for ArcGIS or MapInfo, and is able to slurp data directly from providers like Geoscience Australia.

- [**Natural Eath**](http://www.naturalearthdata.com/) is a fantastic resource for getting nicely curated vector geospatial data with decent metadata, available at 1:10 million (1 cm = 100 km), 1:50 million, and 1:110 million map scales. This data comes in shapefile format, but Mike Bostock (of protovis/d3 fame) has a good post on using this data with a bit of `ogr2ogr` munging to generate nice d3 maps: [http://bost.ocks.org/mike/map/](http://bost.ocks.org/mike/map/).

- On the topic of geojson, there are a bunch of really good libraries in most languages for dealing with geospatial data in that format - aside from the usual suspects in js (as well as Mike's tutorial above, see [here for a tutorial on choropleth mapping](http://blog.visual.ly/how-to-make-choropleth-maps-in-d3/), and any of the examples on the [d3 gallery](https://github.com/mbostock/d3/wiki/Gallery)), Python has libraries like [shapely](https://github.com/Toblerity/Shapely) for dealing with vector data, and [rasterio](https://github.com/mapbox/rasterio) for raster coverages.

- Another issue (which will be especially important for data mashups) will be having to deal with different projections etc. Make sure you have a good idea of what libraries you're going to use for this - you don't want to be debugging a hand-rolled transform function in the middle of the hack.

- Try to think about doing more than just 'we plotted this data on a map' - is there a cool mashup with some other data that you can use to add value to your map? Can it be used as a gateway for some other dataset? 

- If you are producing javascript maps and want to make it look a bit more unique then the usual google maps/openstreetmap styling take a look at [Mapbox](https://www.mapbox.com/), which allows you to design and serve up really pretty map styles over the web. Most decent mapping libraries will let you slurp in tiles from Mapbox. [Cesium](http://cesiumjs.org/) is another really cool project for WebGL-accelerated 3D globes with good support for visualising geospatial data.