from model import *
from helper.http_status_code import *
from helper.logger import log
import os
import datetime

here = os.path.basename(__file__)


def get_transactions(user_id):
    types = Type.query.filter_by(user_id=user_id).all()
    if not types:
        return False
    types = [t.to_json() for t in types]

    transactions = Transaction.query.filter_by(user_id=user_id).all()
    if not transactions:
        return False
    transactions = [transaction.to_json() for transaction in transactions]

    result_obj = {}
    for user_type in types:
        result_obj[user_type["type_id"]] = []

    for transaction in transactions:
        result_obj[transaction["type_id"]].append(transaction)

    # return transactions
    return result_obj


def add_transaction(object):
    if not object:
        return False
    log(here,
        f"adding transaction on type: {object['type_id']}, amount spent: {object['amount']} ")
    new_transaction = Transaction(user_id=object["user_id"],
                                  type_id=object["type_id"],
                                  amount=object["amount"],
                                  title=object["title"],
                                  description=object["description"],
                                  datetime=object["datetime"]
                                  )
    db.session.add(new_transaction)
    db.session.commit()
    return True


def delete_transaction(transaction_id):
    if not transaction_id:
        return False

    res = Transaction.query.filter_by(
        transaction_id=transaction_id).delete()
    db.session.commit()
    return True


def update_transaction(transaction_obj):
    if not transaction_obj:
        log(here, "Transaction not found")
        return False
    transaction = Transaction.query.filter_by(
        transaction_id=transaction_obj["transaction_id"]).first()

    if not transaction:
        log(here, "Transaction not found")
        return False

    transaction.user_id = transaction_obj["user_id"]
    transaction.type_id = transaction_obj["type_id"]
    transaction.amount = transaction_obj["amount"]
    transaction.title = transaction_obj["title"]
    transaction.description = transaction_obj["description"]

    db.session.commit()
    return True


def generate_mock_transaction():
    coba_user = User.query.filter_by(name='coba').first()
    coba_user = coba_user.to_json()

    type_makanan = Type.query.filter_by(
        user_id=coba_user["user_id"], description='Makanan').first()
    type_makanan = type_makanan.to_json()
    type_entertainment = Type.query.filter_by(
        user_id=coba_user["user_id"], description='Entertainment').first()
    type_entertainment = type_entertainment.to_json()
    type_hobby = Type.query.filter_by(
        user_id=coba_user["user_id"], description='Hobby').first()
    type_hobby = type_hobby.to_json()

    makanan_transactions = [
        Transaction(user_id=coba_user["user_id"],
                    type_id=type_makanan["type_id"],
                    amount=20_0000,
                    title="Soto tangkar",
                    description="Soto tangkar + kerupuk",
                    datetime=datetime.datetime.now()
                    ),
        Transaction(user_id=coba_user["user_id"],
                    type_id=type_makanan["type_id"],
                    amount=5_0000,
                    title="Es Teh Markisa",
                    description="es teh pake nutrisari markisa",
                    datetime=datetime.datetime.now()
                    ),
        Transaction(user_id=coba_user["user_id"],
                    type_id=type_makanan["type_id"],
                    amount=15_0000,
                    title="Warteg",
                    description="Nasi tongkol balado",
                    datetime=datetime.datetime.now()
                    )
    ]
    hobby_transactions = [
        Transaction(user_id=coba_user["user_id"],
                    type_id=type_hobby["type_id"],
                    amount=159_000,
                    title="BLOKEES Transformer",
                    description="Optimus primal",
                    datetime=datetime.datetime.now()
                    ),
        Transaction(user_id=coba_user["user_id"],
                    type_id=type_hobby["type_id"],
                    amount=25_0000,
                    title="Top Up COC",
                    description="Diskon event christmas",
                    datetime=datetime.datetime.now()
                    )
    ]
    entertainment_transactions = [
        Transaction(user_id=coba_user["user_id"],
                    type_id=type_entertainment["type_id"],
                    amount=49_0000,
                    title="Nonton Moana 2",
                    description="Nonton moana sebelum teau",
                    datetime=datetime.datetime.now()
                    ),
    ]

    new_transactions = makanan_transactions + \
        hobby_transactions + entertainment_transactions
    for transaction in new_transactions:
        db.session.add(transaction)
        db.session.commit()

def get_transaction_filter(user_id):
    types = Type.query.filter_by(user_id=user_id).all()
    if not types:
        return False
    types = [t.to_json() for t in types]

    transactions = Transaction.query.filter_by(user_id = user_id).order_by(Transaction.datetime.desc()).all()
    if not transactions:
        return False
    transactions = [transaction.to_json() for transaction in transactions]

    
    result_obj = {}
    for user_type in types:
        result_obj[user_type["type_id"]] = []

    for transaction in transactions:
        result_obj[transaction["type_id"]].append(transaction)

    return result_obj