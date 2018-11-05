# -*- coding:utf-8 -*-
import xlrd
import numpy
from scipy.spatial.distance import cdist
center = [[ 22.66048247, 114.04669449],
 [ 23.04705094, 113.06414342],
 [ 22.88712921, 113.3719818 ],
 [ 23.46804139, 113.34021753],
 [ 22.97020072, 113.788403  ],
 [ 23.1595143,  113.31529503]]

center1 = [
    [23.12,113.35],
    [22.95,113.35],
    [22.80,113.30],
    [23.05,113.75],
    [22.57,113.90],
    [22.73,114.27]
]

workbook = xlrd.open_workbook('task2.xls')
sheet = workbook.sheet_by_index(0)
rows = sheet.nrows
data = {}
a = 0
b = 0
for i in xrange(1,rows):
    row = sheet.row_values(i)
    temp = 100
    for center_ in center1:
        if cdist([[row[1],row[2]]],[center_],metric='euclidean') < temp:
            temp = cdist([[row[1],row[2]]],[center_],metric='euclidean')
    # print temp[0][0]
    # if row[4] == 0.0:
    #     a += 1
    #     b += temp[0][0]
    if temp[0][0] > 0.1:
        print temp[0][0]
