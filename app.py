from dining import *
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


@socketio.on('connect') 
def on_connect():
    print('Someone connected!')
    menu_data = models.menuItem.query.all()
    menu_list = []
    for item in menu_data:
        menu_list.append({
            'title' : item.Utitle,
            'averageRating' : item.Urating,
            'calories' : item.Unutrition,
            'reviews' : item.Ureviews,
            'time' : item.Utypes,
            'location' : item.Ulocation,
            'imageLink' : item.Uimage
        })
    
    socketio.emit('menu loaded' , {
        'menu_items': menu_list
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