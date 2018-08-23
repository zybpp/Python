#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:zpp

import socketserver
import json
import os

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ACCOUNT_PATH = BASE_PATH + "\\conf"
DATA_PATH = BASE_PATH + "\\data"
print(DATA_PATH)

class MyFTPHandler(socketserver.BaseRequestHandler):
	'''
	The request handler class for ftp server.
	'''

	def __init__(self, request, client_address, server):
		super(MyFTPHandler, self).__init__(request, client_address, server)
		self.user_current_dir = ""
		self.home_dir = ""

	def handle(self):
		while True:
			try:
				print("client address:",self.client_address[0])
				self.data = self.request.recv(1024).strip()
				print("{} wrote:".format(self.client_address[0]))
				print(self.data.decode())
				client_msg = json.loads(self.data.decode())
				if client_msg.get("login") == "yes":
					self.login_verify(client_msg)
				else:
					self.own_operation(client_msg)
			except ConnectionResetError as e:
				print("error",e)
				break

	def login_verify(self,client_msg):
		print("login verify:",client_msg)
		name = client_msg["name"]
		account_file = ACCOUNT_PATH + "\\" + name
		own_path = DATA_PATH + "\\" + name
		self.user_current_dir = own_path
		self.home_dir = own_path
		print(own_path)
		if client_msg["new"] == "yes":
			own_msg_dir = {"name": "",
			               "password": "",
			               "disk": "100M"}
			os.makedirs(own_path)
			own_msg_dir["name"] = client_msg["name"]
			own_msg_dir["password"] = client_msg["password"]
			with open(account_file,"w") as f:
				json.dump(own_msg_dir,f)
			self.request.send(b"correct")
		else:
			if os.path.isfile(account_file):
				with open(account_file,"r") as f:
					account_msg = json.load(f)
				if account_msg["name"] == client_msg["name"] and account_msg["password"] == client_msg["password"]:
					self.request.send(b"correct")
				else:
					self.request.send(b"fail")
			else:
				self.request.send(b"none")

	def own_operation(self,client_msg):
		action = client_msg["action"]
		if hasattr(self, "cmd_%s" % action):
			func = getattr(self, "cmd_%s" % action)
			func(client_msg)

	def cmd_ls(self,*args):
		print("This is ls commend")
		print(self.user_current_dir)
		data = os.listdir(self.user_current_dir)
		self.request.send(json.dumps(data).encode("utf-8"))

	def cmd_pwd(self,*args):
		print("This is pwd commend")
		self.request.send(self.user_current_dir.encode("utf-8"))

	def cmd_cd(self,*args):
		print("This is ls commend")
		target = args[0]["target"]
		if target:
			pass
		target_path = self.user_current_dir + target
		if os.path.isdir(target_path):
			self.user_current_dir = target_path

		elif os.path.isfile(target_path):
			self.request.send("Your action object is a file!!".encode("utf-8"))


	def cmd_mkdir(self,*args):
		pass

	def cmd_get(self,*args):
		pass

	def cmd_put(self,*args):
		pass

if __name__ == "__main__":
	HOST, PORT = "localhost", 9999

	server = socketserver.ThreadingTCPServer((HOST, PORT),MyFTPHandler)
	server.serve_forever()