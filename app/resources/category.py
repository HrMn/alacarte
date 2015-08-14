#!flask/bin/python
from flask_restful import Resource
from flask import jsonify
from app.models.category_model import Category
from flask_restful import reqparse
from app import db_session
from sqlalchemy.exc import IntegrityError
from werkzeug import datastructures
from flask import send_file

import os
import app
import sys

class CategoryListAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("name", type = str, required = True, help = 'No name provided')
        self.reqparse.add_argument("description", type = str, required = False)
        self.reqparse.add_argument("image_url", type = str, required = False)
        self.reqparse.add_argument('image', type=datastructures.FileStorage, location='files')
        super(CategoryListAPI, self).__init__()

    def get(self):
        categories = Category.query.all()
        results = []
        for row in categories:
            results.append(row.as_dict())
        return results

    def post(self):
        args = self.reqparse.parse_args()
        o = Category(args["name"],args["description"],args["image_url"])

        try:
            db_session.add(o)
            db_session.commit()
        except IntegrityError as err:
            db_session.rollback()
            return {"DB Error: {0}".format(err)}, 500

        file = args['image']
        if file:
            extension = os.path.splitext(file.filename)[1]
            filename = "uploads/categories/category_img_" + str(o.id) + extension
            o.image_url = filename
            file.save(os.path.join(os.getcwd(), filename))

        return o.as_dict(),201

class CategoryAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('name', type = str,location = 'json')
        self.reqparse.add_argument('description', type = str, location = 'json')
        self.reqparse.add_argument('image_url', type = str, location = 'json')
        super(CategoryAPI, self).__init__()

    def get(self, id):
        e = Category.query.filter(Category.id == id).first()
        if e is not None:
            return e.as_dict()
        else:
            return {}

    def put(self, id):
        pass

    def delete(self, id):
        pass

class CategoryImageAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        super(CategoryImageAPI, self).__init__()

    def get(self, id):
        filename="uploads/categories/" + id
        fullpath = os.path.join(os.getcwd(), filename)
        return send_file(fullpath, mimetype="image/jpeg")

    def put(self, id):
        pass

    def delete(self, id):
        pass