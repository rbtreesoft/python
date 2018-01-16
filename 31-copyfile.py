#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#文件拷贝
def main():
	#用户输入文件名
	f1 = input().strip()
	f2 = input().strip()

	#打开文件
	infile = open(f1,'r')
	outfile = open(f2,'w')

	#拷贝数据
	countLines = countchars = 0
	for line in infile:
		countLines += 1
		countchars += len(line)
		outfile.write(line)
	print(countLines,"lines and",countchars,"chars copied")

	infile.close()
	outfile.close()

main()