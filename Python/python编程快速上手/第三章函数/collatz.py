#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:zpp

def collatz(number):
	if number%2 == 0:
		return number//2
	elif number%2 == 1:
		return (3*number + 1)

print("Please enter number:")
num = int(input())
while True:
	num = collatz(num)
	print(str(num))
	if num == 1:
		break