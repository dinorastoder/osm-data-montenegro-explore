import streamlit as st
from folium.vector_layers import CircleMarker
import leafmap.foliumap as leafmap
import geopandas as gpd
from helper import load_all_data


st.title("Main Page")

m = leafmap.Map(tiles="Cartodb Positron")

m.zoom_to_bounds((18.9894022, 42.3356869, 19.6647575, 42.7089575))

institution_types = ["kindergarten", "school", "university"]

for institution_type in institution_types:
    if institution_type + '_data_final' not in st.session_state:
        load_all_data()

    gdf_institution_final = st.session_state[institution_type + '_data_final']
    gdf_institution_final = gdf_institution_final[["name", "centroid"]]

    m.add_gdf(
        gdf=gdf_institution_final,
        layer_name=f"{institution_type.capitalize()}",
        popup_field="name",
        marker=CircleMarker(),
    )

if 'bus_stop_data_final' not in st.session_state:
    load_all_data()

gdf_bus_stop_final = st.session_state['bus_stop_data_final']

gdf_bus_stop_buffer_union = gpd.GeoDataFrame({
    'type': ["buffer100m", "buffer250m", "buffer500m"],
    'geometry': [
        gdf_bus_stop_final["buffer100m"].unary_union,
        gdf_bus_stop_final["buffer250m"].unary_union,
        gdf_bus_stop_final["buffer500m"].unary_union
    ]
}, crs="EPSG:4326")

m.add_gdf(
    gdf=gdf_bus_stop_buffer_union[(gdf_bus_stop_buffer_union['type'] == "buffer100m")],
    layer_name="Bus stop buffer 100m",
    popup_field="type",
    style={
        "fillColor": "#ff0000",
        "color": "#00ff00"
    }
)

m.add_gdf(
    gdf=gdf_bus_stop_buffer_union[(gdf_bus_stop_buffer_union['type'] == "buffer250m")],
    layer_name="Bus stop buffer 250m",
    popup_field="type",
    style={
        "color": "#0000ff"
    }
)

m.add_gdf(
    gdf=gdf_bus_stop_buffer_union[(gdf_bus_stop_buffer_union['type'] == "buffer500m")],
    layer_name="Bus stop buffer 500m",
    popup_field="type",
    style={
        "color": "#ff0000"
    }
)

if 'bus_line_data_final' not in st.session_state:
    load_all_data()

gdf_bus_line_final = st.session_state['bus_line_data_final']

m.add_gdf(
    gdf=gdf_bus_line_final,
    layer_name="Bus line",
    popup_field="route_tags",
    style={
        "color": "#0000ff"
    }
)

m.to_streamlit(height=900)
