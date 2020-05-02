import os, flask, flask_socketio, flask_sqlalchemy,smtplib, json

from google.oauth2 import id_token
from google.auth.transport import requests
import send_sms as send
from datetime import date


app = flask.Flask(__name__)
socketio = flask_socketio.SocketIO(app=app, cors_allowed_origins='*')

import models 

global foodDetailsDict
foodDetailsDict = None

@app.route('/')
def hello():
    return flask.render_template('index.html')

@app.route('/review')
def hi():
    return flask.render_template('index.html')

@socketio.on('connect') 
def on_connected():
    print("somebody connected")
    global foodDetailsDict
    breakfast_data = models.menuItem.query.filter_by(Utypes='breakfast').all()
    lunch_data = models.menuItem.query.filter_by(Utypes='lunch').all()
    dinner_data = models.menuItem.query.filter_by(Utypes='dinner').all()
    breakfast_list = []
    lunch_list = []
    dinner_list = []
    for bf_item in breakfast_data:
        breakfast_list.append({
            'title' : bf_item.Utitle,
            'averageRating' : bf_item.Urating,
            'calories' : bf_item.Unutrition,
            'reviews' : bf_item.Ureviews,
            'time' : bf_item.Utypes,
            'location' : bf_item.Ulocation,
            'imageLink' : bf_item.Uimage
            }) 
    for lunch_item in lunch_data:
        lunch_list.append({
            'title' : lunch_item.Utitle,
            'averageRating' : lunch_item.Urating,
            'calories' : lunch_item.Unutrition,
            'reviews' : lunch_item.Ureviews,
            'time' : lunch_item.Utypes,
            'location' : lunch_item.Ulocation,
            'imageLink' : lunch_item.Uimage
            })
    for dinner_item in dinner_data:
            dinner_list.append({
            'title' : dinner_item.Utitle,
            'averageRating' : dinner_item.Urating,
            'calories' : dinner_item.Unutrition,
            'reviews' : dinner_item.Ureviews,
            'time' : dinner_item.Utypes,
            'location' : dinner_item.Ulocation,
            'imageLink' : dinner_item.Uimage
        })
    
    print("dinner", dinner_list, "\n")
    print("lunch", lunch_list, "\n")
    print("breakfast", breakfast_list, "\n")
    
    socketio.emit('menu loaded' , {
        'breakfast_items': breakfast_list,
        'lunch_items' : lunch_list,
        'dinner_items' : dinner_list
    })
    if foodDetailsDict:
        socketio.emit('menu item' , {
        'menu_item': foodDetailsDict
        })  
        print("food details dict", foodDetailsDict)
        
    
# ******************************.  This part receives the like, dislikes, I made everything global to use for all methods ******************************
    
#Receive the food reveiws from client

#declaring global variables for likes, dislikes and food title

received_foodTitle =""
received_category =""
received_comment =""
received_rating= ""
received_date = ""
received_foodTitle = ""
#Receive the food reveiws from client

@socketio.on('new like/disike')
def on_new_like(data):
    
    print("Got an event for like dislikes :", data)

    received_like = data["likes"]
    received_dislike= data["dislikes"]
    
    
    add_item = models.reviewPost(received_comment, received_rating, received_category, received_like, received_dislike, googleName, googleImage, received_date, received_foodTitle)
    models.db.session.add(add_item)
    models.db.session.commit()
    models.db.session.close()
    
    #This is the title to be received from client
    
    
    # global received_foodTitle
    # # received_foodTitle = data['foodTitle']

# ********************************* This part adds the comments and other stuff reviewPost database needs  ***************************************


@socketio.on('new review')
def on_new_review(data):
    print("Got an event for new message with data:", data)
    
#TODO (priority #1): get all reviews for that specific food from the database and add it to review list

#This scoketio will fetch rating, category, comment and date

    today = date.today()
    data['review']['date'] = today.strftime("%m/%d/%y")
    
    global received_rating
    received_rating = data['review']['rating']
    print(received_rating)
    global received_comment
    received_comment = data['review']['body']
    print(received_comment)
    global received_date
    received_date = data['review']['date']
    print(received_date)
    
#Lookup the database for category
#The Utitle equals received_foodTitle from line 88 once it is fetched from client
    fetch_data = models.menuItem.query.filter_by(Utitle='Pork Bacon').limit(1).all()

    for item in fetch_data:
        global received_category
        received_category = item.Utypes
        
    
    add_item = models.reviewPost(received_comment, received_rating, received_category, 0, 0, googleName, googleImage, received_date, 'Pork Bacon')
    models.db.session.add(add_item)
    models.db.session.commit()
    models.db.session.close()
    
    
    posted_data = models.reviewPost.query.filter_by(UfoodTitle='Pork Bacon').all()
    print("$$$$$$$$$$$$$$$$")
    print(posted_data)
    print("$$$$$$$$$$$$$$$$")
    
    # updated_database = models.menuItem.query.filter_by(Utitle= item_name).all()
    # for i in updated_database:
    #     print(i)
    # print(updated_database)
    
    #TODO (priority #1): get all reviews for that specific food from the database and add it to review list
    # data['review']['foodTitle'] gets you the title of the food that was reviewed
    #ReviewObject.jsx file should show the atrributes of a review object
    #TODO (priority #3): create separate lists sorted by date, likes, stars and dislikes
    
    #negative_reviews_list = []
    #popular_reviews_list = []
    #positive_reviews_list = []
    
    newest_reviews_list = []
    for review in posted_data:
        newest_reviews_list.append({
        'comment' :review.Ucomment,
        'rating' : review.Urating,
        'category' : review.Ucategory,
        'like' : review.Ulike,
        'dislike' : review.Udislike,
        'author' : review.Uauthor,
        'image' : review.Uimage,
        'date' : review.Udate,
        'foodTitle' : review.UfoodTitle
            })    
    print(newest_reviews_list)
    # newest_reviews_list.append(data['review'])
    #TODO (priority #2): save that new review to the database
    socketio.emit('send review', {
        'newest_reviews': newest_reviews_list,
        'popular_reviews': newest_reviews_list,
        'positive_reviews': newest_reviews_list,
        'negative_reviews': newest_reviews_list,
    })
    
@socketio.on('rating')
def on_new_rating(data):
    print("Got an event for new message with data:", data)
    socketio.emit('review rating' , {
        'rating': data['rating']
    })
 
@socketio.on('send to reviews')
def on_new_menu_click(data):
    global foodDetailsDict
    foodDetailsDict = data['food']
    print("Got an event for new message with data:", data)
    print("update global variable", foodDetailsDict)


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
        
        global googleName
        googleName = idinfo['name']
        
        global googleEmail
        googleEmail = idinfo['email']
        
        global canSendSms 
        canSendSms= True
    
        socketio.emit('logged in' , {
            'user':{ 
                "name": googleName,
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
        
#Check the disconnect status

@socketio.on('disconnect')
def on_disconnect(data):
    socketio.emit('disconnecting', {
        'disconnect status': True
    })

if __name__ == '__main__':
    socketio.run(
        app,
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', 8080)),
        debug=True
    )