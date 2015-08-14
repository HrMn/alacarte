from app import Base
from sqlalchemy import Column,String, Integer,TEXT,Numeric

# Define a Order model
class Orders(Base):
    __tablename__ = 'orders'
    __table_args__ = {"useexisting": True}

    id = Column(Integer, primary_key=True)
    table_id = Column(Integer, nullable=False)
    waiter_id = Column(Integer)
    chef_id = Column(Integer)
    order_details = Column(TEXT,nullable=False)
    order_status = Column(String(100))
    cost = Column(String(50))

    # New instance instantiation procedure
    def __init__(self, table_id,waiter_id,chef_id,order_details,order_status,cost):
        self.table_id = table_id
        self.waiter_id = waiter_id
        self.chef_id = chef_id
        self.order_details = order_details
        self.order_status = order_status
        self.cost = cost

    def __repr__(self):
        return '<Order Status %r>' % (self.order_status)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}



