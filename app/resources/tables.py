#!flask/bin/python
from flask_restful import Resource
from flask import jsonify
from app.models.table_model import Tables
from flask_restful import reqparse
from app import db_session
from sqlalchemy.exc import IntegrityError
import sys

class TablesListAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("name", type = str, required = True, help = 'No name provided')
        super(TablesListAPI, self).__init__()

    def get(self):
        tables = Tables.query.all()
        results = []
        for row in tables:
            results.append(row.as_dict())
        return results

    def post(self):
        args = self.reqparse.parse_args()
        o = Tables(args["name"])

        try:
            db_session.add(o)
            db_session.commit()
        except IntegrityError as err:
            db_session.rollback()
            return {"DB Error: {0}".format(err)}, 500
        return o.as_dict(),201

class TableAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('name', type = str, location = 'json')
        super(TableAPI, self).__init__()

    def get(self, id):
        e = Tables.query.filter(Tables.id == id).first()
        if e is not None:
            return e.as_dict()
        else:
            return {}

    def put(self, id):
        pass

    def delete(self, id):
        pass

