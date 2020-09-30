from flask import render_template, url_for
from . import main

@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')