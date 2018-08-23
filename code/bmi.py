# -*- coding: utf-8 -*-

name=input('enter name:')
h=input('enter height:')
w=input('enter weight:')
h=float(h)
w=float(w)
print(h)
print(w)
bmi = w / (h * h)
print(bmi)
if (bmi < 18.5):
    print("过轻")
elif (18.5 < bmi < 25):
    print("正常")
elif (25 < bmi < 28):
    print("过重")
elif (28 < bmi < 32):
    print("肥胖")
else:
    print("严重肥胖")