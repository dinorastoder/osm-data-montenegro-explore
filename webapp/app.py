import streamlit as st

st.set_page_config(page_title="OSM data for Montenegro", page_icon=":material/dashboard:")

page = st.navigation([
    st.Page("page_map_overview.py", title="Map overview"),
    st.Page("page_educational_institution.py", title="Data - Educational institution")
])

page.run()
