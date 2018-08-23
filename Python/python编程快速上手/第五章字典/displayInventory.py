#!/usr/bin/env python3
# -*- coding: utf-8 -*-

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(dict):
	print("Inventory:")
	count_total = 0
	for k,v in dict.items():
		print(str(v) + " " + k)
		count_total += v
	print("Total number of items:%d" %count_total)

if __name__ == "__main__":
	displayInventory(stuff)