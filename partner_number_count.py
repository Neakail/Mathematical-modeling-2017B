# -*- coding:utf-8 -*-
import xlrd
from scipy.spatial.distance import cdist
import xlrd
import math
members = []
workbook = xlrd.open_workbook('task3.xlsx')
sheet = workbook.sheet_by_index(0)
rows = sheet.nrows
for i in xrange(1,rows):
    row = sheet.row_values(i)
    jingweidu = row[1].split(' ')
    weidu = float(jingweidu[0])
    jingdu = float(jingweidu[1])
    huoyuedu = float(row[4])
    members.append([weidu,jingdu,huoyuedu])

workbook = xlrd.open_workbook('task2.xls')
sheet = workbook.sheet_by_index(0)
rows = sheet.nrows
for i in xrange(1,rows):
    number = 0
    row = sheet.row_values(i)
    temp = [row[1],row[2]]
    for member in members:
        if cdist([temp], [member[:2]], metric='euclidean') < 0.1:
            # number += (1 * math.log(float(member[2])))
            number += 1
    print number
