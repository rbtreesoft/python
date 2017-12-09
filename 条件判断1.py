#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re

height_input=input("please enter your height:")

ss = re.findall(r"\d+\.?\d*",height_input)

if ss:
	height_input = ss[0]
else:
	print("input illegal")

height=float('%.2f' % float(height_input))

weight_input=input("please enter your weight:")

sss = re.findall(r"\d+\.?\d*",weight_input)

if sss:
	weight_input = sss[0]
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