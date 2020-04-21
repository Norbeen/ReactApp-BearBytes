import os, flask, flask_socketio, flask_sqlalchemy 

from google.oauth2 import id_token
from google.auth.transport import requests

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

app = flask.Flask(__name__)
socketio = flask_socketio.SocketIO(app=app, cors_allowed_origins='*')

import models 

@app.route('/')
def hello():
    return flask.render_template('index.html')

@app.route('/review')
def hi():
    return flask.render_template('index.html')

# Check the disconnect status

@socketio.on('disconnect')
def on_disconnect(data):
    socketio.emit('disconnecting', {
        'disconnect status': data["I am disconnecting"]
    })

#Check the connect status

@socketio.on('connect') 
def on_connected():
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
    
#Receive the food reveiws from client

@socketio.on('new review')
def on_new_review(data):
    print("Got an event for new message with data:", data)
    

# Declaring oogle Variables 

googleImage = ""
googleName = "" 
googleEmail = ""

#  #***********************  verification of the user signed in with the google *****************
@socketio.on('google token')
def google_information(token):
    
    print ("Got an event for GOOGLE TOKEN ID: "+ str(token['user_token']))
    
    try:
        CLIENT_ID = '120440974471-c3v5k5h966i0jdei02gmut1gar1l1ple.apps.googleusercontent.com'
        print(token['user_token'])
        idinfo = id_token.verify_oauth2_token(token['user_token'], requests.Request(), CLIENT_ID)
        print(idinfo['iss'])
    
        if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
            raise ValueError('Wrong issuer.')
            
        #**************** After verification getting the user id.     ************************
        userid = idinfo['sub']
        print(idinfo)
        
        # ***************** Declaring global variable for name and image extracted from google ********
       
        global googleImage
        googleImage= idinfo['picture']
        
        global googleName
        googleName = idinfo['name']
        
        global googleEmail
        googleEmail = idinfo['email']
    
    except ValueError:
        print("Invalid token")
        
# ***************************  Twilio SMS API  **********************************************************
    #     message = Mail(
    #     from_email='norbeen7@gmail.com',
    #     to_emails=googleEmail,
    #     subject='Sending with Twilio SendGrid is Fun',
    #     html_content='<strong>Testing email</strong>')
    # try:
    #     sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    #     response = sg.send(message)
    #     print(response.status_code)
    #     print(response.body)
    #     print(response.headers)
    # except Exception as e:
    #     print(e)

if __name__ == '__main__':
    socketio.run(
        app,
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', 8080)),
        debug=True
    )