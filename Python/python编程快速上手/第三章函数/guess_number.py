#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:zpp
# This is a guess the number game.
import random

secretNumber = random.randint(1,20)
print("I am thinking of a number between 1 and 20,you can only guess at most six times.")

for i in range(1,7):
	print("Take a guess.")
	num = int(input())
	if num < secretNumber:
		print("Your guess is too low.")
	elif num > secretNumber:
		print("Your guess is too high.")
	else:
		print("Good job! You guessed my number in " + str(i) + " guesses!")
		break
if num != secretNumber:
	print("Nope. The number I was thinking of was " + str(secretNumber))


