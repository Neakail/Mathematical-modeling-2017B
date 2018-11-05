# -*- coding:utf-8 -*-
import xlrd
import matplotlib.pyplot as plt
workbook = xlrd.open_workbook('task1.xls')
sheet = workbook.sheet_by_index(0)
rows = sheet.nrows

count = [0,0,0,0,0,0,0]
for i in xrange(1,rows):
    row = sheet.row_values(i)
    if row[4] == 1.0:
        distance = float(row[5])
        if distance < 0.05 :
            count[0] += 1
        elif distance >= 0.05 and distance <= 0.1:
            count[1] += 1
        elif distance >= 0.1 and distance <= 0.15:
            count[2] += 1
        elif distance >= 0.15 and distance <= 0.2:
            count[3] += 1
        elif distance >= 0.2 and distance <= 0.25:
            count[4] += 1
        elif distance >= 0.25 and distance <= 0.3:
            count[5] += 1
print count
all_count = sum(count)
print all_count
bilv = []
for i in count:
    bilv.append(i*1.0/all_count)
plt.bar([0.025,0.075,0.125,0.175,0.225,0.275,0.325],bilv,width = 0.05)
plt.show()