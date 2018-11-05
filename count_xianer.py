# -*- coding:utf-8 -*-
import xlrd

workbook = xlrd.open_workbook('task3.xlsx')
sheet = workbook.sheet_by_index(0)
rows = sheet.nrows
xianer = 0
for i in xrange(1,rows):
    row = sheet.row_values(i)
    xianer += row[2]
print xianer*1.0/(rows-1)