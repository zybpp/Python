#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:zpp

name = "My name is ZhangPP"
age = "-"
age_list = ['m','y',' ','a','g','e']
s1 = "I am {},I'm {} years old！"
s2 = "I am {1},I'm {0} years old！"
s3 = "I am {name},I'm {age} years old！"

print(name)
print(name.index("is"))    ##获取首字符索引
print(name.find("me"))     ##搜索到字符，并返回首字符索引
print(name.count("a"))     ##统计字符出现的次数
print(name.strip())        ##去掉字符前后空格
print(name.split("n"))     ##分割字符，返回列表
print(name.replace("zhangpp","zhangtt"))    ##替换字符
print(age.join(age_list))       ##将列表以指定字符拼接成新的字符串
print(s1.format("zhangpp","27"))
print(s2.format("27","zhangpp"))
print(s3.format(name = "zhangpp", age = "27"))    ##字符串格式化，传参
print(name.encode('utf-8'))         ##对字符进行编码
print(name.encode('utf-8').decode('utf-8'))         ##解码字符串
print(name.title())         ##字符串以Title形式显示
print(name.startswith("my"))        ##字符串是否以my字符开头
print(name.endswith("tt"))          ##字符串是否以tt字符结尾
print(name.upper())                 ##字符串改为大写
print(name.lower())                 ##字符串改为小写
print(name.swapcase())              ##字符串大小写转换
print(name.center(50,"*"))
print(name.find('am',5))