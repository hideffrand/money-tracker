from flask import Blueprint, request
from service.transaction_service import *
from helper.http_status_code import *
from helper.response import send_response
import datetime

transactions = Blueprint("transactions", __name__)


@transactions.route("/<int:user_id>", methods=["GET"])
def handle_get_transactions(user_id):
    res = get_transactions(user_id)
    if not res:
        return send_response(http_internal_server_error)

    return send_response(http_ok, res)


@transactions.route("/", methods=["POST"])
def handle_create_new_transaction():
    body = request.get_json()
    if not body:
        return send_response(http_bad_request)

    transaction_obj = {
        "type_id": body.get("type_id"),
        "user_id": body.get("user_id"),
        "description": body.get("description"),
        "title": body.get("title"),
        "amount": body.get("amount"),
        "datetime": datetime.datetime.now(),
    }

    res = add_transaction(transaction_obj)
    if not res:
        return send_response(http_internal_server_error)

    return send_response(http_ok, res)


@transactions.route("/", methods=["PUT"])
def handle_update_transaction():
    body = request.get_json()
    if not body:
        return send_response(http_bad_request)

    transaction_obj = {
        "transaction_id": body.get("transaction_id"),
        "type_id": body.get("type_id"),
        "description": body.get("description"),
        "title": body.get("title"),
        "amount": body.get("amount"),
        "user_id": body.get("user_id"),
    }
    res = update_transaction(transaction_obj)
    if not res:
        return send_response(http_internal_server_error)

    return send_response(http_ok, res)


@transactions.route("/<int:transaction_id>", methods=["DELETE"])
def handle_delete_transaction(transaction_id):
    res = delete_transaction(transaction_id)
    if not res:
        return send_response(http_internal_server_error)

    return send_response(http_ok, res)

@transactions.route("/<int:transaction_id>/date", methods=["GET"])
def handle_get_transaction_by_date(user_id):
    res = get_transaction_filter(user_id)
    if not res:
        return send_response(http_internal_server_error)

    return send_response(http_ok, res)


    