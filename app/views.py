#!venv/bin/python
# -*- coding: utf-8 -*-

from flask import render_template
from app import app 

@app.route('/')
@app.route('/index')
def index():
    title = u"Är det säkert att gå ut?"
    answer = 'hide yo wife, hide yo kids'
    return render_template('index.html',
                           title = title,
                           answer = answer);
