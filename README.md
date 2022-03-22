# Interrail
This python library is an unofficial wrapper around the api of [Interrail](https://www.interrail.eu/en) which can be used to plan train trips through europe.

## Installation
```commandline
pip install interrail
```

## Usage

```python
from interrail.api import *

# To search for a station use get_stop_location
amsterdam = get_stop_location("Amsterdam Centraal")
paris = get_stop_location("Paris")


# To plan a trip between two stations use get_trip
trip = get_trip(origin=amsterdam, dest=paris, departure_time=datetime.now())
```

To see what fields `StopLocation` and `Trip` provide, reference [data.py](./interrail/data.py).

Note that `get_stop_location `/`get_trip` only return the first entry that the api provides. To view all entries use `get_stop_locations`/`get_trips`.


## Contributing
Currently, this wrapper is far from complete and probably contains bugs. Feel free to contribute using issues/prs.
