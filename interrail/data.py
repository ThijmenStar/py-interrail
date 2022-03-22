from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import List, Optional


@dataclass
class StopLocation:
    """
    Represents a train station
    """

    id: str
    name: str
    lon: float
    lat: float

    def get_coords(self) -> tuple:
        return self.lat, self.lon

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data["id"],
            name=data["name"],
            lon=data["lon"],
            lat=data["lat"],
        )


@dataclass
class Stop(StopLocation):
    """
    Represents an arrival/departure at a StopLocation at a specific time
    """

    time: datetime
    track: Optional[str]

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data["id"],
            name=data["name"],
            lon=data["lon"],
            lat=data["lat"],
            time=datetime.strptime(
                f"{data['date']} {data['time']}", "%Y-%m-%d %H:%M:%S"
            ),
            track=data.get("track"),
        )


@dataclass
class Leg:
    """
    Represents a segment of a train route
    """

    origin: Stop
    dest: Stop
    name: str

    def get_duration(self) -> timedelta:
        return self.dest.time - self.origin.time

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            origin=Stop.from_dict(data["Origin"]),
            dest=Stop.from_dict(data["Destination"]),
            name=data["name"],
        )


@dataclass
class Trip:
    """
    Represents a trip from origin to destination consisting of one or multiple legs
    """

    origin: Stop
    dest: Stop

    legs: List[Leg]

    def get_duration(self) -> timedelta:
        return self.dest.time - self.origin.time

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            origin=Stop.from_dict(data["Origin"]),
            dest=Stop.from_dict(data["Destination"]),
            legs=list(map(lambda x: Leg.from_dict(x), data["LegList"]["Leg"])),
        )
