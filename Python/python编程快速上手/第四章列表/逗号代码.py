#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:zpp

def listToStr(list):
	str = ""
	for l in list:
		if l == list[-1]:
			str = str + "and " + l
		else:
			str = str + l +", "
	print(str)

spam = ['apples', 'bananas', 'tofu', 'cats']
listToStr(spam)