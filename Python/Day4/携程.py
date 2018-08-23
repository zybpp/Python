#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:zpp

import time

def consumer(name):
	print("%s 准备吃包子！" %(name))
	while True:
		baozi = yield
		print("包子[%s]来了，被[%s]吃了。" %(baozi,name))

def producer(name,number):
	c = consumer("A")
	c2 = consumer("B")
	c.__next__()
	c2.__next__()
	print("[%s]开始做包子了！" %(name))
	for i in range(number):
		time.sleep(1)
		print("做了一个包子。")
		c.send(i)
		c2.send(i)

producer("zhangpp",10)
