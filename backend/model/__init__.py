from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "user"

    user_id = db.Column('user_id', db.Integer(),
                        primary_key=True, autoincrement=True)
    email = db.Column('email', db.String(150), unique=True, nullable=False)
    password = db.Column('password', db.String(100), nullable=False)
    name = db.Column('username', db.String(100), nullable=False)

    def __init__(self, email, password, name):
        # self.user_id = user_id
        self.email = email
        self.password = password
        self.name = name

    def to_json(self):
        return {
            "user_id": self.user_id,
            "email": self.email,
            "password": self.password,
            "name": self.name,
        }


class Type(db.Model):
    __tablename__ = "type"

    type_id = db.Column('type_id', db.Integer(),
                        primary_key=True, autoincrement=True)
    user_id = db.Column('user_id', db.Integer(), db.ForeignKey('user.user_id'))
    description = db.Column('description', db.String(100), nullable=False)
    budget = db.Column('budget', db.Integer(), nullable=False)
    checked = db.Column('checked', db.Boolean(), nullable=False, default=True)

    def __init__(self, user_id, description, budget):
        # self.type_id = type_id
        self.user_id = user_id
        self.description = description
        self.budget = budget

    def to_json(self):
        return {
            "type_id": self.type_id,
            "user_id": self.user_id,
            "description": self.description,
            "budget": self.budget,
            "checked": self.checked
        }


class Transaction(db.Model):
    __tablename__ = "transaction"

    transaction_id = db.Column(
        'transaction_id', db.Integer(), primary_key=True, autoincrement=True)
    type_id = db.Column('type_id', db.Integer(), db.ForeignKey('type.type_id'))
    user_id = db.Column('user_id', db.Integer(), db.ForeignKey('user.user_id'))
    title = db.Column('title', db.String(100), nullable=False)
    description = db.Column('description', db.String(100), nullable=False)
    amount = db.Column('amount', db.Integer(), nullable=False)
    datetime = db.Column('datetime', db.DateTime(timezone=True),
                         nullable=False, server_default=func.now())
    
    # harusnya ini udh bener V
    # created_at = db.Column(db.DateTime(timezone=True),
    #                        server_default=func.now())

    def __init__(self, type_id, user_id, description, amount, title, datetime):
        # self.transaction_id = transaction_id
        self.type_id = type_id
        self.user_id = user_id
        self.title = title
        self.description = description
        self.amount = amount
        self.datetime = datetime

    def to_json(self):
        return {
            "transaction_id": self.transaction_id,
            "type_id": self.type_id,
            "user_id": self.user_id,
            "title": self.title,
            "description": self.description,
            "amount": self.amount,
            "datetime": self.datetime
        }
