from model import *
from helper.http_status_code import *
from helper.logger import log
import os


here = os.path.basename(__file__)


def get_types_by_user(user_id):
    data = Type.query.filter_by(user_id=user_id).all()

    if not data:
        return False

    return [t.to_json() for t in data]


def add_type(type_obj):
    if not type_obj:
        return False
    log(here, f"adding type: {type_obj["type_name"]} as type name with {type_obj["budget"]} as budget")

    new_type = Type(user_id=type_obj["user_id"],
                    type_description=type_obj["type_description"],
                    type_name=type_obj["type_name"],
                    budget=type_obj["budget"])

    db.session.add(new_type)
    db.session.commit()
    log(here, "New Type Created!")
    return True


def delete_type(type_id):
    log(here, f"deleting type {type_id}")
    Type.query.filter_by(id=type_id).delete()
    db.session.commit()
    return True

def change_type_budget(type_id, new_budget):
    log(here, f"changing type {type_id} budget to {new_budget}")
    type = Type.query.filter_by(id=type_id).first()
    type.budget = new_budget
    db.session.commit()
    return True
