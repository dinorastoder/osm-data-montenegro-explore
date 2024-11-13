from osm_data_load_transform import load_osm_parquet, transform_ed_institution_osm_data, transform_bus_stop_osm_data
import streamlit as st

def load_all_data():
    # Load data
    public_transportation_data = ["bus_stop"]
    urls = {
        "bus_stop": "data/osm.bus_stop.20241104.parquet"
    }

    for data_type in public_transportation_data:
        url = urls[data_type]
        gdf_data_original = load_osm_parquet(url)
        gdf_data_final = transform_bus_stop_osm_data(gdf_data_original, data_type)

        st.session_state[data_type + '_data_original'] = gdf_data_original
        st.session_state[data_type + '_data_final'] = gdf_data_final

    urls = {
        "kindergarten": "data/osm.kindergarten.20241104.parquet",
        "school": "data/osm.school.20241104.parquet",
        "university": "data/osm.university.20241104.parquet"
    }

    for institution_type in urls.keys():
        url = urls[institution_type]

        gdf_data_original = load_osm_parquet(url)
        gdf_data_final = transform_ed_institution_osm_data(gdf_data_original, institution_type)

        st.session_state[institution_type + '_data_original'] = gdf_data_original
        st.session_state[institution_type + '_data_final'] = gdf_data_final
