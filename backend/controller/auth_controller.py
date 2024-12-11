from flask import Blueprint, request, session
from helper.response import send_response
from helper.http_status_code import *
from service.auth_service import *
from helper.logger import log
import os
from datetime import datetime, timedelta


here = os.path.basename(__file__)
auth = Blueprint('auth', __name__)


@auth.route("/login", methods=['POST', 'GET'])
def auth_login():
    log(here, "New Login Request")
    if request.method == 'POST':
        body = request.get_json()
        if body is None:
            log(here, "Failed Login Request")
            return send_response(http_bad_request)

        user_obj = {
            'email': body.get("email"),
            'password': body.get("password")
        }
        user = login(user_obj)
    else:
        if not request.args.get("email") or not request.args.get("password"):
            return send_response(http_bad_request)

        user_obj = {
            'email': request.args.get("email"),
            'password': request.args.get("password")
        }
        user = login(user_obj)

    if not user:
        return send_response(http_internal_server_error)

    del user['password']
    token = generate_token(user_obj)
    response = send_response(http_ok, {"user": user, "token": token})
    response.set_cookie('token', token)
    session["access_token"] = token
    return response


@auth.route("/register", methods=['POST', 'GET'])
def auth_register():
    log(here, "New Register Request")
    if request.method == 'POST':
        body = request.get_json()
        if body is None:
            log(here, "Failed Register Request")
            return send_response(http_bad_request)

        user_obj = {
            'email': body.get("email"),
            'password': body.get("password"),
            'name': body.get("name"),
        }

        new_user = register(user_obj)
    else:
        if not request.args.get("email") or not request.args.get("password") or not request.args.get("name"):
            return send_response(http_bad_request)

        user_obj = {
            'email': request.args.get("email"),
            'password': request.args.get("password"),
            'name': request.args.get("name"),
        }
        new_user = register(user_obj)

    if not new_user:
        return send_response(http_internal_server_error)

    del new_user['password']
    token = generate_token(new_user)
    response = send_response(http_created, {'user': new_user, 'token': token})
    response.set_cookie('token', token)
    # session['access_token'] = token
    return response


@auth.route("/logout", methods=['POST', 'GET'])
def auth_logout():
    response = send_response(http_ok, 'Logged out successfully')
    response.delete_cookie('token')
    response.delete_cookie('session')

    return response


@auth.route("/test-cookie", methods=['GET', 'POST'])
def test_cookie():
    token = request.cookies.get('token')
    if not token:
        return send_response(http_not_found, 'cookie not found')

    parsed_token = decode_token(token)
    user_data = get_user_data_by_email(parsed_token.get('email'))
    if not user_data:
        return send_response(http_not_found)

    return send_response(http_ok, user_data)
