#!flask/bin/python
from flask_restful import Resource
from flask import jsonify
from app.models.userrole_model import UserRoles
from flask_restful import reqparse
from app import db_session
from sqlalchemy.exc import IntegrityError
import sys

class UserRolesListAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("role_name", type = str, required = True, help = 'No role name provided')
        super(UserRolesListAPI, self).__init__()

    def get(self):
        roles = UserRoles.query.all()
        results = []
        for row in roles:
            results.append(row.as_dict())
        return results

    def post(self):
        args = self.reqparse.parse_args()
        o = UserRoles(args["role_name"])

        try:
            db_session.add(o)
            db_session.commit()
        except IntegrityError as err:
            db_session.rollback()
            return {"DB Error: {0}".format(err)}, 500
        return o.as_dict(),201

class UserRoleAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('role_name', type = str, location = 'json')
        super(UserRoleAPI, self).__init__()

    def get(self, id):
        e = UserRoles.query.filter(UserRoles.id == id).first()
        if e is not None:
            return e.as_dict()
        else:
            return {}

    def put(self, id):
        pass

    def delete(self, id):
        pass