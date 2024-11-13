import streamlit as st
from helper import load_all_data


st.title("Educational institution")
st.sidebar.header("Mapping Demo")
map_preview = st.sidebar.checkbox("Preview data on map", True)

institution_types = ["kindergarten", "school", "university"]

for institution_type in institution_types:
    
    if institution_type + '_data_original' not in st.session_state:
        load_all_data()
    if institution_type + '_data_final' not in st.session_state:
        load_all_data()

    gdf_data_original = st.session_state[institution_type + '_data_original']
    gdf_data_final = st.session_state[institution_type + '_data_final']

    # Display the DataFrame in Streamlit
    col1, col2 = st.columns(2)
    with col1:
        st.header(f"{institution_type.capitalize()}(s) in Podgorica, Montenegro (Raw Data)")
        st.dataframe(gdf_data_original)

    with col2:
        st.header(f"{institution_type.capitalize()}(s) in Podgorica, Montenegro (Final Input Data)")
        st.dataframe(gdf_data_final)
        if map_preview:
            gdf_data_final["latitude"] = gdf_data_final["centroid"].y
            gdf_data_final["longitude"] = gdf_data_final["centroid"].x
            st.map(data=gdf_data_final, color="#00ff00")
