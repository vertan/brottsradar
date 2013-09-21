#!venv/bin/python
import sys
sys.path.append('../')

from app import app
app.run(debug = True)
