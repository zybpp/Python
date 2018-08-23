#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:zpp

a1 = [4,6,13,24,26,42,87]
a2 = [2,4,13,34,42,55,65,76,89]
new = []

def f(x, l=[]):
	print(id(l))
	for i in range(x):
		l.append(i**2)
	print(id(l))
	print(l)
	print("#########")

#print(id(f.__defaults__))
f(2)  # [0, 1]
#print(id(f.__defaults__))
f(3, [3, 2, 1])  # [3, 2, 1, 0, 1, 4]
#print(id(f.__defaults__))
f(3)  # [0, 1, 0, 1, 4]
#print(id(f.__defaults__))
f(4)