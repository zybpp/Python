#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:zpp
import sys
from core import login

class student(object):
	def __init__(self):
		print("Welcome into student page.")

	def own_login(self):
		return login.login("student")

def student_page():
	student_obj = student()
	login = student_obj.own_login()
	if login:
		pass
	else:
		print("用户登陆失败！！")
		sys.exit()