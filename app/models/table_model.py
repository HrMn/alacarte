from app import Base
from sqlalchemy import Column,String, Integer

# Define a Table model
class Tables(Base):
    __tablename__ = 'tables'
    __table_args__ = {"useexisting": True}

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    # New instance instantiation procedure
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Table %r>' % (self.name)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


