#!/usr/bin/python3

import geopandas

## Firstly download the shape file from here: https://www.abs.gov.au/AUSSTATS/abs@.nsf/DetailsPage/1270.0.55.005July%202016?OpenDocument
inputfile='/mnt/c/data/geodata/RA_2016_AUST/RA_2016_AUST.shp'
myshpfile = geopandas.read_file(inputfile)
print(inputfile+': file read')

## Convert the shape file to GeoJSON and write 
outputfile='/mnt/c/data/geodata/RA_2016_AUST/RA_2016_AUST.geojson'
myshpfile.to_file(outputfile, driver='GeoJSON') 
print(outputfile+': file written')
