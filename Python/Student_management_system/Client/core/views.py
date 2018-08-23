#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:zpp
import sys
from conf import config

def main():
	"""
	进入程序
	:return:
	"""
	print("""请输入登陆方式：
	1、讲师
	2、学员""")
	while True:
		way = input(">>")
		if way == "1":
			config.sys_port["lecturer"]()
		elif way == "2":
			config.sys_port["student"]()
		elif way == "q":
			sys.exit()
		elif way != "":
			print("输入错误，请输入登陆方式序号，谢谢。")