from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index, CHAR, VARBINARY
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine


Base = declarative_base()


# 创建单表
class UserType(Base):
    __tablename__ = 'usertype'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(32), nullable=True, index=True)


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32), nullable=True,default='sf', index=True)
    extra = Column(String(16), unique=True)
    user_type_id = Column(Integer, ForeignKey('usertype.id'))

    # user_type = relationship('UserType', backref='xxoo')

    # __table_args__ = (
    #     UniqueConstraint('id', 'name', name='uix_id_name'),
    #     Index('ix_id_name', 'name', 'extra'),
    # )

def create_db():
    engine = create_engine("mysql+pymysql://root:079450@127.0.0.1:3306/day63db?charset=utf8", max_overflow=5)
    Base.metadata.create_all(engine)
#
create_db()
#
def drop_db():
    engine = create_engine("mysql+pymysql://root:079450@127.0.0.1:3306/day63db?charset=utf8", max_overflow=5)
    Base.metadata.drop_all(engine)

engine = create_engine("mysql+pymysql://root:079450@127.0.0.1:3306/day63db?charset=utf8", max_overflow=5)

Session = sessionmaker(bind=engine)
session = Session()

# 类 -> 表
# 对象 -> 行
# ########添加##############
# obj1 = UserType(title='usually user')
# session.add(obj1)

# objs = [
#     UserType(title='super user'),
#     UserType(title='golden user'),
#     UserType(title='break user')
# ]
# session.add_all(objs)

##########查#############
# user_type_list = session.query(UserType).all()
# select xx UserType where
# user_type_list = session.query(UserType.id, UserType.title).filter(UserType.id>2)
# for row in user_type_list:
#     print(row.id, row.title)

#分组，排序，链表，通配符，子查询，limit，union，where，原生SQL
# ret = session.query(Users, UserType)
# select * from user, usertype;

# ret = session.query(Users, UserType).filter(Users.user_type_id == UserType.id)
# select * from user, usertype where user.usertype_id = usertype.id

# result = session.query(Users).join(UserType)
# print(result)

# result = session.query(Users).join(UserType, isouter=True)
# print(result)

# 1.
# select * from b where id in (select id from tb2)

# 2.
# select * from (select * from tb) as B
# q1 = session.query(UserType).filter(UserType.id > 0).subquery()
#
# ret = session.query(q1).all()
# print(ret)

# 3.
# select id, (select * from users where users, user_type_id = 1) from Usertype;
# ret = session.query(UserType.id, session.query(Users).filter(Users.id==1).subquery()).all()  # 还没在Users表里加数据
# ret = session.query(UserType.id, session.query(Users).as_scalar())
# print(ret)
ret = session.query(UserType.id, session.query(Users).filter(Users.user_type_id == UserType.id).as_scalar())
print(ret)


#######删##############
# user_type_list = session.query(UserType.id, UserType.title).filter(UserType.id>2).delete()


#######改########
# user_type_list = session.query(UserType.id, UserType.title).filter(UserType.id>2).update({'title':'break user'})
# user_type_list1 = session.query(UserType).filter(UserType.id > 2).update({UserType.title: UserType.title + "x"}, synchronize_session=False)
# user_type_list2 = session.query(UserType).filter(UserType.id > 2).update({"num": UserType.title + 1}, synchronize_session="evaluate")
# 
# session.commit()
# session.close()


# relationship
#      正向操作：有relationship还有ForeignKey
#      反向操作
#

# 问题1.获取用户信息以及与其关联的用户类型名称

# user_list = session.query(Users, UserType).join(UserType, isouter=True)
# for row in user_list:
#     print(row[0].id, row[0].name, row[0].extra, row[0].user_type_id, row[1].title)

# user_list = session.query(Users.name, UserType.title).join(UserType, isouter=True).all()
# for row in user_list:
#     print(row[0], row[1], row.name, row.title)

# user_list = session.query(Users)
# for row in user_list:
#     print(row.name, row.id, row.user_type.title)


# 问题2.获取用户类型

# type_list =session.query(UserType)
# for row in type_list:
#     print(row.id, row.title, session.query(Users).filter(Users.user_type_id == row.id).all())

# type_list =session.query(UserType)
# for row in type_list:
#     print(row.id, row.title, row.xxoo)