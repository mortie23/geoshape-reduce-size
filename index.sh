#!/usr/bin/bash

## Run the convert Python script to convert from Shape to GeoJSON
echo "Converting from ESRI Shape to GeoJSON"
./convert.py

## Reduce the size using the NodeJS mapshaper library
echo "Reducing size to 1% of original"
mapshaper /mnt/c/data/geodata/RA_2016_AUST/RA_2016_AUST.geojson -simplify dp 1% keep-shapes -o format=geojson ./RA_2016_AUST-simple.geojson
