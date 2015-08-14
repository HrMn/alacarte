#!flask/bin/python
from flask_restful import Resource
from flask import jsonify
from app.models.user_model import Users
from flask_restful import reqparse
from app import db_session
from sqlalchemy.exc import IntegrityError
import sys

class UsersListAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("username", type = str, required = True, help = 'No user name provided')
        self.reqparse.add_argument("password", type = str, required = True, help = 'No password provided', location = 'json')
        self.reqparse.add_argument("email", type = str, required = True, help = 'No email provided', location = 'json')
        self.reqparse.add_argument("role", type = int, required = True, help = 'No role id provided', location = 'json')
        super(UsersListAPI, self).__init__()

    def get(self):
        users = Users.query.all()
        results = []
        for row in users:
            results.append(row.as_dict())
        return results

    def post(self):
        args = self.reqparse.parse_args()
        o = Users(args["role"],args["username"],args["email"],args["password"])

        try:
            db_session.add(o)
            db_session.commit()
        except IntegrityError as err:
            db_session.rollback()
            return {"DB Error: {0}".format(err)}, 500
        return o.as_dict(),201

class UserAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('password', type = str, location = 'json')
        self.reqparse.add_argument('email', type = str, location = 'json')
        self.reqparse.add_argument('role', type = int, location = 'json')
        super(UserAPI, self).__init__()

    def get(self, id):
        e = Users.query.filter(Users.id == id).first()
        if e is not None:
            return e.as_dict()
        else:
            return {}

    def put(self, id):
        pass

    def delete(self, id):
        pass
