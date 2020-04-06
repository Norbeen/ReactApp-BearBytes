import os
import flask
from dining import *


app = flask.Flask(__name__)

@app.route('/')
def hello():
    return flask.render_template('index.html')

passed_list = combined_list()
title_parsed =passed_list[0]
calorie_parsed = passed_list[1]
image_parsed = passed_list[2]

print(image_parsed[0])

    

app.run(
    host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', 8080)),
    debug=True
)