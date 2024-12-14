from flask import Blueprint, request
from service.transaction_service import *
from helper.http_status_code import *
from helper.response import send_response
from datetime import datetime

transactions = Blueprint("transactions", __name__)


@transactions.route("/<int:user_id>", methods=["GET"])
def handle_get_transactions(user_id):
    # body = request.get_json()
    start_date = request.args.get("start_date")
    end_date = request.args.get("end_date")

    if start_date:
        try:
            start_date = datetime.strptime(start_date, "%Y-%m-%d")
        except ValueError:
            return send_response(http_bad_request, "Invalid start_date format. Use YYYY-MM-DD.")

    if end_date:
        try:
            end_date = datetime.strptime(end_date, "%Y-%m-%d")
        except ValueError:
            return send_response(http_bad_request, "Invalid end_date format. Use YYYY-MM-DD.")

    if start_date and end_date:
        res = get_transactions(user_id, start_date, end_date)
    else:
        res = get_transactions(user_id)

    log(here, f"hasil filter {res}")
    if not res:
        return send_response(http_ok, [])

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
        "datetime": datetime.now(),
    }

    res = add_transaction(transaction_obj)
    if not res:
        return send_response(http_internal_server_error)

    return send_response(http_ok, res)


@transactions.route("/update", methods=["POST"])
def handle_update_transaction():
    body = request.get_json()
    if not body:
        return send_response(http_bad_request)

    transaction_obj = {
        "transaction_id": body.get("transaction_id"), # coba liat terminal cko none
        "type_id": body.get("type_id"),
        "description": body.get("description"),
        "title": body.get("title"),
        "amount": body.get("amount"),
        "user_id": body.get("user_id"),
    }
    log(here, f'updating transaction {transaction_obj}')
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
