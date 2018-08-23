#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:zpp

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DATE, Enum, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import func

engine = create_engine("mysql+pymysql://root:123456@localhost/zpp",encoding="utf-8")

Base = declarative_base()
class Student(Base):
	__tablename__ = "student"
	id = Column(Integer,autoincrement=True,primary_key=True)
	name = Column(String(32),nullable=False)
	register_date = Column(DATE,nullable=False)

	def __repr__(self):
		return "<id:%s name:%s>" %(self.id, self.name)

class StudyRecord(Base):
	__tablename__ = "studyrecord"
	id = Column(Integer,autoincrement=True,primary_key=True)
	day = Column(Integer,nullable=False)
	status = Column(String(32),nullable=False)
	stu_id = Column(Integer,ForeignKey("student.id"))
	student = relationship("Student",backref="my_study_record")

	def __repr__(self):
		return "<name:%s day:%s status:%s>" %(self.student.name, self.day, self.status)

Base.metadata.create_all(engine)

Session_class = sessionmaker(bind=engine)
session = Session_class()

# s1 = Student(name="lishunbo",register_date="2017-04-15")
# s2 = Student(name="sunhuihui",register_date="2017-08-19")
# s3 = Student(name="sunxiaolong",register_date="2018-01-15")
# s4 = Student(name="xuyi",register_date="2018-04-05")
#
# study1 = StudyRecord(day=1,status="YES",stu_id=1)
# study2 = StudyRecord(day=2,status="NO",stu_id=1)
# study3 = StudyRecord(day=3,status="YES",stu_id=1)
# study4 = StudyRecord(day=1,status="YES",stu_id=2)
# study5 = StudyRecord(day=2,status="NO",stu_id=2)
# study6 = StudyRecord(day=3,status="NO",stu_id=2)
# study7 = StudyRecord(day=1,status="YES",stu_id=3)
# study8 = StudyRecord(day=2,status="YES",stu_id=3)
# study9 = StudyRecord(day=3,status="YES",stu_id=3)
# study10 = StudyRecord(day=1,status="YES",stu_id=4)
# study11 = StudyRecord(day=2,status="NO",stu_id=4)
# study12 = StudyRecord(day=3,status="NO",stu_id=4)

# session.add_all([s1,s2,s3,s4,study1,study2,study3,study4,study5,study6,study7,study8,study9,study10,study11,study12])

stu = session.query(Student).filter(Student.name == "sunhuihui").first()
print(stu.my_study_record)
session.commit()


