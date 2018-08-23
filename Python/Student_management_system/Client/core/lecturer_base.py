#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:zpp
import sys
import socket
import json
from conf import config

class lecturer(object):
	def __init__(self):
		print("Welcome into lecturer page.")
		self.lec_client = socket.socket()
		self.addr = ("localhost",9999)
		self.account_info = config.account_info

	def auth(self,name,password):
		self.lec_client.connect(self.addr)
		self.account_info["name"] =name
		self.account_info["password"] = password
		self.account_info["way"] = "lecturer"
		self.lec_client.send(json.dumps(self.account_info).encode("utf-8"))
		auth_result = self.lec_client.recv(1024).decode("utf-8")
		return auth_result

	def new_account(self):
		while True:
			name = input("请输入新用户名：")
			password = input("请输入密码：")
			if len(name) > 0 and len(password) > 0:
				self.account_info["way"] = "lecturer"
				self.account_info["name"] = name
				self.account_info["password"] = password
				self.account_info["new"] = "yes"
				self.lec_client.send(json.dumps(self.account_info).encode("utf-8"))
				new_result = self.lec_client.recv(1024).decode("utf-8")
				return new_result
			else:
				print("新用户名或密码输入有误！！")

	def login(self):
		while True:
			name = input("请输入用户名：")
			password = input("请输入密码：")
			if len(name) > 0:
				auth_result = self.auth(name,password)
			else:
				print("用户名未输入！！")
			if auth_result == "1001":
				print(config.auth_return[auth_result])
				return True
			elif auth_result == "1002":
				while True:
					resume = input(config.auth_return[auth_result])
					if resume == "y":
						break
					elif resume == "n":
						return False
					elif resume != "":
						print("输入有误！！")
			elif auth_result == "1003":
				while True:
					new = input(config.auth_return[auth_result])
					if new == "y":
						new_result = self.new_account()
						if new_result == "1004":
							print(config.auth_return[new_result])
							return True
						else:
							return False
					elif new == "n":
						return False
					elif new != "":
						print("输入有误！！")

def lecturer_page():
	lecturer_obj = lecturer()
	login = lecturer_obj.login()
	if login:
		pass
	else:
		print("用户登陆失败！！")
		sys.exit()