from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import List


@dataclass
class StopLocation:
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
    time: datetime
    track: str

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
            track=data["track"],
        )


@dataclass
class Leg:
    origin: Stop
    dest: Stop
    name: str

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            origin=Stop.from_dict(data["Origin"]),
            dest=Stop.from_dict(data["Destination"]),
            name=data["name"],
        )


@dataclass
class Trip:
    origin: Stop
    dest: Stop

    legs: List[Leg]

    def get_length(self) -> timedelta:
        return self.dest.time - self.origin.time

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            origin=Stop.from_dict(data["Origin"]),
            dest=Stop.from_dict(data["Destination"]),
            legs=list(map(lambda x: Leg.from_dict(x), data["LegList"]["Leg"])),
        )
