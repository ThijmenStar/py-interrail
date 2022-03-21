from json import loads
from typing import List

import requests as requests

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
