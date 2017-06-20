import orm_m2m
from sqlalchemy.orm import sessionmaker

Session_class = sessionmaker(bind=orm_m2m.engine)
session = Session_class()

# b1 = orm_m2m.Book(name='learn python1 with Alex', pub_date='2014-01-01')
# b2 = orm_m2m.Book(name='learn python2 with Alex', pub_date='2014-02-01')
# b3 = orm_m2m.Book(name='learn python3 with Alex', pub_date='2014-02-01')
b4 = orm_m2m.Book(name='流畅的Python', pub_date='2017-02-01')

# a1 = orm_m2m.Author(name='Alex')
# a2 = orm_m2m.Author(name='Jack')
# a3 = orm_m2m.Author(name='Rain')
a4 = orm_m2m.Author(name='Song1')
a5 = orm_m2m.Author(name='Song2')
#
# b1.authors = [a1, a3]
# b3.authors = [a1, a2, a3]
b4.authors = [a4, a5]
# session.add_all([b1, b2, b3, a1, a2, a3])
session.add_all([b4, ])
#
author_obj = session.query(orm_m2m.Author).filter(orm_m2m.Author.name=='Alex').first()
print(author_obj.books)
print(author_obj)
print(author_obj.books[0].pub_date)

book_obj = session.query(orm_m2m.Book).filter(orm_m2m.Book.id==2).first()
print(book_obj.authors)
# book_obj.authors.remove(author_obj)
session.commit()
