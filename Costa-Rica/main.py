import geopandas as gpd  # if geopandas is not installed, run `pip install geopandas` in the project's directory.

# we are importing the observational data from the ZIP file provided (which contains the shape file) into a GeoDataFrame
gdf = gpd.read_file('Data/Clasification_Plots.zip')

# these display information about the GeoDataFrame to confirm the contains are what we expected
display(gdf.crs)
display(gdf.columns)