#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:zpp

def addToInventory(inventory, addedItems):
	for drag in addedItems:
		inventory.setdefault(drag,0)
		inventory[drag] += 1
	return inventory

def displayInventory(inventory):
	print("Inventory:")
	total = 0
	for k,v in inventory.items():
		print(str(v) + " " + k)
		total += v
	print("Total number of items: ",str(total))

if __name__ == "__main__":
	inv = {'gold coin': 42, 'rope': 1}
	dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
	inv = addToInventory(inv, dragonLoot)
	displayInventory(inv)