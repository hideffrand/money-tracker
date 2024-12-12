from sqlalchemy import func
from model import *
from helper.http_status_code import *
from helper.logger import log
import os


here = os.path.basename(__file__)


def get_types_by_user(user_id):
    data = Type.query.filter_by(user_id=user_id).all()

    if not data:
        return False

    data = [d.to_json() for d in data]

    for t_type in data:
        total_used = db.session.query(func.sum(Transaction.amount))\
                               .filter_by(user_id=user_id, type_id=t_type['type_id'])\
                               .scalar() or 0

        t_type['total_used'] = int(total_used)

    return data


def add_type(type_obj):
    if not type_obj:
        return False
    log(here,
        f"adding type: {type_obj['description']} as type name with {type_obj['budget']} as budget")

    new_type = Type(user_id=type_obj["user_id"],
                    description=type_obj["description"],
                    budget=type_obj["budget"])

    db.session.add(new_type)
    db.session.commit()
    log(here, "New Type Created!")
    return True


def delete_type(type_id):
    log(here, f"deleting type {type_id}")
    if not type_id:
        return False
    Type.query.filter_by(id=type_id).delete()
    db.session.commit()
    return True


def change_type_budget(type_id, new_budget):
    log(here, f"changing type {type_id} budget to {new_budget}")
    selected_type = Type.query.filter_by(id=type_id).first()
    if not selected_type:
        return False

    selected_type.budget = new_budget
    db.session.commit()
    return True


def change_type_description(type_id, new_desc):
    log(here, f"changing type {type_id} description to {new_desc}")
    selected_type = Type.query.filter_by(id=type_id).first()
    if not selected_type:
        return False

    selected_type.budget = new_desc
    db.session.commit()
    return True


def generate_mock_type():
    coba_user = User.query.filter_by(name='coba').first()
    coba_user = coba_user.to_json()

    new_types = [
        Type(user_id=coba_user["user_id"],
             description="Makanan",
             budget=500_000),
        Type(user_id=coba_user["user_id"],
             description="Entertainment",
             budget=200_000),
        Type(user_id=coba_user["user_id"],
             description="Hobby",
             budget=300_000),
    ]
    for t in new_types:
        db.session.add(t)
        db.session.commit()
