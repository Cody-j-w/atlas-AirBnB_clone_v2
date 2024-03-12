from models import storage

def test_func():
    states = storage.all("State").values()
    amenities = storage.all("Amenity").values()
    for state in states:
        print(state.name)
    for amenity in amenities:
        print(amenity.name)
test_func()