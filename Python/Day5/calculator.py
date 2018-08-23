#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:zpp

import re

def adder_subtractor(x,y):
	return x + y

def multiply_divide(x,y):
	return x * y

def bracket(s):
	pass

def main():
	operation = input("Please input operation:").strip()
	num = re.search("\(+.+\)","(((1 + 3) * (5 - 2)) * 4)/5")
	print(num)

main()
