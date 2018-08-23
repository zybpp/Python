#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:zpp

import socket
import json
import hashlib
import os

class FtpClient(object):
	'''
	The clsss id ftp client class.
	'''
	def __init__(self):
		self.client = socket.socket()
		self.inf = {}
		self.msg = {}
		self.path = ""

	def help(self):
		msg = '''
		ls
		pwd
		cd ../..
		mkdir dir
		get filename
		put filename
		'''
		print("The command is :",msg)

	def connect(self,host,port):
		self.client.connect((host, port))

	def client_inf(self,new):
		m = hashlib.md5()
		name = input("Please input your name:").strip()
		password = input("Please input your password:").strip()
		m.update(password.encode("utf-8"))
		password_md5 = m.hexdigest()
		self.inf = {
			"login": "yes",
			"name": name,
			"password": password_md5,
			"new": "no"
		}
		if new == "yes":
			self.inf["new"] = "yes"
		return self.inf

	def login(self):
		new = "no"
		while True:
			client_msg = self.client_inf(new)
			self.client.send(json.dumps(client_msg).encode("utf-8"))
			login_state = self.client.recv(1024).decode("utf-8")
			if login_state == "correct":
				self.path = client_msg["name"]
				print("%s, Welcome to the FTP." %client_msg["name"])
				break
			elif login_state == "fail":
				again = input("Wrong password, please enter again?(y or n):").strip()
				if again == "n":
					return False
			elif login_state == "none":
				new = input("The user does not exist, whether the new user?(y or n):").strip()
				if new == "y":
					new = "yes"
				elif new == "n":
					return False
		return True

	def interactive(self):
		while True:
			cmd = input("%s>>" %self.path).strip()
			if len(cmd) == 0: continue
			cmd_str = cmd.split()[0]
			if hasattr(self,"cmd_%s" %cmd_str):
				func = getattr(self,"cmd_%s" %cmd_str)
				func(cmd)
			else:
				self.help()

	def command_single(self,*args):
		cmd = args[0].split()
		server_response = ""
		if len(cmd) > 1:
			self.help()
		else:
			self.msg = {
				"action" : cmd[0]
			}
			self.client.send(json.dumps(self.msg).encode("utf-8"))
			server_response = self.client.recv(1024).decode("utf-8")
		return  server_response

	def commend_multi(self,*args):
		cmd = args[0].split()
		server_response = ""
		if len(cmd) > 1:
			self.msg = {
				"action" : cmd[0],
				"target" : cmd[1]
			}
			self.client.send(json.dumps(self.msg).encode("utf-8"))
			server_response = self.client.recv(1024).decode("utf-8")
		else:
			self.help()
		return server_response

	def cmd_ls(self,*args):
		server_response = json.loads(self.command_single(args[0]))
		for i in server_response:
			print(i)

	def cmd_pwd(self,*args):
		server_response = self.command_single(args[0])
		print(server_response)

	def cmd_cd(self,*args):
		self.commend_multi(*args)

	def cmd_mkdir(self,*args):
		cmd = args[0].split()
		if len(cmd) > 1:
			self.help()
		else:
			self.msg = {
				"action" : cmd[0]
			}
			self.client.send(json.dumps(self.msg).encode("utf-8"))

	def cmd_put(self,*args):
		cmd = args[0].split()
		if len(cmd) > 1:
			filename = cmd[1]
			if cmd[0] == "put" and os.path.isfile(filename):
				self.client.send(cmd.encode("utf-8"))
				recv = self.client.recv(1024)
			elif cmd[0] == "get":
				pass
			elif cmd[0] == "cd":
				pass
		else:
			self.help()

	def cmd_get(self,*args):
		cmd = args[0].split()
		if len(cmd) > 1:
			self.help()
		else:
			self.msg = {
				"action" : cmd[0]
			}
			self.client.send(json.dumps(self.msg).encode("utf-8"))

	def close(self):
		print("client is close")
		self.close()


client = FtpClient()
client.connect('localhost',9999)
login_state = client.login()
if login_state:
	client.interactive()

client.close()


