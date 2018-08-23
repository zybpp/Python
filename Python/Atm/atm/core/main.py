#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:zpp

from core import auth
from core import transaction
from core import manage

def main():
	print("Welcome to atm home page!!")
	operation = input("Please input your operation(m > 管理 , l > 登陆):")
	if operation == "m":
		manage.atm_manage()
	elif operation == "l":
		name = input("Please input your name:")
		password = input("Please input your password:")
		login_data = auth.auth(name,password)
		if login_data:
			transaction.transaction(login_data)
