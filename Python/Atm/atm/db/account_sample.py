#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:zpp

import json
from db import *
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
account_key = ["name", "password", "unlock", "lump_sum", "balance"]
account_value = ["abc","abc",1,15000,15000]

def init(name,password):
	#print(os.getcwd())
	dir = BASE_DIR + "\\db\\accounts"
	os.chdir(dir)
	#print(os.getcwd())
	account_name = name + ".json"
	f = open(account_name,"w")
	account = dict(zip(account_key,account_value))
	account["name"] = name
	account["password"] = password
	lump_sum = input("Please input your lump sum.:")
	if lump_sum:
		account["lump_sum"] = lump_sum
		account["balance"] = lump_sum
	json.dump(account,f)
	f.close()
