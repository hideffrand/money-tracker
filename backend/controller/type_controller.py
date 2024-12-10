from flask import Blueprint, request
from helper.response import send_response
from helper.http_status_code import *
from service.type_service import *
types = Blueprint("types", __name__)


@types.route("/<string:user_id>", methods=["GET"])
def handle_get_all_types_by_user(user_id):
    data = get_types_by_user(user_id)
    if not data:
        return send_response(http_not_found)

    return send_response(http_ok, data)


@types.route("/", methods=["POST"])
def handle_post_type():
    body = request.get_json()
    if not body:
        return send_response(http_bad_request)

    type_obj = {
        "user_id": body["user_id"],
        "type_description": body["type_description"],
        "type_name": body["type_name"],
        "budget": body["budget"],
    }

    result = add_type(type_obj)

    if not result:
        return send_response(http_bad_request)

    return send_response(http_ok)