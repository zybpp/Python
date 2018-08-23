#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:zpp

import getpass
import os

account = {'zhangsan': 'ad123', 'lishi': '123456', 'wangwu': 'sd12345'}

name = input("please input name:")
password = input("please input password:")
res = account.get(name,-1)
time = 0

if name in account:
	if os.path.exists('name.txt'):
		file = open('name.txt','r')
		time = int(file.read())
	else:
		file = open('name.txt', 'w')
		file.write(str(1))
	if time <= 3:
		if password == account[name]:
			print("Welcome to login account!!")
		else:
			print("Your password is error!!")
			time += 1;
			file = open('name.txt', 'w')
			file.write(str(time))
	else:
		print("Your password error time is three times,your account is locked!!")
else:
	print("Your name isn't exist!!")

