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


@socketio.on('connect') 
def on_connect():
    print('Someone connected!')
    breakfast_data = models.menuItem.query.filter_by(Utypes='breakfast').all()
    lunch_data = models.menuItem.query.filter_by(Utypes='lunch').all()
    dinner_data = models.menuItem.query.filter_by(Utypes='dinner').all()
    breakfast_list = []
    lunch_list = []
    dinner_list = []
    for bf_item in breakfast_data:
        breakfast_list.append({
            'bf_title' : bf_item.Utitle,
            'bf_averageRating' : bf_item.Urating,
            'bf_calories' : bf_item.Unutrition,
            'bf_reviews' : bf_item.Ureviews,
            'bf_time' : bf_item.Utypes,
            'bf_location' : bf_item.Ulocation,
            'bf_imageLink' : bf_item.Uimage
            }) 
    for lunch_item in lunch_data:
        lunch_list.append({
            'lunch_title' : lunch_item.Utitle,
            'lunch_averageRating' : lunch_item.Urating,
            'lunch_calories' : lunch_item.Unutrition,
            'lunch_reviews' : lunch_item.Ureviews,
            'lunch_time' : lunch_item.Utypes,
            'lunch_location' : lunch_item.Ulocation,
            'lunch_imageLink' : lunch_item.Uimage
            })
    for dinner_item in dinner_data:
            dinner_list.append({
            'din_title' : dinner_item.Utitle,
            'din_averageRating' : dinner_item.Urating,
            'din_calories' : dinner_item.Unutrition,
            'din_reviews' : dinner_item.Ureviews,
            'din_time' : dinner_item.Utypes,
            'din_location' : dinner_item.Ulocation,
            'din_imageLink' : dinner_item.Uimage
        })
    
    socketio.emit('menu loaded' , {
        'breakfast_items': breakfast_list,
        'lunch_items' : lunch_list,
        'dinner_items' : dinner_list
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