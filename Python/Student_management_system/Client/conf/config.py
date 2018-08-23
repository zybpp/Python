#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:zpp

from core import lecturer
from core import student

sys_port = {
	"lecturer": lecturer.lecturer_page,
	"student": student.student_page
}

account_info = {
	"login": "yes",
	"way": "",
	"name": "",
	"password": "",
	"new": "no"
}

auth_return = {
	"1001": "登陆成功！！",
	"1002": "账号或密码错误，是否重新输入？('y' or 'n')>>",
	"1003": "账号不存在，是否注册新账户？('y' or 'n')>>",
	"1004": "恭喜，新账户创建成功！！"
}