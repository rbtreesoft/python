#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
	infile = open("sourcefile.txt","r")
	outfile = open("copiedfile.txt","w")
	for line in fo:
            outfile.write(line)
	outfile.close()
	infile.close()
	fo = open("copiedfile.txt","r")
	print(fo.read())
	
main()
