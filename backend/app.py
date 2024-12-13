from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from helper.http_status_code import *
from helper.response import send_response
from model import db
from controller.auth_controller import auth
from controller.transaction_controller import transactions
from controller.type_controller import types
from service.auth_service import generate_mock_user
from service.type_service import generate_mock_type
from service.transaction_service import generate_mock_transaction
import os

load_dotenv()
here = os.path.basename(__file__)
app = Flask(__name__)
CORS(app,
     origins=["http://localhost:5173", "http://localhost:5174", "http://localhost:5175",
              "https://p9jctgvq-5173.asse.devtunnels.ms"],
     methods=["GET", "POST", "PUT", "PATCH", "DELETE"]
     )


# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:cbOiysfVpBZVvQUbHjhNsMyZZWXJaPvK@junction.proxy.rlwy.net:44512/railway'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres.cxsnfjtvayxqgffdtife:NHMLf69iaXuC9zOg@aws-0-ap-southeast-1.pooler.supabase.com:6543/postgres'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/money_tracker'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = os.getenv('SECRET_KEY')

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/api", methods=["GET"])
def index():
    return send_response(http_ok, 'ok')


@app.route("/api/generate-mock", methods=["GET"])
def generate_mock():
    generate_mock_user()
    generate_mock_type()
    generate_mock_transaction()
    return send_response(http_ok, 'Mock Generated, User: coba@gmail.com')


app.register_blueprint(auth, url_prefix='/api/auth')
app.register_blueprint(transactions, url_prefix='/api/transactions')
app.register_blueprint(types, url_prefix='/api/types')


if __name__ == '__main__':
    app.run(debug=True)
