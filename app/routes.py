from flask import render_template
from app import app
import json


flowerfields = json.load(open("fields.json", "r"))["features"]


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')


@app.route('/fields')
def fields():
    return render_template('fields.html', title='Explore the flower fields', flowerfields=flowerfields)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact')
