from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func

engine = create_engine('mysql+pymysql://root:mysql@localhost/python',
                       encoding='utf-8', echo=True)

Base = declarative_base()

class User(Base):
    __tablename__ = 'user_song'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32))
    password = Column(String(64))

    def __repr__(self):
        return '<id:%s | name:%s | password: %s>' % (self.id, self.name, self.password)


class Students(Base):
    __tablename__ = 'students2'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=True)
    name = Column(String(32))
    gender = Column(Enum('F', 'M'), nullable=False)

    def __repr__(self):
        return '<id:%s | name: %s | gender: %s>' % (self.id, self.name, self.gender)
Base.metadata.create_all(engine)
# data = Students(name='song1', gender='M')

Session_class = sessionmaker(bind=engine)  # 创建与数据库会话的类，不是实例
Session = Session_class()  # 生成session实例(cursor)
# Session.add(data)
# Session.commit()
# 增
# user_obj1 = User(name='song1', password='song1')  # 生成你要创建的数据对象
# user_obj2 = User(name='song2', password='song2')  # 生成你要创建的数据对象
# # print(user_obj1.name, user_obj1.id)
#
# Session.add(user_obj1)
# Session.add(user_obj2)
# #print(user_obj1.name, user_obj1.id)
#
# Session.commit()
# print(user_obj1.name, user_obj1.id)
# print(user_obj2.name, user_obj2.id)

# 查询

# data = Session.query(User).filter().first()
# data2 = Session.query(User).filter_by().all()
# data3 = Session.query(User).filter(User.id>1).all()
# data4 = Session.query(User).filter(User.id==1).all()
# data5 = Session.query(User).filter_by(id=1).all()
# data6 = Session.query(User).filter(User.id>1).filter(User.id<4).all()
# data7 = Session.query(User.id, User.name, User.password).first()
# filter和filter_by类似where
# print(data)
# print(data7)
# print(data2)
# print(data3)
# print(data4)
# print(data5)
# print(data6)

# 修改
# data.name = 'Song11'
# data.password = 'Song11'
# Session.commit()
# 回滚
# my_user = Session.query(User).filter_by(id=1).first()
# my_user.name = 'Jack'
#
# fake_user = User(name='Rain', password='12345')
# Session.add(fake_user)
#
# print(Session.query(User).filter(User.name.in_(['Jack', 'rain'])).all())
#
# Session.rollback()
#
# print(Session.query(User).filter(User.name.in_(['Jack', 'rain'])).all())

# 统计
# count = Session.query(User).filter(User.name.like('S%')).count()
# data = Session.query(User).filter(User.name.like('S%')).all()
# print(data)
# print(count)

# 分组
print(Session.query(func.count(User.name), User.name).group_by(User.name).all())

# 连表 join
print(Session.query(User, Students).filter(User.id==Students.id).all())


