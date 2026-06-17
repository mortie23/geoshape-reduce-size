import pandas as pd
import geopandas as gpd
from geoshape_reduce_size.config import get_path

def main():
    inputfile = get_path("simplified_geojson")
    ra = gpd.read_file(inputfile)
    print(f"Read: {inputfile}")

    # Fix any invalid geometries before dissolving
    ra_valid = ra.copy()
    ra_valid.geometry = ra_valid.geometry.make_valid()
    ra_clean = ra_valid[ra_valid.area > 0].copy()
    ra_clean['RA_CODE16'] = pd.to_numeric(ra_clean['RA_CODE16']) % 10

    # Dissolve state boundaries
    aus = ra_clean.dissolve(by='RA_NAME16', as_index=False)
    aus['STE_CODE16'] = 10
    aus['STE_NAME16'] = 'Australia'
    aus['RA_CODE16'] = aus['RA_CODE16'] + 100

    # Combine dissolved Australia features with the originals
    ra_with_aus = gpd.GeoDataFrame(pd.concat([aus, ra], ignore_index=True))

    outputfile = get_path("dissolved_geojson")
    ra_with_aus.to_file(outputfile, driver="GeoJSON")
    print(f"Written: {outputfile}")

if __name__ == "__main__":
    main()
