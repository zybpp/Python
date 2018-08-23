#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:zpp

salay = int(input("your salay:"))
line = [1, 2, 3, 4, 5]
goods = ["Iphone", "Mac Pro", "Starbuck Latte", "Python book", "Bike"]
price = [5800, 12000, 31, 58, 800]
buy = []

while True:
	for i in range(5):
		print("{0}.{1}    {2}".format(line[i],goods[i],price[i]))
	total = 0
	shop = input(">>>:")
	buy_len = len(buy)
	if shop is not "q":
		shop = int(shop) - 1
		if buy_len > 0:
			for i in buy:
				total += int(price[i])
			total = total + int(price[shop])
			print("total = ", total)
			if total > salay:
				print("I'm sorry, your balance is insufficient!!")
			else:
				buy.append(shop)
		else:
			if price[shop] > salay:
				print("I'm sorry, your balance is insufficient!!")
			else:
				buy.append(shop)
	else:
		if buy_len > 0:
			print("Your shopping cart is:")
			for i in buy:
				total += int(price[i])
				print("{0}  {1}".format(goods[i],price[i]))
			print("Your total amount of goods: ",total)
		else:
			print("Your shopping cart is empty!!")
		break
