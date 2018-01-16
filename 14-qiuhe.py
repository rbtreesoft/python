#!/usr/bin/env python3
# -*- coding: utf-8 -*-

n=input("请输入整数N：")
sum=0
for i in range(int(n)):
    sum=sum+i+1
print("1到%d求和结果：%d"%(int(n),sum))