import smtplib
import os, flask, flask_socketio

# ********************************** Script to send email with the link *********************************************

# Send email upon successful login with google 

def message_sent(googleName, googleEmail): 
    
    try:
        subject= 'Save this link to checkout our website!!'
        msg = 'Dear ' + str(googleName) + ', '+  '\n\nPlease checkout the morgan dining website to see what is being served today. \n\nhttp://bear-bites.herokuapp.com/\n\n Thank you!'
        server =smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        
        # This EMAIL AND PASS is an environment variable already setup in heroku, for testing use your email and pass as string 
        
        server.login(EMAIL, PASS)
        message = 'Subject:{}\n\n{}'.format(subject,msg)
        server.sendmail(googleEmail, googleEmail,message)
        server.quit()
        print("email sent successfully")
    except:
        print("email failed to send")

        
def user_name(name, email):
    return name
    
def user_email(name, email):
    return email

def user_loggedIn(user_status):
    return user_status
    