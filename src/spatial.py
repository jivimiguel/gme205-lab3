from shapely.geometry import Point as ShapelyPoint

class Point:
    def __init__(self, id, lon, lat, name=None, tag=None):
        if not (-180 <= lon <= 180):
            raise ValueError("Longitude must be between -180 and 180")
        if not (-90 <= lat <= 90):
            raise ValueError("Latitude must be between -90 and 90")
        
        self.id = id
        self.geometry = ShapelyPoint(lon, lat)
        self.name = name
        self.tag = tag
        
    # -------------------------------------------------------------------
    # Update to_tuple() to read from Shapely geometry
    # -------------------------------------------------------------------
    def to_tuple(self):
        """
        Retutn (x, y) as a simple tuple from the Shapely point.
        """
        return (self.geometry.x, self.geometry.y)
    
    # -------------------------------------------------------------------
    # Update distance_to() to delegate to Shapely
    # -------------------------------------------------------------------
    def distance_to(self, other: "Point"):
        """
        Return planar distance between this Point and another Point.
        """
        return self.geometry.distance(other.geometry)