#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#利用字典将两个通讯录文本合并为一个文本
def main():
    ftele1=open('TeleAddressBook.txt','rb')
    ftele2=open('EmailAddressBook.txt','rb')
 
    ftele1.readline()#跳过第一行
    ftele2.readline()
    lines1 = ftele1.readlines()
    lines2 = ftele2.readlines()
 
    dic1 = {}  
    dic2 = {}
 
    for line in lines1:#获取第一个文本中的姓名和电话信息
        elements = line.split()
        dic1[elements[0]]=str(elements[1].decode('utf-8'))
    for line in lines2:#获取第二个文本中的姓名和邮件信息
        elements = line.split()
        dic2[elements[0]]=str(elements[1].decode('utf-8'))
 
    ###开始处理###
    lines = []
    lines.append('姓名\t    电话\t    邮箱\n')
 
    for key in dic1: 
        s= ''
        if key in dic2.keys():
                s = '\t'.join([str(key.decode('utf-8')), dic1[key], dic2[key]])
                s += '\n'
        else:
                s = '\t'.join([str(key.decode('utf-8')), dic1[key], str('   -----   ')])
                s += '\n'
        lines.append(s)
           
    for key in dic2: 
        s= ''
        if key not in dic1.keys():
                s = '\t'.join([str(key.decode('utf-8')), str('   -----   '), dic2[key]])
                s += '\n'
        lines.append(s)  
 
    ftele3 = open('AddressBook.txt', 'w')
    ftele3.writelines(lines)
    ftele3.close()
    ftele1.close()
    ftele2.close()
 
    print("The addressBooks are merged!")
    infile=open('AddressBook.txt', 'r')
    data=infile.read()
    print(data)
 
if __name__ == "__main__":
    main()