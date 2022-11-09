import os
import sqlite3
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from flask_migrate import Migrate
from flask_cors import CORS
import cloudinary
from schemas import db
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager


from routes.main import bpMain
from routes.routes import bpPeople, bpUser, bpPlanets, bpFav_Planets, bpFav_Char

load_dotenv()

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['DEBUG'] = True
app.config['ENV'] = 'development'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////workspace/base-workspace-mysql/StarWars.db"
#db = SQLAlchemy(app)
app.config['CORS_HEADERS'] = 'Content-Type'

db.init_app(app)
Migrate(app, db)
jwt = JWTManager(app)
CORS(app)

# cloudinary.config(
#     cloud_name = os.getenv('CLOUDINARY_CLOUD_NAME'),
#     api_key = os.getenv('CLOUDINARY_API_KEY'),
#     api_secret = os.getenv('CLOUDINARY_API_SECRET'),
#     secure = True
# )

app.register_blueprint(bpMain)
app.register_blueprint(bpUser, url_prefix='/api')
app.register_blueprint(bpPeople, url_prefix='/api')
app.register_blueprint(bpPlanets, url_prefix='/api')
app.register_blueprint(bpFav_Char, url_prefix='/api')
app.register_blueprint(bpFav_Planets, url_prefix='/api')

if __name__ == '__main__':
    app.run()