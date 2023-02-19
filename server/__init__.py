from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

#db = SQLAlchemy() #Initialize database
#app = Flask(__name__)
#app.config['UPLOAD_FOLDER'] = '/uploads'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://cred.db' #refer to the sql database locally with our app.py not sure if three / are needed so I am going with two for now
#db = SQLAlchemy(app)

#from app import routes, models