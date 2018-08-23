#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:zpp

import re

def own_strip(str,replace=None):
	if replace == None:
		replaceRegex = re.compile(r"(^\s*)(\S.*\S)(\s*$)",re.DOTALL)
		string = replaceRegex.search(str)
		return string[2]

if __name__ == "__main__":
	while True:
		str = input("请输入内容:")
		new_str = own_strip(str)
		print(new_str)
