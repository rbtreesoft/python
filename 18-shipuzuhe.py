#!/usr/bin/env python3
# -*- coding: utf-8 -*-

diet=['西红柿','花椰菜','黄瓜','牛排','虾仁']
for x in range(len(diet)):
	for y in range(len(diet)):
		if not(x == y):
			print("{0}{1}".format(diet[x],diet[y]))