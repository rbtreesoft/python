#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re

height_input=input("please enter your height:")

ss = re.findall(r"\d+\.?\d*",height_input)

if ss:
	for i in ss:
		if 0<float(i)<3:
			height_input=i
else:
	print("input illegal")

height=float('%.2f' % float(height_input))

weight_input=input("please enter your weight:")

sss = re.findall(r"\d+\.?\d*",weight_input)

if sss:
	for x in sss:
		if 0<float(x)<200:
			weight_input=x
else:
	print("input illegal")

weight=float('%.2f' % float(weight_input))

bmi =float('%.2f' % (weight/(height*height)))

if bmi>32:
    print('bmi:',bmi,'严重肥胖')
elif bmi>28:
    print('bmi:',bmi,'肥胖')
elif bmi>25:
    print('bmi:',bmi,'过重')
elif bmi>18.5:
    print('bmi:',bmi,'正常')
else:
    print('bmi:',bmi,'过轻')
