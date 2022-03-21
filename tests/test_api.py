import datetime
import unittest

from interrail.api import get_stop_location, get_trip


class InterrailApi(unittest.TestCase):
    def test_get_for_stop_location_name(self):
        stop_location = get_stop_location("Leiden")

        self.assertEqual(stop_location.name, "LEIDEN CENTRAAL (Netherlands)")

    def test_get_for_stop_location_lat_lon(self):
        stop_location = get_stop_location("Amsterdam")

        self.assertEqual(stop_location.lat, 52.378607)
        self.assertEqual(stop_location.lon, 4.900829)

    def test_get_trip(self):
        leiden = get_stop_location("Leiden")
        rijswijk = get_stop_location("Rijswijk")

        trip = get_trip(
            leiden,
            rijswijk,
            datetime.datetime(year=2022, month=3, day=21, hour=10, minute=0),
        )

        self.assertEqual(trip.legs[0].dest.name, "DEN HAAG HS (Netherlands)")

    def test_get_length(self):
        leiden = get_stop_location("Leiden")
        rijswijk = get_stop_location("Rijswijk")

        trip = get_trip(
            leiden,
            rijswijk,
            datetime.datetime(year=2022, month=3, day=21, hour=10, minute=0),
        )

        self.assertEqual(trip.get_length(), datetime.timedelta(minutes=20))


if __name__ == "__main__":
    unittest.main()
