#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:zpp
import sys
from core import login

class lecturer(object):
	def __init__(self):
		print("Welcome into lecturer page.")

	def own_login(self):
		return login.login("lecturer")

def lecturer_page():
	lecturer_obj = lecturer()
	login = lecturer_obj.own_login()
	if login:
		pass
	else:
		print("用户登陆失败！！")
		sys.exit()