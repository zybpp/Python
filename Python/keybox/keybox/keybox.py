#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:zhangyanbin

import os
import sys
import shutil
import re
import subprocess
import time

"""
	python keybox.py product model start end
	参数解析： 
	product 为项目名，如X705F，X705L，X705M
	model 为需要操作的keybox，如keymaster或widevine
	start 为需要操作keybox起始文件名，参数为数字，如0，1，2，3 ...（可为空，默认值为0）
	end 为需要操作keybox结束文件名，参数为数字，如0，1，2，3 ...（可为空，默认值为model目录下文件数目）
"""
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
orig_dir = BASE_DIR + "\\" + sys.argv[1] + "\\" + sys.argv[2]

def keymaster(orig_path,obj_path,deviceid):
	obj_file_path = obj_path + "\\" + deviceid + ".xml"
	if not os.path.isfile(obj_file_path):
		shutil.copy(orig_path,obj_file_path)
	else:
		print("文件 %s.xml 已存在" % (deviceid))

def widevine(orig_path,obj_path,deviceid):
	delete_log = True
	obj_file_path = obj_path + "\\" + deviceid
	#if os.path.isdir(obj_file_path):
	#	shutil.rmtree(obj_file_path)
	if not os.path.isdir(obj_file_path):
		os.makedirs(obj_file_path)
	filename = "widevine_" + deviceid + ".txt"
	file = open(filename,"w")
	file.writ
	if len(os.listdir(obj_file_path)) == 0:
		with open(filename, "w") as perl_file:
			perlcmd = 'perl turn.pl "{}" {}'.format(orig_path,deviceid)
			popfile = subprocess.Popen(perlcmd,stdout=perl_file,stderr=subprocess.PIPE)
			time.sleep(0.5)
		with open(filename, "r") as updatefile:
			for line in updatefile:
				if line.startswith("Parsing keybox data succeeds") and os.path.isfile(deviceid + "_keybox.bin"):
					print("DeviceId 为%s的keybox.bin转换成功" %deviceid)
					shutil.move(deviceid + "_keybox.bin", obj_file_path + "\\keybox.bin")
					break
			else:
				delete_log = False
				print("DeviceId 为%s的keybox.bin转换失败" % deviceid)
		if delete_log == True:
			os.unlink(filename)
		#popfile.terminate()
	else:
		print("文件 %s %s 已存在" %(deviceid,os.listdir(obj_file_path)[0]))

if os.path.isdir(orig_dir):
	deviceid = None
	keybox_list = []
	obj_dir = BASE_DIR + "\\" + sys.argv[1] + "_update" + "\\" + sys.argv[2]
	#if os.path.isdir(obj_dir):
	#	shutil.rmtree(obj_dir)
	if not os.path.isdir(obj_dir):
		os.makedirs(obj_dir)
	for name in os.listdir(orig_dir):
		keybox_list.append(re.findall("-(\d+).",name)[0])
	keybox_list.sort()
	start = int(sys.argv[3]) if len(sys.argv)>3 else 0
	end = (int(sys.argv[4]) + 1) if len(sys.argv)>4 else len(os.listdir(orig_dir))
	total = 0
	for i in keybox_list[start:end]:
		if len(os.listdir(orig_dir)) > 0:
			file_name = re.sub("-(\d+).", "-" + i + ".", os.listdir(orig_dir)[0])
			if file_name in os.listdir(orig_dir):
				orig_file_path = orig_dir + "\\" + file_name
				with open(orig_file_path, "r") as orig_file:
					for line in orig_file:
						if len(re.findall("DeviceID=\"(\w+)\"", line)) > 0:
							deviceid = re.findall("DeviceID=\"(\w+)\"", line)[0]
							break
				if sys.argv[2] == "keymaster":
					keymaster(orig_file_path,obj_dir,deviceid)
				elif sys.argv[2] == "widevine":
					widevine(orig_file_path,obj_dir,deviceid)
				total = total + 1
			else:
				print("文件：%s  不存在" %file_name)
	if len(os.listdir(obj_dir)) == total:
		print("%s 执行完成！！" %(sys.argv[2]))
else:
	print("无此项目,请重新输入，谢谢！！")
