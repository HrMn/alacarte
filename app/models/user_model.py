from app import Base
from sqlalchemy import Column,String, Integer

# Define a User model
class Users(Base):
    __tablename__ = 'users'
    __table_args__ = {"useexisting": True}

    id = Column(Integer, primary_key=True)
    role = Column(Integer, nullable=False)
    username = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False, unique=True)
    password = Column(String(192), nullable=False)

    # New instance instantiation procedure
    def __init__(self, role, username, email, password):
        self.role = role
        self.username = username
        self.password = password
        self.email = email

    def __repr__(self):
        return '<User %r>' % (self.username)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

