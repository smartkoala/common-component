#! /usr/bin/python
# -*- coding:utf-8 -*-

# 官网： http://www.python-excel.org/
import xlrd
import xlwt

#读excle的数据
def read_excle(excle_path,sheet_name):
    work_book = xlrd.open_workbook(excle_path)
    sheet = work_book.sheet_by_name(sheet_name)
    # work_book.sheet_by_index(0)
    # work_book.sheets()[0]
    # work_book.sheet_names()
    rows = sheet.nrows
    cols = sheet.ncols
    for row_num in range(rows):
        for col_num in range(cols):
            value = sheet.cell_value(row_num,col_num)
            print value


#写excle的数据
def write_excle(excle_path,sheet_name):
    work_book = xlwt.Workbook()
    sheet = work_book.add_sheet(sheet_name)
    sheet.write(0,0,'test')
    work_book.save(excle_path)

if __name__ == '__main__':
    read_excle('test_read.xls','Sheet1')
    #write_excle("test_write.xls","Sheet1")