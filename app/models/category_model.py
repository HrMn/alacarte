from app import Base
from sqlalchemy import Column,String, Integer

# Define a User model
class Category(Base):
    __tablename__ = 'category'
    __table_args__ = {"useexisting": True}

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(500))
    image_url = Column(String(200))

    # New instance instantiation procedure
    def __init__(self, name, description, image_url):
        self.name = name
        self.description = description
        self.image_url = image_url

    def __repr__(self):
        return '<User %r>' % (self.name)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
