#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:zpp

tableData = [['apples', 'oranges', 'cherries', 'banana'],
			['Alice', 'Bob', 'Carol', 'David'],
			['dogs', 'cats', 'moose', 'goose']]

def printTable(list):
	length = 0
	if len(list) > 0:
		for i in range(len(list)):
			for j in range(len(list[i])):
				if len(list[i][j]) > length:
					length = len(list[i][j])
	for i in range(len(list[0])):
		for j in range(len(list)):
			#list[j][i].rjust(colWidths[j])
			print(list[j][i].rjust(length),end="")
		print()

if __name__ == "__main__":
	printTable(tableData)