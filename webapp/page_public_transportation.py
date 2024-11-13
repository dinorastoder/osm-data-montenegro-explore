import streamlit as st
import geopandas as gpd

st.title("Public transportation")
st.sidebar.header("Mapping Demo")
map_preview = st.sidebar.checkbox("Preview data on map", True)

def load_and_transform_osm_data(url, data_type):
    gdf_data_original = gpd.read_parquet(url)
    gdf_data_final = gdf_data_original.to_crs("EPSG:4326")

    gdf_data_final["centroid"] = gdf_data_original.geometry.centroid
    gdf_data_final["buffer100m"] = gdf_data_final["centroid"].buffer(0.001)
    gdf_data_final["buffer250m"] = gdf_data_final["centroid"].buffer(0.0025)
    gdf_data_final["buffer500m"] = gdf_data_final["centroid"].buffer(0.005)
    gdf_data_final = gdf_data_final.reset_index(drop=False)
    gdf_data_final = gdf_data_final.rename(columns={"feature_id": "osm_feature_id", "geometry": "osm_geometry"})
    gdf_data_final["geometry_source"] = "osm"
    gdf_data_final = gdf_data_final[["name", "centroid", "osm_geometry", "buffer100m", "buffer250m", "buffer500m", "geometry_source", "osm_feature_id"]]
    return gdf_data_original, gdf_data_final

public_transportation_data = ["bus_stop"]
urls = {
    "bus_stop": "data/osm.bus_stop.20241104.parquet"
}

for data_type in public_transportation_data:
    url = urls[data_type]
    gdf_data_original, gdf_data_final = load_and_transform_osm_data(url, data_type)

    # Display the DataFrame in Streamlit
    col1, col2 = st.columns(2)
    with col1:
        st.header(f"{data_type.capitalize()} in Podgorica, Montenegro (Raw Data)")
        st.dataframe(gdf_data_original)

    with col2:
        st.header(f"{data_type.capitalize()} in Podgorica, Montenegro (Final Input Data)")
        st.dataframe(gdf_data_final)
        if map_preview:
            gdf_data_final["latitude"] = gdf_data_final["centroid"].y
            gdf_data_final["longitude"] = gdf_data_final["centroid"].x
            st.map(data=gdf_data_final, color="#00ff00")
