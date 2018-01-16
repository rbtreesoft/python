#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import jieba

def main():
	data = jieba.lcut("中国是一个伟大的国家")
	print(data)

main()