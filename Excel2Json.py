#!/usr/bin/env python3
# -*- coding: <utf-8> -*-
#读取excel使用(支持03)
import xlrd
import json
import sys
import os
#读取execel使用(支持07)
from openpyxl import Workbook
#写入excel使用(支持07)
from openpyxl import load_workbook

PATH = ''
def open_excel(file='item.xlsx'):
    data  = xlrd.open_workbook(file)

def read03excel(path):
    workbook=xlrd.open_workbook(path)
    sheets=workbook.sheet_names();
    #多个sheet时，采用下面的写法打印
    #for sname in sheets:
        #print(sname)
    worksheet=workbook.sheet_by_name(sheets[0])
    #nrows=worksheet.nrows
    #nclows=worksheet.ncols
    for i in range(0,worksheet.nrows):
        row=worksheet.row(i)

        for j in range(0,worksheet.ncols):
            print(worksheet.cell_value(i,j),"\t",end="")

        print()

def read07excel(fileName,fileEnd):
	#打开excel表
    wb2=load_workbook(fileName + fileEnd)
    #excel中分表个数
    #print("分表个数: ",len(wb2.get_sheet_names()))
    #print(wb2.get_sheet_names())
    ws=wb2.get_sheet_by_name( wb2.get_sheet_names()[0] )#获取excel中第一个分表
    row=ws.get_highest_row()
    col=ws.get_highest_column()
    #print("列数: ",row)
    #print("行数: ",col)
    
    itemList = []
    item = dict() 

    for i  in range(0,row):
        item = dict() 
        for j in range(0,col):
            if(i > 2):
                item[ws.rows[0][j].value] = ws.rows[i][j].value
        if(i > 2 ):
            itemList.append(item)

    createJsonFile(fileName,itemList)    


def createJsonFile(fileName,datas):
    PATH = os.path.abspath('.')
    fl = open( PATH + '/json/' +fileName + '.json','w')
    fl.write(json.dumps(datas))
    fl.close()
    print('！！！！！！！！！！转换完成！！！！！！！！！', fileName +'.xlsx')


def getCurrentPathFile():
    #获取脚本文件当前路径
    PATH = os.path.abspath('.')
    os.mkdir(PATH+'/json')
    for fileName in os.listdir('.'):
        if(os.path.splitext(fileName)[1]=='.xlsx'):
            read07excel(os.path.splitext(fileName)[0],'.xlsx')
        elif(os.path.splitext(fileName)[1]=='.xls'):
            #read03excel
            pass


def main():
   #read07excel("item.xlsx")
   path = getCurrentPathFile()

if __name__=="__main__":
    main()	
