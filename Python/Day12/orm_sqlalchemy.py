#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:zpp

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DATE, Enum
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func

engine = create_engine("mysql+pymysql://root:123456@localhost/zppdb",encoding="utf-8")

Base = declarative_base()
class User(Base):
	__tablename__ = "user"
	id = Column(Integer,autoincrement=True,primary_key=True)
	name = Column(String(32))
	password = Column(String(64))

	def __repr__(self):
		return "<id:%s, name:%s>" %(self.id,self.name)

class Student(Base):
	__tablename__ = "student"
	id = Column(Integer,autoincrement=True,primary_key=True)
	name = Column(String(32),nullable=False)
	register_date = Column(DATE,nullable=False)
	gender = Column(Enum("M","F"),nullable=False)

Base.metadata.create_all(engine)

Session_class = sessionmaker(bind=engine)
Session = Session_class()

# user_obj = User(name="lishunbo", password="abdia")
# print(user_obj.name,user_obj.id)
# Session.add(user_obj)
# print(user_obj.name,user_obj.id)
#
# Session.commit()
# print(user_obj.name,user_obj.id)

# data = Session.query(User).filter(User.name=="lishunbo").filter(User.id==1).first()
# print(data)
# data.name = "sunhuihui"
# data.password = "1242343"
# print(dir(Session))

# fake_user = User(name="sunxiaolong",password="124234")
# Session.add(fake_user)
# print(Session.query(User).filter(User.name.in_(["sunhuihui", "sunxiaolong"])).all())
# Session.rollback()
print(Session.query(User.name,func.count(User.name)).group_by(User.name).all())
print(Session.query(User).filter(User.name.in_(["sunhuihui", "sunxiaolong"])).count())
# print(Session.query(User,Student).filter(User.id==Student.id).all())
Session.commit()
