#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:zhangyanbin

import os
import sys
import shutil
import re
import subprocess
import time
import asyncio

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
sem = asyncio.Semaphore(1000)

def file_list(path):
	for file in os.listdir(path):
		yield file

async def copy_files(file,orig_dir_sub):
	sem.acquire()
	sub_file_path = ""
	sub_name = file
	#if sub_name in os.listdir(orig_dir):
	sub_file_path = orig_dir + "\\" + sub_name
	shutil.copy(sub_file_path, orig_dir_sub)
	sem.release()

async def keymaster_async(orig_path,obj_path,deviceid):
	sem.acquire()
	obj_file_path = obj_path + "\\" + deviceid + ".xml"
	if not os.path.isfile(obj_file_path):
		shutil.copy(orig_path,obj_file_path)
	else:
		print("文件 %s.xml 已存在" % (deviceid))
	sem.release()

async def widevine_async(orig_path,obj_path,deviceid):
	sem.acquire()
	delete_log = True
	obj_file_path = obj_path + "\\" + deviceid
	#if os.path.isdir(obj_file_path):
	#	shutil.rmtree(obj_file_path)
	if not os.path.isdir(obj_file_path):
		os.makedirs(obj_file_path)
	filename = "widevine_" + deviceid + ".txt"
	if len(os.listdir(obj_file_path)) == 0:
		with open(filename, "w") as perl_file:
			perlcmd = 'perl turn_thread.pl "{}" {}'.format(orig_path,deviceid)
			popfile = subprocess.Popen(perlcmd,stdout=perl_file,stderr=subprocess.PIPE)
			await asyncio.sleep(1)
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
	sem.release()

# async def keymaster_async(orig_path,obj_path,deviceid):
# 	keymaster(orig_path, obj_path, deviceid)

# async def widevine_async(orig_path,obj_path,deviceid):
# 	widevine(orig_path, obj_path, deviceid)

if os.path.isdir(orig_dir):
	deviceid = None
	keybox_list = []
	tasks = []
	copy_tasks = []
	files = file_list(orig_dir)
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
	"""time = (end - start)//10000
	remainder = (end - start)%10000
	if time > 0:
		for i in range(time + 1):
			start = i*10000
			if i == time:
				end = start + remainder
			else:
				end = start + 10000
			orig_dir_sub = orig_dir + "_sub" + str(i)
			os.makedirs(orig_dir_sub)
			id = start
			for file in files:
				copy_tasks.append(asyncio.ensure_future(copy_files(file,orig_dir_sub)))
				id +=1
				if id == end:
					break
			copy_loop = asyncio.get_event_loop()
			copy_loop.run_until_complete(asyncio.wait(copy_tasks))
			for id in keybox_list[start:end]:
				if len(os.listdir(orig_dir_sub)) > 0:
					file_name = re.sub("-(\d+).", "-" + id + ".", os.listdir(orig_dir_sub)[0])
					if file_name in os.listdir(orig_dir_sub):
						orig_file_path = orig_dir_sub + "\\" + file_name
						with open(orig_file_path, "r") as orig_file:
							for line in orig_file:
								if len(re.findall("DeviceID=\"(\w+)\"", line)) > 0:
									deviceid = re.findall("DeviceID=\"(\w+)\"", line)[0]
									break
						if sys.argv[2] == "keymaster":
							tasks.append(asyncio.ensure_future(keymaster_async(orig_file_path,obj_dir,deviceid)))
						elif sys.argv[2] == "widevine":
							tasks.append(asyncio.ensure_future(widevine_async(orig_file_path,obj_dir,deviceid)))
						total = total + 1
					else:
						print("文件：%s  不存在" %file_name)
			loop = asyncio.get_event_loop()
			loop.run_until_complete(asyncio.wait(tasks))
	else:"""
	if True:
		for file in files:
			#if len(os.listdir(orig_dir)) > 0:
			if True:
				file_name = file
				print(file_name)
				if True:
					orig_file_path = orig_dir + "\\" + file_name
					with open(orig_file_path, "r") as orig_file:
						for line in orig_file:
							if len(re.findall("DeviceID=\"(\w+)\"", line)) > 0:
								deviceid = re.findall("DeviceID=\"(\w+)\"", line)[0]
								break
					if sys.argv[2] == "keymaster":
						tasks.append(asyncio.ensure_future(keymaster_async(orig_file_path, obj_dir, deviceid)))
					elif sys.argv[2] == "widevine":
						tasks.append(asyncio.ensure_future(widevine_async(orig_file_path, obj_dir, deviceid)))
					total = total + 1
				else:
					print("文件：%s  不存在" % file_name)
		loop = asyncio.get_event_loop()
		loop.run_until_complete(asyncio.wait(tasks))
	if len(os.listdir(obj_dir)) == total:
		#for i in range(len(os.listdir(BASE_DIR + "\\" + sys.argv[1]))):
		#	shutil.rmtree(orig_dir + "_sub" + str(i))
		print("%s 执行完成！！" %(sys.argv[2]))
else:
	print("无此项目,请重新输入，谢谢！！")
