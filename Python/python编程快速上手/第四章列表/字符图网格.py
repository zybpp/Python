#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:zpp

grid = [['.', '.', '.', '.', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['O', 'O', 'O', 'O', 'O', '.'],
['.', 'O', 'O', 'O', 'O', 'O'],
['O', 'O', 'O', 'O', 'O', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['.', '.', '.', '.', '.', '.']]

def landscape(list):
	len1 = len(list)
	len2 = len(list[0])
	for i in range(len2):
		for j in range(len1):
			print(list[j][i],end="")
		print()

if __name__ == "__main__":
	landscape(grid)