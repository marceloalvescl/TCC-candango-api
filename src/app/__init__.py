from flask import Flask, session
from flask_login import LoginManager, login_manager
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy 
from flask_cors import CORS
from utils.constants import DB_SCHEMA, DB_CREDENTIALS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://{0}:{1}@{2}/{3}'.format(
                                        DB_CREDENTIALS['DatabaseUser'],
                                        DB_CREDENTIALS['DatabasePassword'],
                                        DB_CREDENTIALS['DatabaseHost'],
                                        DB_CREDENTIALS['DatabaseName'])
SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
CORS(app, automatic_options=True)
Session(app)
login_manager = LoginManager(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


#Esse import é realizado após o login_manager ser executado para evitar erro de circular import
from views.routes import candango_routes
app.register_blueprint(candango_routes)