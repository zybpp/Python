#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:zhangyanbin

import os
import subprocess
import sys

# FileName = sys.argv[1]
FileName = "package"
FileName_Base = FileName + "_base"

os.system('adb version')
os.system('adb devices')  # os.system是不支持读取操作的
# os.system('adb shell "pm list packages -f --show-versionname --show-appname"')
file = open(FileName, "w",encoding = "utf-8")
out = subprocess.Popen('adb shell "pm list packages -f --show-versionname --show-appname"', shell=True,
                       stdout=subprocess.PIPE)
# out = os.popen('adb shell "pm list packages -f --show-versionname --show-appname"').read()  # os.popen支持读取操作
data = out.stdout.read().decode("utf-8")
file.write(data)
file.close()
with open(FileName, "r",encoding = "utf-8") as file,open(FileName_Base, "w",encoding = "utf-8") as file_base:
	for line in file:
		if line == '\n':
			line = line.strip("\n")
		file_base.write(line)

with open(FileName_Base, "r",encoding = "utf-8") as file_base,open(FileName, "w",encoding = "utf-8") as file:
	for line in file_base:
		if line.startswith("package"):
			list = line.partition("=")
			path = list[0].partition(":")[2]
			cmd = 'adb shell "ls -l {}"'.format(path)
			size_list = subprocess.Popen(cmd, shell=True,stdout=subprocess.PIPE).stdout.read().decode("utf-8")
			#size = int(size_list.split()[4])/1024/1024
			size = size_list.split()[4]
			size_str = ":size:" + size + "\n"
			line = line.strip("\n") + size_str
		file.write(line)
os.remove(FileName_Base)


