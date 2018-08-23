#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:zpp

list_1 = [1,4,3,4,5,3,7,4,9]
#生成集合,无序的
list_1 = set(list_1)

print(list_1,type(list_1))
list_2 = set([1,3,4,8])

#交集     &
print(list_1.intersection(list_2))
#并集     |
print(list_1.union(list_2))
#差集 in list_1 but not in list_2     -
print(list_1.difference(list_2))

list_3 = set([1,3,4])
#子集
print(list_1.issubset(list_2))
#父集
print(list_1.issuperset(list_2))
print(list_1.issuperset(list_3))

#对称差集       ^
print(list_1.symmetric_difference(list_2))
#若没有交集返回True
list_4 = set([7,5,6])
print(list_3.isdisjoint(list_4))

#添加
list_1.add(88)
print(list_1)
#批量添加
list_1.update([22,33,44])
print(list_1)
#删除某个元素，如果不存在，就报错
list_1.remove(33)
print(list_1)
#任意删除
list_1.pop()
print(list_1)
#删除某个元素，如果不存在，就什么都不做
list_1.discard(99)
print(list_1)