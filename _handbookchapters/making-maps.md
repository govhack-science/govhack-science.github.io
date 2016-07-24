# In which we play at being cartographers

Righto, so you've got some data and need to provide a map for your users to view and interact with all of your lovely new data. Good news, you're spoilt for choice! (Are you detecting a theme here?)

Web mapping loosely falls into two categories:

1. JavaScript libraries that will let you build and customise the map interface (2D and/or 3D) to your heart's content, but require you to host the data, or plug it into other people's web mapping services.

2. Software as a Service platforms that provide simple and powerful GUIs for the creation of maps and support hosting of all sorts of different data formats.

And, of course, there's some grey area between the two - with many libraries supporting standard web mapping protocols like WMS, WMTS, and WFS - and with several of the SaaS platforms providing their own JavaScript client libraries to allow users to craft their own map interfaces.

These days a lot of the modern libraries and platforms have been optimisied to work well on mobile devices, and in some cases have separate libraries for developing native apps on iOS and Android.

Oh, and if you're completely new to web mapping check out [mapschool: a free introduction to geo](http://mapschool.io/) to get yourself up to speed on the concepts behing web mapping. The New York Public Library also has a great, and pretty exhaustive runthrough, of making your first web map: [From Paper Maps to the Web: A DIY Digital Maps Primer](http://www.nypl.org/blog/2015/01/05/web-maps-primer).

![A photograph of the Mappa Mundi, Hereford Cathedral](../imgs/mappa-mundi.jpg)

# MaaS (Maps as a Service)

