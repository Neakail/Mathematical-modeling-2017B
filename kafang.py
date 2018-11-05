# -*- coding:utf-8 -*-
import xlrd
from sklearn.feature_selection import SelectKBest

from sklearn.feature_selection import chi2
workbook = xlrd.open_workbook('task1.xls')
sheet = workbook.sheet_by_index(0)
rows = sheet.nrows
data = []
tags = []
for i in xrange(1,rows):
    row = sheet.row_values(i)
    data.append([row[6],row[7]])
    tags.append(row[4])
model1 = SelectKBest(chi2, k=2)

print model1.fit_transform(data,tags)
print model1.scores_
# print data