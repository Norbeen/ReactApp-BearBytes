from dining import *
import os, flask, flask_socketio, flask_sqlalchemy 
from requests import *
import models
from google.oauth2 import id_token
import google.auth.transport.requests
from google.auth.transport import requests
request = google.auth.transport.requests.Request()



app = flask.Flask(__name__)

socketio = flask_socketio.SocketIO(app)

@app.route('/')

def hello():
    return flask.render_template('index.html')

# json_list = combined_list()
# title_parsed =json_list[0]
# title_parsed =passed_list[0]
# calorie_parsed = passed_list[1]
# image_parsed = passed_list[2]

# socketio.emit('json_file', {'parsed_data': title_parsed})
@socketio.on('connect') 
def on_connect():
    print('Someone connected!') 

''' This will fetch the reviews posted by the students

    for this method to work, need the name, rating, nutrition, reviews, types, location, image
    a. name after google signin
    b. rating after user gives rating
    c. nutrition, from the calorie list 
    d. reviews, comment left by student
    e. types, if it's breakfast/launch / dinner
    f. location, where it belongs to, cafetaria or dining
    g. image, fetched after google signin
    
'''


@socketio.on('student_review')
def on_received_review(data):
  
    grabbedReview  = data['user_message']
  
    # Checking response for the bot.
    if grabbedMessage[:2]=="!!":
        
        global googleName
        showName = Bot(googleName, grabbedMessage )[0]
        showMessage = Bot(googleName, grabbedMessage )[1]
        
        print("#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print(showName)
        print(showMessage)
    else:
        showName = googleName
        showMessage = grabbedMessage
        

    review = models.(showName,showMessage,googleImage)
    models.db.session.add(message)
    models.db.session.commit()
    chatLog = [] 
    
#     # Retrieving the data from database
    database_messages = models.chatMessage.query.all()
    
    
    print("Stored Messages:", database_messages)
    
    for i in database_messages:
        
        name = i.Uname
        message = i.Umessage
        image = i.Uimage
        
# # # #   #****************************** Validating if the message is URL or NO url ***********************
        url = validateUrl(message)[0]
        non_url = validateUrl(message)[1]
    

# # # #   #Appending the google name, url/url message and the image
  
        
        display_list = [name, url, non_url, image]
        chatLog.append(display_list)


    socketio.emit('push to server', {'database_list': chatLog});
    
socketio.run(
    app,
    host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', 8080)),
    debug=True
 )