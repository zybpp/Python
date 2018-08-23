#!/usr/bin/env python3
# -*- coding: utf-8 -*-

name = input('请输入学生姓名：')
grade1 = input('2017年分数：')
grade2 = input('2018年分数：')
grade1 = float(grade1)
grade2 = float(grade2)
per = (grade2 - grade1) / grade1 * 100
print('学生%s2018年分数较2017分数增长率为：%.2f' %(name,per))