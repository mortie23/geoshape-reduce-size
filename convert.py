#!/usr/bin/python3

import geopandas

inputfile='/mnt/c/data/geodata/RA_2016_AUST/RA_2016_AUST.shp'
myshpfile = geopandas.read_file(inputfile)
print(inputfile+': file read')
outputfile='/mnt/c/data/geodata/RA_2016_AUST/RA_2016_AUST.geojson'
myshpfile.to_file(outputfile, driver='GeoJSON') 
print(outputfile+': file written')
