import sys
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()


class User(UserMixin):
    def __init__(self, id, access):
        self.id = id
        self.roles = [access]

# ------------------- SQLITE TABLES -----------------------------------------


class Users(db.Model):
    login = db.Column(db.String(80), unique=True,
                      nullable=False, primary_key=True)
    password = db.Column(db.String(120), nullable=False)
    access = db.Column(db.String(80), nullable=False)


class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type_id = db.Column(db.Integer)
    description = db.Column(db.String(150))


class Jobs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    house_id = db.Column(db.Integer)
    company_id = db.Column(db.Integer)


def select_data_type(id_):
    res = db.session.query(Data.type_id).\
        filter(Data.id == id_).first()[0]
    return res


def delete_data(id_, tipe_id):

    db.session.query(Data).\
        filter(Data.id == id_).delete()

    q = db.session.query(Jobs)
    if tipe_id == 1:
        q.filter(Jobs.company_id == id_).delete()
    else:
        q.filter(Jobs.house_id == id_).delete()
    db.session.commit()


def auth(login):
    return Users.query.get(login)


def select_users():
    return Users.query.all()


def select_jobs():
    return Jobs.query.all()


def insert_data(data):
    record = Data(**data)
    db.session.add(record)
    db.session.commit()


def insert_job(data):
    record = Jobs(**data)
    db.session.add(record)
    db.session.commit()


def select_description(id):
    res = db.session.query(Data.description).\
        filter(Data.id == id).first()
    return res[0]


def select_job(company_id=None, house_id=None):
    if (company_id is not None) and (house_id is not None):
        res = db.session.query(Jobs.id).\
            filter(Jobs.house_id == house_id).\
            filter(Jobs.company_id == company_id).first()
        return res

    if company_id is not None:
        res = db.session.query(Jobs.id).\
            filter(Jobs.company_id == company_id).all()
        return res

    if house_id is not None:
        res = db.session.query(Jobs.id).\
            filter(Jobs.house_id == house_id).all()
        return res


def select_data(type_id):
    res = db.session.query(Data.id, Data.description).\
        filter(Data.type_id == type_id).all()
    return res
