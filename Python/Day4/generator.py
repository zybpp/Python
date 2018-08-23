#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:zpp

def fib(max):
	n, a, b = 0, 0, 1
	while n < max:
		yield b
		a, b = b, a+b
		n += 1
	return "####"

f = fib(10)
print(f.__next__())
# while True:
# 	try:
# 		x = f.__next__()
# 		print("f:",x)
# 	except StopIteration as e:
# 		print("Generator return value:",e.value)
# 		break
