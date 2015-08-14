from app import Base
from sqlalchemy import Column,String, Integer

# Define a UserRoles model
class UserRoles(Base):
    __tablename__ = 'user_roles'
    __table_args__ = {"useexisting": True}

    id = Column(Integer, primary_key=True)
    role_name = Column(String(128), nullable=False)

    # New instance instantiation procedure
    def __init__(self, rolename):
        self.role_name = rolename

    def __repr__(self):
        return '<User %r>' % (self.role_name)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
