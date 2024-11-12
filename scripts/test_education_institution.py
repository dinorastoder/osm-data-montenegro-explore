import unittest
#import geopandas
from education_institucion import FilterOSM, PbfFileMetadata, OSMExtractToPBF

class TestEducationInstitution(unittest.TestCase):

    def setUp(self):
        #self.filter = FilterOSM()
        self.osmExtract = OSMExtractToPBF()

    #@unittest.skip   
    #def test_gdf(self):
    #    self.assertIsInstance(self.filter.extract_all_schools_to_geodataframe(None, None), geopandas.GeoDataFrame)

    def test_osmExtractPlain(self):
        self.assertRegex(self.osmExtract.fetch_pbf_file(PbfFileMetadata()), ".pbf")
    
    def test_FilterOSM(self):
        filter = FilterOSM("string as a file path")
        self.assertFalse(False)

if __name__ == "__main__":
    unittest.main()
