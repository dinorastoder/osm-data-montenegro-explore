import streamlit as st

st.set_page_config(page_title="OSM data for Montenegro (Podgorica)", page_icon=":material/dashboard:",layout="wide")

page = st.navigation([
    st.Page("page_map_overview.py", title="Map overview"),
    st.Page("page_educational_institution.py", title="Data - Educational institution"),
    st.Page("page_public_transportation.py", title="Data - Public transportation")
])

page.run()
