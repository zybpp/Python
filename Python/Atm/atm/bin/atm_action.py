#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:zpp

import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)
sys.path.append(BASE_DIR)

from core import main

main.main()