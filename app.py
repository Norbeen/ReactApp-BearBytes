import os, flask, flask_socketio, flask_sqlalchemy,smtplib, json

from google.oauth2 import id_token
from google.auth.transport import requests
import send_sms as send
from datetime import date


app = flask.Flask(__name__)
socketio = flask_socketio.SocketIO(app=app, cors_allowed_origins='*')

import models 

@app.route('/')
def hello():
    return flask.render_template('index.html')

@app.route('/review')
def hi():
    return flask.render_template('index.html')

#Check the disconnect status

@socketio.on('disconnect')
def on_disconnect(data):
    socketio.emit('disconnecting', {
        'disconnect status': True
    })



@socketio.on('connect') 
def on_connected():
    print("somebody connected")
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
    
#Receive the food reveiws from client

@socketio.on('new review')
def on_new_review(data):
    print("Got an event for new message with data:", data)
    #TODO: get all reviews for that specific food from the database and add it to review list
    # data['review']['foodTitle'] gets you the title of the food that was reviewed
    #ReviewObject.jsx file should show the atrributes of a review object
    reviews_list = []

    today = date.today()
    data['review']['date'] = today.strftime("%m/%d/%y")
    reviews_list.append(data['review'])
    #TODO: save that new review to the database
    socketio.emit('send review', {
        'review': reviews_list
    })
    
@socketio.on('rating')
def on_new_rating(data):
    print("Got an event for new message with data:", data)
    socketio.emit('review rating' , {
        'rating': data['rating']
    })
    

# Declaring oogle Variables 

googleImage = ""
googleName = "" 
googleEmail = ""
canSendSms= False

#  #***********************  verification of the user signed in with the google *****************
@socketio.on('google token')
def google_information(token):
    print ("Got an event for GOOGLE TOKEN ID: "+ str(token['user_token']))
    
    #**************** After verification getting the user id.     ************************
    if is_valid_token(token['user_token']):
        idinfo = is_valid_token(token['user_token'])
        userid = idinfo['sub']
        print(idinfo)
        
        # ***************** Declaring global variable for name and image extracted from google ********
        googleImage= idinfo['picture']
        googleFirstName = idinfo['given_name']
        
        global googleName
        googleName = idinfo['name']
        
        
        
        global googleEmail
        googleEmail = idinfo['email']
        
        global canSendSms 
        canSendSms= True
    
        socketio.emit('logged in' , {
            'user':{ 
                "name": googleFirstName,
                "profilePic": googleImage
                }
        })
    
    if (canSendSms):
        send.message_sent(googleName, googleEmail)
    else:
        print("Error sending email")


def is_valid_token(token):
    try:
        # Specify the CLIENT_ID of the app that accesses the backend:
        CLIENT_ID = '120440974471-c3v5k5h966i0jdei02gmut1gar1l1ple.apps.googleusercontent.com'
        idinfo = id_token.verify_oauth2_token(token, requests.Request(), CLIENT_ID)
        print("id info:",idinfo['iss'])
        if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
            raise ValueError('Wrong issuer.')
        return idinfo

    except ValueError:
        if token == os.getenv('dummy_token'):
            return True
        print('Invalid token')
        return False

if __name__ == '__main__':
    socketio.run(
        app,
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', 8080)),
        debug=True
    )