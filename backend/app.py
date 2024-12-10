from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from helper.http_status_code import *
from helper.response import send_response
from model import db
from controller.auth_controller import auth
import os

load_dotenv()
here = os.path.basename(__file__)
app = Flask(__name__)
CORS(app)


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:cbOiysfVpBZVvQUbHjhNsMyZZWXJaPvK@junction.proxy.rlwy.net:44512/railway'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres.cxsnfjtvayxqgffdtife:NHMLf69iaXuC9zOg@aws-0-ap-southeast-1.pooler.supabase.com:6543/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = os.getenv('SECRET_KEY')

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/api", methods=["GET"])
def index():
    return send_response(http_ok, 'ok')


app.register_blueprint(auth, url_prefix='/api/auth')


if __name__ == '__main__':
    app.run(debug=True)
