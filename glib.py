class GeoPoint:
    #sets 3 attributes: self.lat, self.lon, and self.description
    def __init__(self, lat = 0.0, lon = 0.0, description = ''):
        self.lat = lat
        self.lon = lon
        self.description = description

    #sets values of self.lat and self.lon
    def SetPoint(self, coords):
        self.lat = coords[0]
        self.lon = coords[1]
        
    #returns a list with self.lat and self.lon
    def GetPoint(self):
        point = [self.lat, self.lon]
        return point

    def SetDescription(self, description):
        self.description = description
        
    def GetDescription(self):
        return self.description

    PointCoords = property(GetPoint,SetPoint)
    Description = property(GetDescription, SetDescription)

    #Calculates the distance between the object's coordinates and the user's coordinates that are passed in as parameters
    def Distance(self, point): #gets distance from self to point (both are GeoPoints)
        import math
        
        lat1 = math.radians(self.lat)
        lon1 = math.radians(self.lon)
        lat2 = math.radians(point.lat)
        lon2 = math.radians(point.lon)
        dLat = lat2 - lat1
        dLon = lon2 - lon1
        R = 6371.00 #radius of the earth in km
        A = math.sin(dLat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dLon/2)**2 
        C = 2 * math.atan2(math.sqrt(A), math.sqrt(1-A))   
        D = R * C
        return D

    #set's the object's description
    def SetDescription(self, desc):
        self.description = desc

    #returns the object's description
    def GetDescription(self):
        return self.description
