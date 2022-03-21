import unittest

from interrail.api import get_stop_location


class InterrailApi(unittest.TestCase):
    def test_search_for_stop_location_name(self):
        stop_location = get_stop_location("Leiden")

        self.assertEqual(stop_location.name, "LEIDEN CENTRAAL (Netherlands)")

    def test_search_for_stop_location_lat_lon(self):
        stop_location = get_stop_location("Amsterdam")

        self.assertEqual(stop_location.lat, 52.378607)
        self.assertEqual(stop_location.lon, 4.900829)


if __name__ == "__main__":
    unittest.main()
