#!venv/bin/python
# -*- coding: utf-8 -*-

from flask import render_template, request
from app import app, distance_calculation

@app.route('/')
@app.route('/index')
def index():
    title = u"Är det säkert att gå ut?"
    answer = 'FARLIGT'
    level = 'red'
    return render_template('index.html',
                           title = title,
                           answer = answer,
                           level = level)

@app.route('/status')
def status():
    longitude = request.args['longitude']
    latitude = request.args['latitude']
    if longitude == "e":
        # Do a geoip
        crime_score = 0
    else:
        location = distance_calculation.DistanceCalculator(latitude, longitude)
        crime_score = location.find_crimes()

    title = u"Är det säkert att gå ut?"

    return render_template('status.html',
                           title = title,
                           answer = answer,
                           level = level)

