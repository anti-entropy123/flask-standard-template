from . import ws
from flask_socketio import SocketIO, emit

name_space = '/dcenter'

@ws.on('connect', namespace=name_space)
def connected_msg():
    print('client connected.')


@ws.on('disconnect', namespace=name_space)
def disconnect_msg():
    print('client disconnected.')


@ws.on('my_event', namespace=name_space)
def mtest_message(message):
    print(message)
    emit('my_response',
         {'data': message['data'], 'count': 1})
