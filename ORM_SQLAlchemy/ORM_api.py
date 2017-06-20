from ORM_SQLAlchemy import ORM_more_foreignkey
from sqlalchemy.orm import sessionmaker

Session_class = sessionmaker(bind=ORM_more_foreignkey.engine)
session = Session_class()

# addr1 = ORM_more_foreignkey.Address(street='Tiantongyuan', city='ChangPing', state='BJ')
# addr2 = ORM_more_foreignkey.Address(street='Wudaokou', city='HaiDian', state='BJ')
# addr3 = ORM_more_foreignkey.Address(street='Yanjiao', city='LangFang', state='HB')
#
# session.add_all([addr1, addr2, addr3])
#
# c1 = ORM_more_foreignkey.Customer(name='Alex', billing_address=addr1, shipping_address=addr2)
# c2 = ORM_more_foreignkey.Customer(name='Jack', billing_address=addr3, shipping_address=addr3)
#
# session.add_all([c1, c2])

obj = session.query(ORM_more_foreignkey.Customer).filter(ORM_more_foreignkey.Customer.name=='Alex').first()
print(obj)
print(obj.name, obj.billing_address, obj.shipping_address)
session.commit()