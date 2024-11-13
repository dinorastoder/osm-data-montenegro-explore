import streamlit as st
from folium.vector_layers import CircleMarker
import leafmap.foliumap as leafmap
import geopandas as gpd
import json


st.title("Main Page")

m = leafmap.Map(tiles="Cartodb Positron")

m.zoom_to_bounds((18.9894022, 42.3356869, 19.6647575, 42.7089575))

url = "data/osm.kindergarten.20241104.parquet"
gdf_kindergarten = gpd.read_parquet(url)

gdf_kindergarten = gdf_kindergarten.to_crs("EPSG:4326")
gdf_kindergarten = gdf_kindergarten[gdf_kindergarten["amenity"] == "kindergarten"]
gdf_kindergarten = gdf_kindergarten[["name", "geometry"]]
gdf_kindergarten_final = gdf_kindergarten[["name", "geometry"]]
gdf_kindergarten_final["centroid"] = gdf_kindergarten_final.geometry.centroid
gdf_kindergarten_final["buffer100m"] = gdf_kindergarten_final["centroid"].buffer(0.001)
gdf_kindergarten_final["buffer250m"] = gdf_kindergarten_final["centroid"].buffer(0.0025)
gdf_kindergarten_final["buffer500m"] = gdf_kindergarten_final["centroid"].buffer(0.005)

# Remove the area of the 100m buffer from the 250m buffer
gdf_kindergarten_final["buffer250m_diff"] = gdf_kindergarten_final["buffer250m"].difference(gdf_kindergarten_final["buffer100m"])

# Convert the GeoDataFrame to GeoJSON
#geojson = json.loads(gdf_kindergarten.to_json())

# Add the centroid to the map
m.add_geojson(
    gdf_kindergarten_final[["name", "centroid"]].rename(columns={"centroid": "geometry"}).to_json(),
    marker=CircleMarker(),
    layer_name="Kindergarten (Centroid)",
    popup_field="name"
)

# Add the buffer 100m to the map
m.add_geojson(
    gdf_kindergarten_final[["name", "buffer100m"]].rename(columns={"buffer100m": "geometry"}).to_json(),
    layer_name="Kindergarten (100m buffer)",
    popup_field="name",
    style={
        "fillColor": "#00ff00",
        "color": "#00ff00"
    }
)

# Add the buffer 250m to the map
m.add_geojson(
    gdf_kindergarten_final[["name", "buffer250m_diff"]].rename(columns={"buffer250m_diff": "geometry"}).to_json(),
    layer_name="Kindergarten (250m buffer)",
    popup_field="name",
    style={
        "fillColor": "#ff0000",
        "color": "#ff0000"
    }
)    

# Add the buffer 500m to the map
m.add_gdf(
    gdf_kindergarten_final[["name", "buffer500m"]].set_geometry("buffer500m"),
    layer_name="Kindergarten (500m buffer)",
    popup_field="name",
    style={
        "fillColor": "#0000ff",
        "color": "#0000ff"
    }
)

# Add the union buffer 500m to the map
u = gdf_kindergarten_final["buffer500m"].unary_union
d = {'number': [1], 'geometry': u}
gdf = gpd.GeoDataFrame(d, crs="EPSG:4326")
m.add_gdf(
    gdf,
    layer_name="Kindergarten (Union 500m buffer)",
    style={
        "fillColor": "#000ff0",
        "color": "#000ff0"
    }
)

m.to_streamlit(height=900)
