from dataclasses import dataclass


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
