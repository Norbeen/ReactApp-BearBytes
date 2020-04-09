import os, flask, flask_socketio, flask_sqlalchemy 
from requests import *
#from google.oauth2 import id_token
#import google.auth.transport.requests
#from google.auth.transport import requests
#request = google.auth.transport.requests.Request()



app = flask.Flask(__name__)

socketio = flask_socketio.SocketIO(app)

import models 

@app.route('/')
def hello():
    return flask.render_template('index.html')
    
@app.route('/review')
def hi():
    return flask.render_template('index.html')

# json_list = combined_list()
# title_parsed =json_list[0]
# title_parsed =passed_list[0]
# calorie_parsed = passed_list[1]
# image_parsed = passed_list[2]

# socketio.emit('json_file', {'parsed_data': title_parsed})
@socketio.on('connect') 
def on_connect():
    #menu = models.menu.query.all()
    print('Someone connected!')
    
@socketio.on('load_menu')
def load_menu():
    socketio.emit('get_data', {
        'data' : menu 
    })
  
@socketio.on('disconnect')
def on_disconnect():
    print('Someone disconnected!')


if __name__ == '__main__':
    socketio.run(
        app,
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', 8080)),
        debug=True
    )