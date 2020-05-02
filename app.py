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
            'imageLink' : bf_item.Uimage,
            "id": bf_item.id
            }) 
        
    for lunch_item in lunch_data:
        lunch_list.append({
            'title' : lunch_item.Utitle,
            'averageRating' : lunch_item.Urating,
            'calories' : lunch_item.Unutrition,
            'reviews' : lunch_item.Ureviews,
            'time' : lunch_item.Utypes,
            'location' : lunch_item.Ulocation,
            'imageLink' : lunch_item.Uimage,
            "id": lunch_item.id
            })
        
    for dinner_item in dinner_data:
        dinner_list.append({
            'title' : dinner_item.Utitle,
            'averageRating' : dinner_item.Urating,
            'calories' : dinner_item.Unutrition,
            'reviews' : dinner_item.Ureviews,
            'time' : dinner_item.Utypes,
            'location' : dinner_item.Ulocation,
            'imageLink' : dinner_item.Uimage,
            "id": dinner_item.id
        })
    
    models.db.session.commit()
    
    print("dinner", dinner_list, "\n")
    print("lunch", lunch_list, "\n")
    print("breakfast", breakfast_list, "\n")
    
    breakfast_list = sorted(breakfast_list, key = lambda i: i['id'])
    lunch_list = sorted(lunch_list, key = lambda i: i['id']) 
    dinner_list = sorted(dinner_list, key = lambda i: i['id']) 
    
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
        
        posted_data = models.reviewPost.query.filter_by(UmenuItemId=foodDetailsDict['id']).all()
        reviews_list = []
        for review in posted_data:
            reviews_list.append({
            'body' :review.Ucomment,
            'rating' : review.Urating,
            'category' : review.UmenuItemId,
            'likes' : review.Ulike,
            'dislikes' : review.Udislike,
            'username' : review.Uauthor,
            'profilePic' : review.Uimage,
            'date' : review.Udate,
            'id': review.id
                }) 
        
        newest_reviews_list = sorted(reviews_list, key = lambda i: i['id'],reverse=True) 
        negative_reviews_list = sorted(reviews_list, key = lambda i: i['dislikes'],reverse=True) 
        popular_reviews_list = sorted(reviews_list, key = lambda i: i['rating'],reverse=True) 
        positive_reviews_list = sorted(reviews_list, key = lambda i: i['likes'],reverse=True)
        socketio.emit('send review list', {
            'newest_reviews': newest_reviews_list,
            'popular_reviews': popular_reviews_list,
            'positive_reviews': positive_reviews_list,
            'negative_reviews': negative_reviews_list,
        })
        
        

@socketio.on('new like/disike')
def on_new_like(data):
    
    print("Got an event for like dislikes :", data)

    received_like = data["likes"]
    received_dislike= data["dislikes"]
    
    
    #add_item = models.reviewPost(received_comment, received_rating, received_category, received_like, received_dislike, googleName, googleImage, received_date)
    # models.db.session.add(add_item)
    # models.db.session.commit()
    # models.db.session.close()
    

@socketio.on('new review')
def on_new_review(data):
    print("Got an event for new message with data:", data)
    
    #TODO (priority #1): get all reviews for that specific food from the database and add it to review list

    #This scoketio will fetch rating, category, comment and date
    review = data['review']
    
    today = date.today()
    review['date'] = today.strftime("%m/%d/%y")
    
    rating = review['rating']
    comment = review['body']
    received_date = review['date']
    menu_item_id = review['foodId']
    likes = review["likes"]
    dislikes = review["dislikes"]
    username = review['user']['name']
    profile = review['user']['profilePic']
    
    
        
    
    add_review = models.reviewPost(comment, rating, menu_item_id, likes, dislikes, username, profile, received_date)
    models.db.session.add(add_review)
    models.db.session.flush()
    review['id'] = add_review.id
    print("added review", add_review)
    models.db.session.commit()
    models.db.session.close()
    
    review['username'] = username
    review['profilePic'] = profile
    print("id", review['id'])
    print("review emitted", review)
    socketio.emit('send review', {
            'review': review
        })
        
    # update average rating in Database
    menu_item = models.menuItem.query.filter_by(id=menu_item_id).all()[0]
    print(menu_item)
    reviews_for_item = models.reviewPost.query.filter_by(UmenuItemId=menu_item_id).all()
    rating_total = 0
    total = len(reviews_for_item)
    for review in reviews_for_item:
        rating_total += review.Urating

    menu_item.Urating = round(rating_total/total)
    print("rating updated", menu_item.Urating)
    models.db.session.add(menu_item)
    models.db.session.commit()
    models.db.session.close()

    

    
    
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