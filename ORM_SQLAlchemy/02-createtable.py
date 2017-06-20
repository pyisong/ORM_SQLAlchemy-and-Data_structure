from sqlalchemy import Table, MetaData, Column, Integer, String,  create_engine


metadata = MetaData()

engine = create_engine('mysql+pymysql://root:mysql@localhost/python',
                        encoding='utf-8', echo=True)

user = Table('user_song2', metadata,
             Column('id', Integer, primary_key=True, autoincrement=True),
             Column('name', String(50)),
             Column('fullname', String(50),),
             Column('password', String(12))
             )


class User(object):
    def __init__(self, name, fullname, password):
        self.name = name
        self.fullname = fullname
        self.password = password

metadata.create_all(engine)
