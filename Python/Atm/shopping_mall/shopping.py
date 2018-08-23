#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:zpp

import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

import json
from atm import *

prod_list = {"iphone":5800, "asus":1588, "huawei":2888, "xiaomi":1988, "oppo":2188, "vivo":2588, "meizu":2288}
cart = []

def login():
	print("Welcome login shopping mall!!")

def show_prods():
	for i in prod_list:
		print("%s   %s" %(i,prod_list[i]))

def add_cart(prod):
	cart.append(prod)

def show_cart():
	sum = 0
	if cart:
		for i in cart:
			print("%s   %s" % (i, prod_list[i]))
			sum = sum + prod_list[i]
		print("You products sum is:",sum)
		action = input("What are you doing?( 'q' > quit, 'd' > delete)>>>")
		if action is "d":
			while True:
				del_prod = input("Please enter the item to be deleted.( 'q' > quit,or delete product)>>>")
				if del_prod is "q":
					break
				else:
					cart.remove(del_prod)
					for i in cart:
						print("%s   %s" % (i, prod_list[i]))
					sum = sum - prod_list[del_prod]
					print("You products sum is:", sum)
		elif action is "q":
			pass
	else:
		print("Your shopping cart is empty!!")

def buy():
	sum = 0
	for i in cart:
		sum = sum + prod_list[i]
	with open("sum.json","w") as f:
		json.dump(sum,f)


def shopping():
	login()
	show_prods()
	while True:
		action = input("What are you doing?( 'i'> Inquire,'b' > Buy ,'q' > quit,or add products)>>>")
		if action is "i":
			show_cart()
		elif action is "b":
			buy()
		elif action is "q":
			break
		else:
			add_cart(action)

shopping()



