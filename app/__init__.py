from flask import Flask
from flask_navigation import Navigation

app = Flask(__name__)

nav = Navigation(app)

nav.Bar('top', [
    nav.Item('Home', 'index'),
    nav.Item('Flower fields', 'fields'),
    nav.Item('About', 'about'),
    nav.Item('Contact', 'contact')
])

from app import routes
