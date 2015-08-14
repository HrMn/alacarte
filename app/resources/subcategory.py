#!flask/bin/python
from flask_restful import Resource
from flask import jsonify
from app.models.subcategory_model import SubCategory
from flask_restful import reqparse
from app import db_session
from sqlalchemy.exc import IntegrityError
import sys

class SubCategoryListAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("name", type = str, required = True, help = 'No name provided')
        self.reqparse.add_argument("description", type = str, required = False, location = 'json')
        self.reqparse.add_argument("image_url", type = str, required = False,location = 'json')
        self.reqparse.add_argument("category_id", type = int, required = True,location = 'json')
        super(SubCategoryListAPI, self).__init__()

    def get(self):
        sub_categories = SubCategory.query.all()
        results = []
        for row in sub_categories:
            results.append(row.as_dict())
        return results

    def post(self):
        args = self.reqparse.parse_args()
        o = SubCategory(args["name"],args["description"],args["image_url"],args["category_id"])

        try:
            db_session.add(o)
            db_session.commit()
        except IntegrityError as err:
            db_session.rollback()
            return {"DB Error: {0}".format(err)}, 500
        return o.as_dict(),201

class SubCategoryAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('name', type = str,location = 'json')
        self.reqparse.add_argument('description', type = str, location = 'json')
        self.reqparse.add_argument('image_url', type = str, location = 'json')
        self.reqparse.add_argument("category_id", type = int, required = True,location = 'json')
        super(SubCategoryAPI, self).__init__()

    def get(self, id):
        e = SubCategory.query.filter(SubCategory.id == id).first()
        if e is not None:
            return e.as_dict()
        else:
            return {}

    def put(self, id):
        pass

    def delete(self, id):
        pass
