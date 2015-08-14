from app import Base
from sqlalchemy import Column,String, Integer,TEXT,Numeric

# Define a User model
class FoodItems(Base):
    __tablename__ = 'food_items'
    __table_args__ = {"useexisting": True}

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(500))
    image_url = Column(String(200))
    category_id = Column(Integer,nullable=False)
    sub_category_id = Column(Integer)
    rating = Column(Integer)
    ingredients = Column(TEXT)
    best_combination = Column(TEXT)
    rate = Column(Numeric)


    # New instance instantiation procedure
    def __init__(self, name, description, image_url,category_id,sub_category_id,rating,ingredients,best_combination,rate):
        self.name = name
        self.description = description
        self.image_url = image_url
        self.category_id = category_id
        self.sub_category_id = sub_category_id
        self.rating = rating
        self.ingredients = ingredients
        self.best_combination = best_combination
        self.rate = rate

    def __repr__(self):
        return '<User %r>' % (self.name)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}