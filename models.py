import os, flask_sqlalchemy, app

# app.app = app modules app variable
app.app.config['SQLALCHEMY_DATABASE_URI']  = os.getenv('DATABASE_URL')
# app.app.config['SQLALCHEMY_DATABASE_URI']  = 'postgresql://uname:pass@localhost/postgres'
db = flask_sqlalchemy.SQLAlchemy(app.app)

class menu(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    Utitle = db.Column(db.String(30))
    Urating = db.Column(db.Integer(300))
    Unutrition = db.Column(db.String(300))
    Ureviews= db.Column(db.Integer(300))
    Utypes = db.Column(db.String(300))
    Ulocation = db.Column(db.String(300))
    Uimage = db.Column(db.String(300))
    
    
    def __init__(self, name, rating, nutrition, reviews, types, location, image): 
        self.Utitle = name
        self.Urating = rating
        self.Unutrition = image
        self.Ureviews = reviews
        self.Utypes = types
        self.Ulocation = location
        self.Uimage = image
        
    def __repr__(self):
        # return '<Message user_name: %s>' % self.user_name
        return "{'food title':'%s', 'food rating':'%s', 'food nutrition':'%s', 'food reviews':'%s', 'food types':'%s', 'food location':'%s', 'food image':'%s'}" % (self.Utitle, self.Urating, self.Unutrition, self.Ureviews, self.Utypes, self.Ulocation,self.Uimage )