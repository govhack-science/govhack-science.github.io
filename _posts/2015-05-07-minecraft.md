---
layout: post
tags: ideas
title: An interactive geological map in Minecraft for Raspberry Pi
photo_url: http://www.scienceimage.csiro.au/images/cache/detail/976_0_BU5630.jpg
---

Produce a map generator which uses geological data from Geoscience Australia's Geological Maps and topography webservices to generate playable Minecraft maps with real geology.

[![A mining truck](http://www.scienceimage.csiro.au/images/cache/detail/976_0_BU5630.jpg)](http://www.scienceimage.csiro.au/image/5285/a-120-ton-ore-truck-at-the-new-celebration-gold-mine//large)

[Here's a similar idea](http://www.bgs.ac.uk/discoveringGeology/geologyOfBritain/minecraft/home.html) produced by the British Geological Survey for the UK. 

**Datasets & resources**:

- **Geological maps & topography** - these are provided for the entire Australian continent via Open Geospatial Consortium Web Feature Services from Geoscience Australia (for example, here's [the endpoint for WA's geology](http://www.ga.gov.au/geows/geologicunits/oneg_wa_1m/wfs?request=GetCapabilities&service=wfs&version=1.1.0)). There's a _lot_ of data behind this service so you might just want to concentrate on a small area - you can request just the data lying within a given bounding box. This will give you an XML document which you can grep through to find the shape data, as well as a bunch of metadata (what rock type each shape refers to etc). Check out GA's list of webservices for more info.

- **[Fiona](https://github.com/Toblerity/Fiona), [Shapely](https://github.com/Toblerity/Shapely) and [Rasterio](https://github.com/mapbox/rasterio)** - these libraries make it easy to handle vector and raster mapping data in Python. You'll need to get a way of transferring the XML from the feature service into a Shapely object.

- [**Bukkit**](https://bukkit.org/) and [**RaspberryJuice**](http://dev.bukkit.org/bukkit-plugins/raspberryjuice/) - this is an open source minecraft server which you can run locally on your machine to be able to test your maps, and a plugin which exposes a Python-based API for generating maps.

Once you're up and running you can consider adding other datasets to your map generator - given the GA data is just coming from a WFS you should be able to handle any other WFS endpoint to give you access to a new dataset.
