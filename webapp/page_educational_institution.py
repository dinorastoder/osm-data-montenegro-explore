import streamlit as st
import geopandas as gpd

st.title("Educational institution")

def load_and_transform_osm_data(url, institution_type):
    gdf_data_original = gpd.read_parquet(url)
    gdf_data_original = gdf_data_original.to_crs("EPSG:4326")

    gdf_data_final = gdf_data_original[gdf_data_original["amenity"] == institution_type]
    gdf_data_final["centroid"] = gdf_data_final.geometry.centroid
    gdf_data_final = gdf_data_final.reset_index(drop=False)
    gdf_data_final = gdf_data_final.rename(columns={"feature_id": "osm_feature_id", "geometry": "osm_geometry"})
    gdf_data_final["institution_type"] = institution_type
    gdf_data_final["geometry_source"] = "osm"
    gdf_data_final = gdf_data_final[["institution_type", "name", "centroid", "osm_geometry", "geometry_source", "osm_feature_id"]]
    return gdf_data_original, gdf_data_final

institution_types = ["kindergarten", "school", "university"]
urls = {
    "kindergarten": "webapp/data/osm.kindergarten.20241104.parquet",
    "school": "webapp/data/osm.school.20241104.parquet",
    "university": "webapp/data/osm.university.20241104.parquet"
}

for institution_type in institution_types:
    url = urls[institution_type]
    gdf_data_original, gdf_data_final = load_and_transform_osm_data(url, institution_type)

    # Display the DataFrame in Streamlit
    col1, col2 = st.columns(2)
    with col1:
        st.header(f"{institution_type.capitalize()} in Podgorica, Montenegro (Raw Data)")
        st.dataframe(gdf_data_original)

    with col2:
        st.header(f"{institution_type.capitalize()} in Podgorica, Montenegro (Final Data)")
        st.dataframe(gdf_data_final)
        gdf_data_final["latitude"] = gdf_data_final["centroid"].y
        gdf_data_final["longitude"] = gdf_data_final["centroid"].x
        st.map(data=gdf_data_final, color="#00ff00", zoom=12)
