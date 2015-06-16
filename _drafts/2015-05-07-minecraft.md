---
layout: post
tags: ideas
title: An interactive geological map in Minecraft for Raspberry Pi
---



# Datasets & resources

- **Geological maps** - these are provided for the entire Australian continent via Open Geospatial Consortium Web Feature Services from Geoscience Australia. There's a _lot_ of data behind this service so you might just want to concentrate on a small area. You can request just the data lying within a given bounding box as follows:

This will give you an XML document which you can grep through to find the shape data, as well as a bunch of metadata (what rock type each shape refers to etc)

- **Shapely and Rasterio** - these libraries make it easy to handle vector and raster mapping data in Python. You'll need to get a way of transferring the XML from the feature service into a Shapely object.

- **Bukkit** and **RaspberryJuice** - this is an open source minecraft server which you can run locally on your machine to be able to test your maps, and a plugin which exposes a Python-based API for generating maps.

Once you're up and running you can consider
