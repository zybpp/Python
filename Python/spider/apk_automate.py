#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:zpp

import requests
import re
import sys
import urllib
import socket

class spider(object):
	"""
		getsource :
		geteveryapp:
		saveinfo:
		saveinfo:
	"""
	def __init__(self):
		print("开始爬取豌豆荚网页上下载排名前1000 apk应用".center(50,"-"))

	def getsource(self,url):
		html = requests.get(url)
		return html.text

	def geteveryapp(self, source):
		everyapp = re.findall('<li.*? class="card".*?</li>', source, re.S)
		return everyapp

	def getinfo(self, eachclass):
		str1 = re.findall('<a data-app-id=.*?href=.*?>', eachclass, re.S)
		app_name = re.search('"(.*?)"',re.search('data-app-name=".*?"', str1[0]).group(0)).group(0).split("\"")[1]
		app_url = re.search('"(.*?)"', re.search('href=".*?"', str1[0]).group(0)).group(0).split("\"")[1]
		info = {app_name:app_url}
		return info

	def saveinfo(self, classinfo):
		with open('apk_info', 'w',encoding="utf-8") as f:
			for each in classinfo:
				f.write(str(each))
				f.write("\n")

	def auto_down(self, url):
		try:
			requests.post(url)
		except socket.timeout:
			count = 1
			while count <= 15:
				try:
					urllib.urlretrieve(url, filename)
					break
				except socket.timeout:
					err_info = 'Reloading for %d time' % count if count == 1 else 'Reloading for %d times' % count
					print(err_info)
					count += 1
			if count > 15:
				print("下载失败")

class phone(object):
	def __init__(self):
		pass

	def install(self):
		pass

	def uninstall(self):
		pass

if __name__ == '__main__':
	appinfo = []
	url = 'http://www.wandoujia.com/top/app'
	appurl = spider()
	html = appurl.getsource(url)
	every_app = appurl.geteveryapp(html)
	for each in every_app:
		info = appurl.getinfo(each)
		appinfo.append(info)
	print(appinfo)
	appurl.saveinfo(appinfo)
	for app in appinfo:
		app_name = list(app.keys())[0]
		app_url = list(app.values())[0]
		print("app name : %s , app url : %s" %(app_name,app_url))
		appurl.auto_down(app_url)
