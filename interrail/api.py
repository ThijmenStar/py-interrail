from datetime import datetime
from json import loads
from typing import List

import requests as requests

from interrail.data.routes import Trip
from interrail.data.stations import StopLocation

INTERRAIL_API_URI = "https://api.eurail.com"
LANG = "en"


def get_stop_locations(query: str) -> List[StopLocation]:
    """
    Retrieves a list of StopLocations matching the query.

    :param query: the search query
    :return: the StopLocations returned by interrail
    """
    param = {"input": query}
    res = requests.get(INTERRAIL_API_URI + "/timetable/location.name", params=param)

    data = loads(res.text)

    stop_locations = data["stopLocationOrCoordLocation"]
    stop_locations = list(
        map(lambda x: StopLocation.from_dict(x["StopLocation"]), stop_locations)
    )

    return stop_locations


def get_stop_location(query: str) -> StopLocation:
    """
    Retrieves the top StopLocation matching the query.

    :param query: the search query
    :return: the first StopLocations returned by interrail
    """
    return get_stop_locations(query)[0]


def get_trips(
    origin: StopLocation, dest: StopLocation, departure_time: datetime
) -> List[Trip]:
    """
    Retrieves possible trips between two StopLocations.

    :param origin: the start location of the trip
    :param dest: the end location of the trip
    :param departure_time: the minimum departure time
    :return: the trips
    """
    param = {
        "lang": LANG,
        "originId": origin.id,
        "destId": dest.id,
        "date": format(departure_time.date(), "%Y-%m-%d"),
        "time": format(departure_time.time(), "%H:%M:%S"),
    }

    res = requests.get(INTERRAIL_API_URI + "/timetable/trip", params=param)

    data = loads(res.text)

    trips = data["Trip"]
    trips = list(map(lambda x: Trip.from_dict(x), trips))

    return trips


def get_trip(
    origin: StopLocation, dest: StopLocation, departure_time: datetime
) -> Trip:
    """
    Retrieves the first trip between two StopLocations

    :param origin: the start location of the trip
    :param dest: the end location of the trip
    :param departure_time: the minimum departure time
    :return: the first trip
    """
    return get_trips(origin, dest, departure_time)[0]
