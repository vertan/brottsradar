from app import db, models
import math
from pprint import pprint

class DistanceCalculator
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude
    
    def find_crimes():
        clause = "((69.1 * (latitude - :lat) * (latitude - :lat)) + (53.0 * (longitude - :lon) * (longitude - :lon))) < 0.01"
        query = db.session.query(models.Crime).filter(clause).params(lat=self.latitude, lon=self.longitude)
        r = query.all()
        a = 0
        for i in r:
            distance = selflaw_of_cosines(i.latitude, self.latitude, i.longitude, self.longitude)
            # Ignore crimes without a home
            if i.latitude == 59.858143 and i.longitude == 17.644587:
                continue
            if distance < 200:
                a = a+1 
                print distance
                pprint (vars(i))

    def law_of_cosines(lat1, lat2, lon1, lon2):
        R = 6371 # Earht radius in km
        lat1 = lat1 * math.pi / 180;
        lat2 = lat2 * math.pi / 180;
        lon1 = lon1 * math.pi / 180;
        lon2 = lon2 * math.pi / 180;
        d = math.acos(math.sin(lat1)*math.sin(lat2) + math.cos(lat1)*math.cos(lat2) * math.cos(lon2-lon1)) * R

        # Returns meter
        return d*1000

# Flogsta
my_lat = 59.84886
my_lon = 17.597866

# OG
my_lat = 59.855524
my_lon = 17.638807


