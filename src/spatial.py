from shapely.geometry import Point as ShapelyPoint

class SpatialObject:
    """
    Base class for anything that exists in space.
    Stores geometry and provides shared spatial behavior/
    """
    
    def __init__(self, geometry):
        self.geometry = geometry
        
    def bbox(self):
        """
        Return bounding box as (minx, miny, maxx, maxy).
        """
        return self.geometry.bounds

# class Point:
#    def __init__(self, id, lon, lat, name=None, tag=None):
#        if not (-180 <= lon <= 180):
#            raise ValueError("Longitude must be between -180 and 180")
#        if not (-90 <= lat <= 90):
#            raise ValueError("Latitude must be between -90 and 90")
#        
#        self.id = id
#        self.geometry = ShapelyPoint(lon, lat)
#        self.name = name
#        self.tag = tag
        
    # -------------------------------------------------------------------
    # Update to_tuple() to read from Shapely geometry
    # -------------------------------------------------------------------
#    def to_tuple(self):
#        """
#        Retutn (x, y) as a simple tuple from the Shapely point.
#        """
#        return (self.geometry.x, self.geometry.y)
    
    # -------------------------------------------------------------------
    # Update distance_to() to delegate to Shapely
    # -------------------------------------------------------------------
#    def distance_to(self, other: "Point"):
#        """
#        Return planar distance between this Point and another Point.
#        """
#        return self.geometry.distance(other.geometry)

class Point(SpatialObject):
    def __init__(self, id, lon, lat, name=None, tag=None):
        if not (-180 <= lon <= 180):
            raise ValueError("Longitude must be between -180 and 180")
        if not (-90 <= lat <= 90):
            raise ValueError("Latitude must be between -90 and 90")
        
        geometry = ShapelyPoint(lon, lat)
        super().__init__(geometry)
        
        self.id = id
        self.name = name
        self.tag = tag
        
    def to_tuple(self):
        return (self.geometry.x, self.geometry.y)
    
    def distance_to(self, other):
        return self.geometry.distance(other.geometry)

class Parcel(SpatialObject):
    """
    Parcel = spatial object + structured attributes.
    """
    
    def __init__(self, parcel_id, geometry, attributes: dict):
        super().__init__(geometry)
        self.parcel_id = parcel_id
        self.attributes = attributes