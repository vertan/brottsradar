from app import db

class Crime(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    place = db.Column(db.String)
    date = db.Column(db.DateTime, index = True)
    longitude = db.Column(db.Float, index = True)
    latitude = db.Column(db.Float, index = True)

