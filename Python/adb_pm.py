#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:zhangyanbin

import os
import subprocess
import sys
import threading

#FileName = sys.argv[1]
FileName = "abc"
FileName_Base = FileName + "_base"

os.system('adb version')
os.system('adb devices')  # os.system是不支持读取操作的
file = open(FileName, "w",encoding = "utf-8")
out = subprocess.Popen('adb shell "pm list packages -f --show-versionname --show-appname"', shell=True,
                       stdout=subprocess.PIPE)
data = out.stdout.read().decode("utf-8")
file.write(data)
file.close()
with open(FileName, "r",encoding = "utf-8") as file,open(FileName_Base, "w",encoding = "utf-8") as file_base:
	for line in file:
		if line == '\n':
			line = line.strip("\n")
		file_base.write(line)

def cmd_ls(line):
	with open(FileName, "a", encoding="utf-8") as file:
		if line.startswith("package"):
			list = line.partition("=")
			path = list[0].partition(":")[2]
			cmd = 'adb shell "ls -l {}"'.format(path)
			size_list = subprocess.Popen(cmd, shell=True,stdout=subprocess.PIPE).stdout.read().decode("utf-8")
			size = str(round(int(size_list.split()[4])/1024,2))
			size_str = ":size:" + size + "KB" + "\n"
			line = line.strip("\n") + size_str
		file.write(line)

thd = []
with open(FileName_Base, "r",encoding = "utf-8") as file_base:
	print("正在获取对应apk size")
	os.remove(FileName)
	for line in file_base:
		cmd = threading.Thread(target=cmd_ls,args=(line,))
		cmd.start()
		thd.append(cmd)

for t in thd:
	t.join()

os.remove(FileName_Base)
print("成功获取apk size")


