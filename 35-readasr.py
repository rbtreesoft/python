#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
	infile = open("test.txt","r")
	data = infile.read()
	print(data)
	infile.close()

main()