#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:zpp

import json
import os
from db import account_sample
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
dir = BASE_DIR + "\\db\\accounts"
os.chdir(dir)

def auth_decoration(func):
	def decoration(*args,**kwargs):
		account_name = args[0] + ".json"
		if os.path.exists(account_name):
			func(*args,**kwargs)
		else:
			new = input("Your account was not found, do you need new?(n or y):")
			if new == "y":
				account_sample.init(*args,**kwargs)
				print("Congratulations on your successful login authentication!!")
				f = open(account_name,"r")
				data = json.load(f)
				f.close()
				return data
			elif new == "n":
				print("Welcome to atm home page!!")
	return decoration

@auth_decoration
def auth(name,password):
	account_name = name + ".json"
	f = open(account_name,"r")
	data = json.load(f)
	count = 0
	if data["unlock"]:
		while count < 3:
			if password == data["password"]:
				print("Congratulations on your successful login authentication!!")
				return data
			else:
				count += 1
				if count < 3:
					print("The password was entered incorrectly %s times, Your have %s times." %(count,(3 - count)))
					password = input("Please input your password:")
				else:
					data["unlock"] = 0
					f = open(account_name, "w")
					json.dump(data,f)
					print("The password was entered incorrectly three times, Your account is locked.")
					return False
	else:
		print("Your account is locked.")
		return False
	f.close()