At presents there are two main players in the SaaS mapping space: [CartoDB](http://cartodb.com/) and [MapBox](https://www.mapbox.com/).

They both do a great job of covering the basics of map building with quick and easy tools for uploading data and push-button interfaces that abstract away alot of the more complex spatial side of spatial data. They both also have generous free usage tiers.

CartoDB tends to focus more on the "make really pretty vector maps" side of the equation, with great visualisation tools like [Torque](http://blog.cartodb.com/torque-is-live-try-it-on-your-cartodb-maps-today/) (beautiful animations with time series data), powerful and simple [push-button visualisation of data](http://cartodb.com/visualize/), and a wonderful [SQL API](http://docs.cartodb.com/cartodb-platform/sql-api.html) for interacting directly with their PostGIS backend from the client. Oh - and they also have [some support for 3D](http://cartodb.com/case-studies/3d-bogota/) and can handle huge datasets, like [colouring every river in the US](http://cartodb.com/gallery/river-direction/).

And lastly, CartoDB comes with a powerful [point-and-click map building GUI](http://docs.cartodb.com/cartodb-editor.html#visualizations) or, if you need more control, the [CartoDB.js](http://docs.cartodb.com/cartodb-platform/cartodb-js.html) library exposes all of the same functionality. Oh, and did we mention that it's open source and you can [run your own CartoDB instance](https://github.com/CartoDB/cartodb)?

![A screenshot of the CartoDB Editor web interface](../imgs/cartodb-interface.png)

[MapBox](https://www.mapbox.com/) focuses slightly more on the traditionally geospatial side of things, with a powerful desktop map designer, [MapBox Studio](https://www.mapbox.com/mapbox-studio/) (which can process raster as well as vector data), some great work on [tools for processing](https://www.mapbox.com/blog/landsat-live-live/) [satellite imagery](https://www.mapbox.com/blog/processing-landsat-8/), developing the  [vector tiling](https://www.mapbox.com/developers/vector-tiles/) standard, and pushing the boundaries of web mapping with [MapBox GL](https://www.mapbox.com/mapbox-gl/). On top of all of that they also maintain [iOS](https://www.mapbox.com/mapbox-ios-sdk/) and [Android](https://www.mapbox.com/mapbox-android-sdk/) SDKs, the [Mapbox.js](https://www.mapbox.com/mapbox.js/api/) library; and APIs for [surface heights](https://www.mapbox.com/developers/api/surface/), [geocoding](https://www.mapbox.com/developers/api/geocoding/), and [directions](https://www.mapbox.com/developers/api/directions/).

And a couple of honorary mentions:

[GeoServer](http://geoserver.org/) is an open source spatial data server that may be worth you're look if you're having to deal with larger or more complex datasets that CartoDB/MapBox can't handle - or can't handle without charging you for the pleasure. GeoServer also has support for more advanced functionality like WCS and WPS for extracting raw data from rasters on-the-fly, or writing proceses to perform geospatial analysis on-the-fly. You can run GeoServer on its own, or in combination with other packages via the [OpenGeo Suite](http://boundlessgeo.com/solutions/opengeo-suite/) or [GeoNode](http://geonode.org/).

ESRI's ArcGIS software suite is worth a brief mention as the main commercial provider of geospatial software in the world, including its SaaS [ArcGIS Online](https://www.arcgis.com/home/) platform - which provides a 60-day free trial, after which you're required to pay (handsomely).

## NationalMap (aka TerriaJS)

And finally, a most honourary mention to the [NationalMap](http://nationalmap.nicta.com.au/) project out of the Department of Communications and developed by NICTA. NationlMap [runs on a powerful little open source stack](http://nationalmap.nicta.com.au/help/About.html) comprised of Cesium, Leaflet, topogeojson, Jasmine, et cetera. While NationalMap, being primarily a client-side viewing framework, isn't a true "Maps as a Service" platform it does have a nifty hidden feature - you can [pass it the URL to a JSON file](http://nationalmap.gov.au/help/HowTo.html#DisplayMyOwnSpatialData) and use an iframe to embed the result in your webpage.

Ta-da! Instant map :)

![A screenshot of NICTA's National Map web mapping app](../imgs/national-map-overlay.jpg)

There's also some work going on to turn NationalMap into a standalone single page JS library called [TerriaJS](https://github.com/TerriaJS/TerriaJS) - so watch this space for GovHack 2016!

# JavaScript mapping libraries

These past few years have seen an explosion in the numbers of JavaScript libraries for creating rich web mapping interfaces.

[OpenLayers](http://openlayers.org/) is probably the most mature player on the stage, and has recently undergone a ground-up rewrite of the library to simplify the API and leverage modern web technologies like WebGL, Canvas, and the full capabilities of HTML5 and CSS3. It even has support for true 3D web mapping via its [OL3-Cesium](http://openlayers.org/ol3-cesium/) plugin which seamlessly integrates the [Cesium](https://cesium.agi.com/) WebGL 3D globe library.

[Leaflet](http://leafletjs.com/), the relatively new kid on the block, started as a protest against other web mapping libraries that required a fair amount of knowledge of geopsatial data to use effectively. As such, it is a super simple API and a more limited range of features than the likes of OpenLayers (but has a large library of community-developed plugins that can help address that gap).

[ModestMaps](http://modestmaps.com/) is an even simpler library again than Leaflet, with a simple API and a focus on the core functionality of producing interactive maps easily.

[Turf](https://www.mapbox.com/blog/turf-gis-for-web-maps/) has been developed by the MapBox team and bills itself as "GIS for web maps" with support for common geospatial operations like buffering, contours, hexbinning, et cetera performed all in the client. Turf also integrates easily with Leaflet and MapBox.js.

## SVG-powered mapping data visualisations

If you're looking at maps as more of a data visualisation tool then the subcategory of web mapping libraries that play in the SVG space are probably more appropriate for your needs.

Well we couldn't not mention [D3.js](http://d3js.org/) in talking about data visualisation. Michael Bowman's [Designing Beautiful Maps with D3.js](http://bowmanmc.github.io/designing_maps/) talk is worth a look to familiarise yourself with the topic, and then head on over to this [truly exhaustive list](http://bl.ocksplorer.org/#/search/d3.geo) of examples of using D3 for maps on [bl.ocksplorer.org](http://bl.ocksplorer.org).

![A screenshot of the D3.js homepage](../imgs/d3js.jpg)

The team behind the graphing library Highcharts have a separate [Highmaps](http://www.highcharts.com/maps/demo) library that makes creating mapping data visualisations a breeze.

Lastly [Polymaps](http://polymaps.org/) is a bit of a hybrid library in that it provides image and vector-tiled maps via SVG, so you can mix up your choice of basemap (OpenStreetMap, Bing, et cetera) with your image and vector data easily.

## Web mapping frameworks

The last sub-category of web mapping library worth a mention are the rich web mapping frameworks that exist to provide a whole UI framework around the map itself (i.e. map toolbars, layer trees and controls, advanced data query UIs, et cetera).

First and foremost is the beautiful, modern, and AngularJS-based framework [map.geo.admin.ch](https://github.com/geoadmin/mf-geoadmin3) that the Swiss Federal Office of Topography has open sourced for all to use - check out [a demo](http://map.geo.admin.ch/).

If you're a Sencha fan the [GeoExt](http://geoext.org/) library is worth a look - though note that there are different versions for ExtJS 3 and ExtJS 4/5. In a similar vein you'll find both [GeoMOOSE](http://www.geomoose.org/) and [MapBender](http://mapbender3.org).

And lastly, [MapFish](http://mapfish.org/), a lighter framework than its cousins, and based on the older version of OpenLayers, but with a standalone Java library for printing web maps in [MapFish Print](http://www.mapfish.org/doc/print/).
