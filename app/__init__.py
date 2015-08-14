import os
from flask import Flask
from flask_restful import Api, Resource
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

if os.environ.get('DATABASE_URL') is None:
  engine = create_engine('postgresql://postgres:root@localhost/alacarte_db', convert_unicode=True)
else:
  engine = create_engine(os.environ['DATABASE_URL'], convert_unicode=True)

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

# Define the database object which is imported
# by modules and controllers
#db = SQLAlchemy(app)

Base = declarative_base()
Base.query = db_session.query_property()

from app.resources.users import UsersListAPI
from app.resources.users import UserAPI
from app.resources.userroles import UserRolesListAPI
from app.resources.userroles import UserRoleAPI
from app.resources.category import CategoryListAPI
from app.resources.category import CategoryAPI
from app.resources.subcategory import SubCategoryListAPI
from app.resources.subcategory import SubCategoryAPI
from app.resources.fooditems import FoodItemsListAPI
from app.resources.fooditems import FoodItemAPI
from app.resources.tables import TablesListAPI
from app.resources.tables import TableAPI
from app.resources.orders import OrdersListAPI
from app.resources.orders import OrderAPI
from app.resources.category import CategoryImageAPI

api = Api(app)

api_root = "/alacarte/api/v1.0/"
api.add_resource(UserRolesListAPI, api_root + 'user_roles')
api.add_resource(UserRoleAPI, api_root + 'user_roles/<int:id>')
api.add_resource(UsersListAPI, api_root + 'users')
api.add_resource(UserAPI, api_root + 'users/<int:id>')
api.add_resource(CategoryListAPI, api_root + 'categories')
api.add_resource(CategoryAPI, api_root + 'categories/<int:id>')
api.add_resource(SubCategoryListAPI, api_root + 'sub_categories')
api.add_resource(SubCategoryAPI, api_root + 'sub_categories/<int:id>')
api.add_resource(FoodItemsListAPI, api_root + 'food_items')
api.add_resource(FoodItemAPI, api_root + 'food_items/<int:id>')
api.add_resource(TablesListAPI, api_root + 'tables')
api.add_resource(TableAPI, api_root + 'tables/<int:id>')
api.add_resource(OrdersListAPI, api_root + 'orders')
api.add_resource(OrderAPI, api_root + 'orders/<int:id>')
api.add_resource(CategoryImageAPI,api_root+ 'uploads/categories/<string:id>')
