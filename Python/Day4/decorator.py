#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:zpp

import time
user,passwd = 'aaa','abc123'
def auth(auth_type):
    print("auth func:",auth_type)
    def outer_wrapper(func):
        def wrapper(*args, **kwargs):
            print("wrapper func args:", *args, **kwargs)
            if auth_type == "local":
                username = input("Username:").strip()
                password = input("Password:").strip()
                print("Username:", username)
                print("Password:", password)
                print("User:", user)
                print("Passwd:", passwd)
                if user == username and passwd == password:
                    print("\033[32;1mUser has passed authentication\033[0m")
                    res = func(*args, **kwargs)  # from home
                    print("---after authenticaion ")
                    return res
                else:
                    exit("\033[31;1mInvalid username or password\033[0m")
            elif auth_type == "ldap":
                print("搞毛线ldap,不会。。。。")
        return wrapper
    return outer_wrapper


def index():
	print("Welcome to index page")

@auth(auth_type="local") # home = wrapper
def home():
	print("Welcome to home page")
	return "form home"

@auth(auth_type="ldap")
def bbs():
	print("Welcome to user page")

index()
print(home())
bbs()
