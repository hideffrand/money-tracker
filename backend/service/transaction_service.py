from model import *

def get_transaction_by_user(user_id):
    data = Transaction.query.get(user_id =user_id).all()
    if not data:
        return False

    return [t.to_json() for t in data]


