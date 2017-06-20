from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,  ForeignKey
from sqlalchemy.orm import relationship

engine = create_engine('mysql+pymysql://root:mysql@localhost/python',
                       encoding='utf-8')
Base = declarative_base()


class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))

    billing_address_id = Column(Integer, ForeignKey('address.id'))
    shipping_address_id = Column(Integer, ForeignKey('address.id'))

    billing_address = relationship('Address', foreign_keys=billing_address_id)
    shipping_address = relationship('Address', foreign_keys=shipping_address_id)


class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    street = Column(String(64))
    city = Column(String(64))
    state = Column(String(64))

    def __repr__(self):
        return '%s : %s : %s' % (self.street, self.city, self.state)

Base.metadata.create_all(engine)
