#!flask/bin/python
from flask_restful import Resource
from flask import jsonify
from app.models.order_model import Orders
from flask_restful import reqparse
from app import db_session
from sqlalchemy.exc import IntegrityError
import sys

class OrdersListAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("table_id", type = int, required = True, help = 'No table id provided')
        self.reqparse.add_argument("waiter_id", type = int, required = False,  location = 'json')
        self.reqparse.add_argument("chef_id", type = int, required = False, location = 'json')
        self.reqparse.add_argument("order_details", type = str, required = True, help = 'Order details not provided', location = 'json')
        self.reqparse.add_argument("order_status", type = str, required = False,  location = 'json')
        self.reqparse.add_argument("cost", type = int, required = True, help = 'No cost provided', location = 'json')

        super(OrdersListAPI, self).__init__()

    def get(self):
        users = Orders.query.all()
        results = []
        for row in users:
            results.append(row.as_dict())
        return results

    def post(self):
        args = self.reqparse.parse_args()
        o = Orders(args["table_id"],args["waiter_id"],args["chef_id"],args["order_details"],args["order_status"],args["cost"])

        try:
            db_session.add(o)
            db_session.commit()
        except IntegrityError as err:
            db_session.rollback()
            return {"DB Error: {0}".format(err)}, 500
        #return o.as_dict(),201
        return "Success"

class OrderAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('table_id', type = int, location = 'json')
        self.reqparse.add_argument('waiter_id', type = int, location = 'json')
        self.reqparse.add_argument('chef_id', type = int, location = 'json')
        self.reqparse.add_argument('order_details', type = str, location = 'json')
        self.reqparse.add_argument('order_status', type = str, location = 'json')
        self.reqparse.add_argument('cost', type = int, location = 'json')
        super(OrderAPI, self).__init__()

    def get(self, id):
        e = Orders.query.filter(Orders.id == id).first()
        if e is not None:
            return e.as_dict()
        else:
            return {}

    def put(self, id):
        pass

    def delete(self, id):
        pass

