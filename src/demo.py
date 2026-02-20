from spatial import Point

a = Point("A", 121.0, 14.6)
b = Point ("B", 122.0, 15.6)

print("A tuple:", a.to_tuple())
print("B tuple:", b.to_tuple())
print("Distance A to B:", a.distance_to(b))
