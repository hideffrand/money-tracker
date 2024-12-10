import jwt
from datetime import datetime, timedelta, timezone
from helper.http_status_code import *
from helper.logger import log
from model import db, User
import bcrypt
import os


here = os.path.basename(__file__)
VERY_SECRET_KEY = 'VERY_SECRET_KEY'


def generate_token(user):
    payload = {
        'sub': user['email'],
        'iat': datetime.now(timezone.utc),
        'exp': datetime.now(timezone.utc) + timedelta(hours=12)
    }
    token = jwt.encode(payload, VERY_SECRET_KEY, algorithm='HS256')

    return token


def decode_token(token):
    decoded_token = jwt.decode(token, VERY_SECRET_KEY, algorithms=['HS256'])
    if not decoded_token:
        return False

    return decoded_token


def hash_password(plain_text_password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(plain_text_password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')


def register(user_obj):
    log(here, f"Registering user {user_obj['email']}...")

    hashed_password = hash_password(user_obj["password"])

    """"
    ini dibawah masih dummy
    """
    new_user = User(
        # user_id='MOCK_ID',
        email=user_obj["email"],
        password=hashed_password,
        name=user_obj["name"],
    )

    db.session.add(new_user)
    db.session.commit()
    log(here, "New User Created!")

    user = User.query.filter_by(email=user_obj['email']).first()
    if not user:
        return False

    return user.to_json()


def login(user_obj):
    log(here, f"User {user_obj['email']} logging in...")

    user = User.query.filter_by(email=user_obj['email']).first()

    if not user:
        log(here, "Login Failed: User not found")
        return False

    if not bcrypt.checkpw(user_obj['password'].encode('utf-8'), user.password.encode('utf-8')):
        log(here, "Login Failed: Incorrect password")
        return False

    log(here, "Login Success")
    return user.to_json()
