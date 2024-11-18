import geopandas as gpd
import streamlit as st

@st.cache_resource
def load_osm_parquet(url):
    """
    load the OSM data from a Parquet
        :param url: The URL of the Parquet file
        :type url: str
        :return: The GeoDataFrame with the OSM data
    """
    gdf_data_original = gpd.read_parquet(url)
    return gdf_data_original


def transform_ed_institution_osm_data(gdf_data_original, institution_type):

    gdf_data_final = gdf_data_original[gdf_data_original["amenity"] == institution_type]
    gdf_data_final.set_crs(epsg=4326, inplace=True, allow_override=True)
    gdf_data_final["centroid"] = gdf_data_final.geometry.centroid
    gdf_data_final = gdf_data_final.reset_index(drop=False)
    gdf_data_final = gdf_data_final.rename(columns={"feature_id": "osm_feature_id", "geometry": "osm_geometry"})
    gdf_data_final["institution_type"] = institution_type
    gdf_data_final["geometry_source"] = "osm"
    gdf_data_final = gdf_data_final[["institution_type", "name", "centroid", "osm_geometry", "geometry_source", "osm_feature_id"]]
    gdf_data_final.set_geometry("centroid", inplace=True)
    gdf_data_final.set_crs(epsg=4326, inplace=True, allow_override=True)
    return gdf_data_final


def transform_bus_stop_osm_data(gdf_data_original):

    gdf_data_final = gdf_data_original
    gdf_data_final.set_crs(epsg=4326, inplace=True, allow_override=True)
    gdf_data_final["centroid"] = gdf_data_original.geometry.centroid
    gdf_data_final["buffer100m"] = gdf_data_final["centroid"].buffer(0.001)
    gdf_data_final["buffer250m"] = gdf_data_final["centroid"].buffer(0.0025)
    gdf_data_final["buffer500m"] = gdf_data_final["centroid"].buffer(0.005)
    gdf_data_final = gdf_data_final.reset_index(drop=False)
    gdf_data_final = gdf_data_final.rename(columns={"feature_id": "osm_feature_id", "geometry": "osm_geometry"})
    gdf_data_final["geometry_source"] = "osm"
    gdf_data_final = gdf_data_final[["name", "centroid", "osm_geometry", "buffer100m", "buffer250m", "buffer500m", "geometry_source", "osm_feature_id"]]
    gdf_data_final.set_geometry("centroid", inplace=True)
    gdf_data_final.set_crs(epsg=4326, inplace=True, allow_override=True)
    return gdf_data_final

def transform_bus_line_osm_data(gdf_data_original):
    
    gdf_data_final = gdf_data_original
    gdf_data_final.set_crs(epsg=4326, inplace=True, allow_override=True)
    gdf_data_final = gdf_data_final.reset_index(drop=False)
    gdf_data_final = gdf_data_final.rename(columns={"feature_id": "osm_feature_id", "geometry": "osm_geometry"})
    gdf_data_final["geometry_source"] = "osm"
    gdf_data_final = gdf_data_final[["route_tags", "osm_geometry","geometry_source", "osm_feature_id"]]
    gdf_data_final.set_geometry("osm_geometry", inplace=True)
    gdf_data_final.set_crs(epsg=4326, inplace=True, allow_override=True)
    return gdf_data_final
