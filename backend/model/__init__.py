from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "user"

    user_id = db.Column('user_id', db.String(10), primary_key=True)
    email = db.Column('email', db.String(150), unique=True, nullable=False)
    password = db.Column('password', db.String(100), nullable=False)
    name = db.Column('username', db.String(100), nullable=False)

    def __init__(self, user_id, email, password, name):
        self.user_id = user_id
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

    type_id = db.Column('type_id', db.String(10), primary_key=True)
    user_id = db.Column('user_id', db.String(
        10), db.ForeignKey('user.user_id'))
    description = db.Column('description', db.String(100), nullable=False)
    budget = db.Column('budget', db.Integer(), nullable=False)

    def __init__(self, type_id, user_id, description, budget):
        self.type_id = type_id
        self.user_id = user_id
        self.description = description
        self.budget = budget

    def to_json(self):
        return {
            "type_id": self.type_id,
            "user_id": self.user_id,
            "description": self.description,
            "budget": self.budget
        }


class Transaction(db.Model):
    __tablename__ = "transaction"

    transaction_id = db.Column(
        'transaction_id', db.String(10), primary_key=True)
    type_id = db.Column('type_id', db.String(
        10), db.ForeignKey('type.type_id'))
    user_id = db.Column('user_id', db.String(
        10), db.ForeignKey('user.user_id'))
    description = db.Column('description', db.String(100), nullable=False)
    amount = db.Column('amount', db.Integer(), nullable=False)

    def __init__(self, transaction_id, type_id, user_id, description, amount):
        self.transaction_id = transaction_id
        self.type_id = type_id
        self.user_id = user_id
        self.description = description
        self.amount = amount

    def to_json(self):
        return {
            "transaction": self.transaction_id,
            "type_id": self.type_id,
            "user_id": self.user_id,
            "description": self.description,
            "amount": self.amount
        }
