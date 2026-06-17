import geopandas as gpd
from geoshape_reduce_size.config import get_path, get_value

def main():
    inputfile = get_path("geojson_output")
    gdf = gpd.read_file(inputfile)
    print(f"Read: {inputfile} ({len(gdf)} features)")

    tolerance = get_value("simplify_tolerance")
    gdf.geometry = gdf.geometry.simplify(tolerance, preserve_topology=True)
    print(f"Simplified with tolerance={tolerance}")

    outputfile = get_path("simplified_geojson")
    gdf.to_file(outputfile, driver="GeoJSON")
    print(f"Written: {outputfile}")

if __name__ == "__main__":
    main()
