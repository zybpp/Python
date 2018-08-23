#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:zpp

face = {'pro':1, 'oop':2}
pro = ['c', 'vb']
oop = ['java', 'c++', 'python']

print("Programming")
one_menu = input('please select one menu:')
if one_menu:
	for key in face.keys():
		print(key, end=" ", flush=True)
	print('\n')
	two_menu = input('please select two menu:')
	if two_menu == 'd':
		print("Programming")
	elif two_menu == '1':
		for menu in pro:
			print(menu, end=" ", flush=True)
		print('\n')
		thr_menu = input('please select three menu:')
		if thr_menu == 'd':
			print("Programming")
	elif two_menu == '2':
		for menu in oop:
			print(menu, end=" ", flush=True)
		print('\n')
		thr_menu = input('please select three menu:')
