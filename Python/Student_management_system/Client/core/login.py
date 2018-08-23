#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:zpp

import socket
import json
from conf import config

lec_client = socket.socket()
addr = ("localhost", 9999)

def auth( name, password):
	"""
	Check account and password.
	"""
	lec_client.connect(addr)
	account_info["name"] = name
	account_info["password"] = password
	lec_client.send(json.dumps(account_info).encode("utf-8"))
	auth_result = lec_client.recv(1024).decode("utf-8")
	return auth_result


def new_account():
	"""
	New account.
	"""
	while True:
		name = input("请输入新用户名：")
		password = input("请输入密码：")
		if len(name) > 0 and len(password) > 0:
			account_info["name"] = name
			account_info["password"] = password
			account_info["new"] = "yes"
			lec_client.send(json.dumps(account_info).encode("utf-8"))
			new_result = lec_client.recv(1024).decode("utf-8")
			return new_result
		else:
			print("新用户名或密码输入有误！！")


def login(way):
	"""
	Login account.
	"""
	global account_info
	account_info  = config.account_info
	while True:
		name = input("请输入用户名：")
		password = input("请输入密码：")
		account_info["way"] = way
		if len(name) > 0:
			auth_result = auth(name, password)
		else:
			print("用户名未输入！！")
			continue
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
					new_result = new_account()
					if new_result == "1004":
						print(config.auth_return[new_result])
						return True
					else:
						return False
				elif new == "n":
					return False
				elif new != "":
					print("输入有误！！")