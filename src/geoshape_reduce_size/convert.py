import geopandas
from geoshape_reduce_size.config import get_path

def main():
    # Firstly download the shape file from here: https://www.abs.gov.au/AUSSTATS/abs@.nsf/DetailsPage/1270.0.55.005July%202016?OpenDocument
    inputfile = get_path("raw_shapefile")
    myshpfile = geopandas.read_file(inputfile)
    print(f"Read: {inputfile}")

    outputfile = get_path("geojson_output")
    myshpfile.to_file(outputfile, driver='GeoJSON')
    print(f"Written: {outputfile}")

if __name__ == "__main__":
    main()
