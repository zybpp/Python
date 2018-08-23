#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:zpp

message = "It was a bright cold day in April, and the clocks were striking thirteen."
count = {}

for character in message:
	count.setdefault(character,0)
	count[character] += 1

print(count)