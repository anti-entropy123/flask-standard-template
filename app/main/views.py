from flask import render_template, url_for
from . import main
from ..ws import ws

name_space = '/dcenter'

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/push')
def push_once():
    event_name = 'has_message'
    broadcasted_data = {'data': "test message!"}
    ws.emit(event_name, broadcasted_data, broadcast=False, namespace=name_space)
    return 'done!'

