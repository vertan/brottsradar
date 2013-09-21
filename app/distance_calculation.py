# encoding: utf-8
from app import db, models
import math
from datetime import datetime
from pprint import pprint

class DistanceCalculator:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude
    
    def law_of_cosines(self, lat1, lat2, lon1, lon2):
        R = 6371 # Earht radius in km
        lat1 = lat1 * math.pi / 180;
        lat2 = float(lat2) * math.pi / 180;
        lon1 = lon1 * math.pi / 180;
        lon2 = float(lon2) * math.pi / 180;
        d = math.acos(math.sin(lat1)*math.sin(lat2) + math.cos(lat1)*math.cos(lat2) * math.cos(lon2-lon1)) * R

        # Returns meter
        return d*1000
    
    def find_crimes(self):
        clause = "((69.1 * (latitude - :lat) * (latitude - :lat)) + (53.0 * (longitude - :lon) * (longitude - :lon))) < 0.01"
        query = db.session.query(models.Crime).filter(clause).params(lat=self.latitude, lon=self.longitude)
        r = query.all()
        a = 0
        crime_score = 0
        now = datetime.now()
        for i in r:
            distance = self.law_of_cosines(i.latitude, self.latitude, i.longitude, self.longitude)
            # Ignore crimes without a home
            if i.latitude == 59.858143 and i.longitude == 17.644587:
                continue
            if i.date.hour < now.hour - 2 or i.date.hour > now.hour + 2:
                continue
            if distance < 200:
                crime_score = crime_score + self.calculate_crime_score(distance, i)
                pprint(vars(i))
                a = a +1 
                
        print("Num crimes %d") % (a)
        return crime_score

    def calculate_crime_score(self, distance, crime):
        crime_score = (200 - distance)/5
        
        if crime.date.year == 2012:
            crime_score = crime_score * 1.4
        elif crime.date.year == 2010:
            crime_score = crime_score * 0.8

        return crime_score

    def get_level(self, crime_score):
        if crime_score < 9:
            answer = 'TRADIGT'
            level = 'green'
            subtext = u'Zzz... Ingenting händer här inte. Till och med syrsorna hörs.'
        elif crime_score > 8 and crime_score < 19:
            answer = 'LUGNT'
            level = 'lime'
            subtext = u'Pfff... Det är lugnare än en filbunke. En lugn filbunke.'
        elif crime_score > 18 and crime_score < 29:
            answer = 'VANLIGT'
            level = 'yellow'
            subtext = u'Jaha, området är varken mer eller mindre farligt eller ofarligt.'
        elif crime_score > 28 and crime_score < 39:
            answer = 'PIRRIGT'
            level = 'orange'
            subtext = u'Oj! Nu gäller det att vara på sin vakt. Här kan det hända grejer.'
        else:
            answer = 'FARLIGT'
            level = 'red'
            subtext = u'Argh! Spring för glatta livet. Spring!'
        return (answer, subtext, level)
# Flogsta
my_lat = 59.84886
my_lon = 17.597866

# OG
my_lat = 59.855524
my_lon = 17.638807


