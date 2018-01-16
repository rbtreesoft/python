#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
	fo = open("sourcefile.txt","r")
	for line in fo:
		print(line)
	fo.close()

main()