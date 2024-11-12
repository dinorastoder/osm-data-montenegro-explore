from dataclasses import dataclass
#import geopandas
import pooch
from typing import Union

class FilterOSM:
    def __init__(self, pbf_file_path):
        self._pbf_file_path = pbf_file_path

    def extract_all_schools_to_geodataframe(self):
        # qosm.convert_pbf_to_geodataframe(tags_filter={"admin_level": "6", "amenity": "bench"}, pbf_path="files/geofabrik_europe_montenegro.osm.pbf")
        return None
    
@dataclass
class PbfFileMetadata:
    source_url = "https://download.geofabrik.de/europe/montenegro-latest.osm.pbf"
    file_name = "montenegro-latest.osm.pbf"

class OSMExtractToPBF:
    
    def fetch_pbf_file(self, pbf_file_metadata: Union[PbfFileMetadata] ) -> str:
        pbf_file_path = pooch.retrieve(
            url=pbf_file_metadata.source_url,
            fname=pbf_file_metadata.file_name,
            known_hash=None,
            progressbar=True
        )

        print(pbf_file_path)

        return pbf_file_path
