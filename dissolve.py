# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Dissovle state boundaries
# 
# Using geopandas to take the Australian Remoteness Area boundaries (which are provided by state) and remove the state boundaries
# 
# A sample of the properties is:
# 
# ```json
# {
#     "properties":{
#         "RA_CODE16":"11"
#         ,"RA_NAME16":"Inner Regional Australia"
#         ,"STE_CODE16":"1"
#         ,"STE_NAME16":"New South Wales"
#         ,"AREASQKM16":87424.8418
#     }
# }
# ```
# 

# %%
## Import libraries
import pandas as pd
import geopandas as gpd
import math
import matplotlib.pyplot as plt


# %%
## Read in the file
inputfile='./RA_2016_AUST-simple.geojson'
ra = gpd.read_file(inputfile)


# %%
## plot the shape file on the map
ra['RA_CAT'] = pd.to_numeric(ra['RA_CODE16']) % 10
ra.plot(column = 'RA_CAT', categorical=True,legend=True,edgecolor='black',figsize=(15, 15))


# %%
## Print the tabular data of the GeoSeries
ra


# %%
ra.geometry.crs


# %%
## Clean out polygons without area
ra_clean = ra[ra.area > 0]
## Remove the state from the RA Code before dissolve
ra_clean['RA_CODE16'] = pd.to_numeric(ra_clean['RA_CODE16']) % 10 + 100


# %%
## Dissolve state boundaries
aus = ra_clean.dissolve(by='RA_NAME16', as_index=False)
## Overwrite the state fields to Australia
aus['STE_CODE16'] = 10
aus['STE_NAME16'] = 'Australia'
aus


# %%
aus.plot(column = 'RA_CAT', categorical=True,legend=True,edgecolor='black',figsize=(15, 15))


# %%
## Concatenate the Australia features to the original
ra_with_aus = gpd.GeoDataFrame( pd.concat( [aus, ra_clean], ignore_index=True) )
ra_with_aus


# %%
## Write to geojson
ra_with_aus.to_file("./RA_2016_AUST_all.geojson", driver="GeoJSON")


# %%



