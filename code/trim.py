# -*- coding: utf-8 -*-
def trim(s):
    for i in range(len(s)):
        if s[i:i+1] != ' ':
            s = s[i:len(s)]
            break
    print(s)
    for i in range(len(s)):
        if s[-i-2:-i-1] != ' ':
            if i == 0:
                s = s[-len(s):]
            else:
                s = s[-len(s):-i-1]
            break
    return s

# 测试:
if trim('hello  ') != 'hello':
	print(111)
	s = trim('hello  ')
	print(s)
	print('测试失败!')
elif trim('  hello') != 'hello':
	print(222)
	s = trim('  hello')
	print(s)
	print('测试失败!')
elif trim('  hello  ') != 'hello':
	print(333)
	s = trim('  hello  ')
	print(s)
	print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
	print(444)
	s = trim('  hello  world  ')
	print(s)
	print('测试失败!')
elif trim('') != '':
	print(555)
	s = trim('')
	print(s)
	print('测试失败!')
elif trim('    ') != '':
	print(666)
	s = trim('    ')
	print(s)
	print('测试失败!')
else:
    print('测试成功!')