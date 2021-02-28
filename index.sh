#!/usr/bin/bash

echo "Converting from ESRI Shape to GeoJSON"
./convert.py
echo "Reducing size to 5% of original"
mapshaper /mnt/c/data/geodata/RA_2016_AUST/RA_2016_AUST.geojson -simplify dp 5% keep-shapes -o format=geojson ./RA_2016_AUST-simple.geojson
