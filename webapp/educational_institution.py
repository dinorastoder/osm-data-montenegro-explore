import streamlit as st
import geopandas as gpd

st.title("Educational institution")

url = "data/osm.kindergarten.20241104.parquet"
gdf_kindergarten = gpd.read_parquet(url)
gdf_kindergarten = gdf_kindergarten.to_crs("EPSG:4326")

gdf_kindergarten_final = gdf_kindergarten[gdf_kindergarten["amenity"] == "kindergarten"]
gdf_kindergarten_final = gdf_kindergarten_final[["name", "geometry"]]
gdf_kindergarten_final["centroid"] = gdf_kindergarten_final.geometry.centroid
gdf_kindergarten_final["buffer100m"] = gdf_kindergarten_final.geometry.buffer(0.1)
gdf_kindergarten_final["buffer250m"] = gdf_kindergarten_final.geometry.buffer(0.25)
gdf_kindergarten_final["buffer500m"] = gdf_kindergarten_final.geometry.buffer(0.5)

# Display the DataFrame in Streamlit
st.header("Kindergartens in Montenegro (Raw Data)")
st.dataframe(gdf_kindergarten)
st.header("Kindergartens in Montenegro (Final Data)")
st.dataframe(gdf_kindergarten_final)
