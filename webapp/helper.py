from osm_data_load_transform import load_osm_parquet, transform_bus_line_osm_data, transform_ed_institution_osm_data, transform_bus_stop_osm_data
import streamlit as st
from pathlib import Path

DATA_DIR = Path(__file__).parent.parent / "data"

def load_all_data():
    # Load data
    public_transportation_data = ["bus_stop", "bus_line"]
    urls = {
        "bus_stop": str(DATA_DIR / "osm.bus_stop.20241104.parquet"),
        "bus_line": str(DATA_DIR / "osm.bus_line.20241104.parquet"),
    }

    for data_type in public_transportation_data:
        url = urls[data_type]
        gdf_data_original = load_osm_parquet(url)
        gdf_data_final = transform_bus_stop_osm_data(gdf_data_original) if data_type == 'bus_stop' else transform_bus_line_osm_data(gdf_data_original)

        st.session_state[data_type + '_data_original'] = gdf_data_original
        st.session_state[data_type + '_data_final'] = gdf_data_final

    urls = {
        "kindergarten": str(DATA_DIR / "osm.kindergarten.20241104.parquet"),
        "school": str(DATA_DIR / "osm.school.20241104.parquet"),
        "university": str(DATA_DIR / "osm.university.20241104.parquet")
    }

    for institution_type in urls.keys():
        url = urls[institution_type]

        gdf_data_original = load_osm_parquet(url)
        gdf_data_final = transform_ed_institution_osm_data(gdf_data_original, institution_type)

        st.session_state[institution_type + '_data_original'] = gdf_data_original
        st.session_state[institution_type + '_data_final'] = gdf_data_final
