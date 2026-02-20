
from shapely.geometry import Polygon
from spatial import Point, Parcel


def main():
    a = Point("A", 121.00, 14.60, name="Gate", tag="POI")
    b = Point("B", 121.02, 14.55, name="Corner", tag="POI")
    print("A tuple:", a.to_tuple())
    print("B tuple:", b.to_tuple())
    print("Distance A-B:", a.distance_to(b))

    geom = Polygon([(0, 0), (10, 0), (10, 5), (0, 5)])
    attrs = {"area": 50.0, "zone": "Residential", "is_active": True}
    parcel = Parcel(parcel_id=101, geometry=geom, attributes=attrs)
    print("Point bbox:", a.bbox())
    print("Parcel bbox:", parcel.bbox())
    print("Parcel zone:", parcel.attributes["zone"])

    row = {"id": "C", "lon": 121.01, "lat": 14.58, "name": "Checkpoint", "tag": "POI"}
    c = Point.from_dict(row)
    print("C tuple (from_dict):", c.to_tuple())

    print("Point A as_dict:", a.as_dict())
    print("Parcel as_dict:", parcel.as_dict())

    inside = Point("IN", 5, 2.5)
    outside = Point("OUT", 20, 20)
    print("Inside intersects parcel:", inside.intersects(parcel))   # True
    print("Outside intersects parcel:", outside.intersects(parcel)) # False


if __name__ == "__main__":
    main()
