import streamlit as st
from osm_data_load_transform import load_osm_parquet, transform_bus_stop_osm_data

st.title("Public transportation")
st.sidebar.header("Mapping Demo")
map_preview = st.sidebar.checkbox("Preview data on map", True)

public_transportation_data = ["bus_stop"]
urls = {
    "bus_stop": "data/osm.bus_stop.20241104.parquet"
}

for data_type in public_transportation_data:
    url = urls[data_type]
    gdf_data_original = load_osm_parquet(url)
    gdf_data_final = transform_bus_stop_osm_data(gdf_data_original, data_type)

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
