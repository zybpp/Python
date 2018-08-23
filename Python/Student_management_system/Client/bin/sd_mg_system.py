#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:zpp
import os,sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)
sys.path.append(BASE_DIR)

if __name__ == "__main__" :
	from core import views
	views.main()

