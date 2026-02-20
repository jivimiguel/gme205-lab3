# from spatial import Point

# p = Point("A", 121.0, 14.6) 
# print("BBox:", p.bbox()) 
# print("Tuple:", p.to_tuple()) 

# from shapely.geometry import Polygon 
# from spatial import Parcel

# a simple rectangle polygon sample 
# geom = Polygon([ 
# (0, 0), 
# (10, 0), 
# (10, 5), 
# (0, 5) 
# ]) 

# Dictionary for added structure 
# attrs = { 
#    "area": 50.0, 
#    "zone": "Residential", 
#    "is_active": True 
# } 
#parcel = Parcel(parcel_id=101, geometry=geom, attributes=attrs)

# print("Parcel BBox:", parcel.bbox()) 
# print("Parcel Zone:", parcel.attributes["zone"]) 


# from spatial import Point

# row_good = {"id": "A", "lon": 121.0, "lat": 14.6}
# row_bad  = {"id": "B", "lon": 999, "lat": 14.6}

# p = Point.from_dict(row_good)
# print("Valid Point:", p.to_tuple())

# try:
#     bad = Point.from_dict(row_bad)
# except Exception as e:
#     print("Invalid dictionary error:", e)
    
# from shapely.geometry import Polygon
# from spatial import Point, Parcel

# p = Point("A", 121.0, 14.6)
# print("Point as dict:", p.as_dict())

# geom = Polygon([(0,0),(10,0),(10,5),(0,5)])
# attrs = {"area":50,"zone":"Residential","is_active":True}
# parcel = Parcel(101, geom, attrs)

# print("Parcel as dict:", parcel.as_dict())

from spatial import Point, Parcel
from shapely.geometry import Polygon

# Parcel polygon
parcel_geom = Polygon([(0,0),(10,0),(10,10),(0,10)])
parcel = Parcel(100, parcel_geom, {})

# Point inside
inside = Point("IN", 5, 5)

# Point outside
outside = Point("OUT", 20, 20)


print("Inside intersects parcel:", inside.intersects(parcel))
print("Outside intersects parcel:", outside.intersects(parcel))