#!flask/bin/python
from flask_restful import Resource
from flask import jsonify
from app.models.fooditems_model import FoodItems
from flask_restful import reqparse
from app import db_session
from sqlalchemy.exc import IntegrityError
import sys

class FoodItemsListAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("name", type = str, required = True, help = 'No name provided')
        self.reqparse.add_argument("description", type = str, required = False, location = 'json')
        self.reqparse.add_argument("image_url", type = str, required = False,location = 'json')
        self.reqparse.add_argument("category_id", type = int, required = True,location = 'json',help = 'Category id not provided')
        self.reqparse.add_argument("sub_category_id", type = int, required = False,location = 'json')
        self.reqparse.add_argument("rating", type = int, required = False,location = 'json')
        self.reqparse.add_argument("ingredients", type = str, required = False,location = 'json')
        self.reqparse.add_argument("best_combination", type = str, required = False,location = 'json')
        self.reqparse.add_argument("rate", type = float, required = True,location = 'json',help = 'Rate not provided')
        super(FoodItemsListAPI, self).__init__()

    def get(self):
        food_items = FoodItems.query.all()
        results = []
        for row in food_items:
            results.append(row.as_dict())
        return results

    def post(self):
        args = self.reqparse.parse_args()
        o = FoodItems(args["name"],args["description"],args["image_url"],args["category_id"],args["sub_category_id"],args["rating"],args["ingredients"],args["best_combination"],args["rate"])

        try:
            db_session.add(o)
            db_session.commit()
        except IntegrityError as err:
            db_session.rollback()
            return {"DB Error: {0}".format(err)}, 500
        return o.as_dict(),201

class FoodItemAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('name', type = str,location = 'json')
        self.reqparse.add_argument('description', type = str, location = 'json')
        self.reqparse.add_argument('image_url', type = str, location = 'json')
        self.reqparse.add_argument("category_id", type = int, required = True,location = 'json')
        self.reqparse.add_argument("sub_category_id", type = int, required = False,location = 'json')
        self.reqparse.add_argument("rating", type = int, required = False,location = 'json')
        self.reqparse.add_argument("ingredients", type = str, required = False,location = 'json')
        self.reqparse.add_argument("best_combination", type = str, required = False,location = 'json')
        self.reqparse.add_argument("rate", type = float, location = 'json',help = 'Rate not provided')
        super(FoodItemAPI, self).__init__()

    def get(self, id):
        e = FoodItems.query.filter(FoodItems.id == id).first()
        if e is not None:
            return e.as_dict()
        else:
            return {}

    def put(self, id):
        pass

    def delete(self, id):
        pass
