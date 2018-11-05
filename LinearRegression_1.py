from sklearn import linear_model
import xlrd
import math
workbook = xlrd.open_workbook('task1.xls')
sheet = workbook.sheet_by_index(0)
rows = sheet.nrows
data = []
tags = []
for i in xrange(1,rows):
    row = sheet.row_values(i)
    data.append([row[5]])
    tags.append(row[3])

clf = linear_model.LinearRegression()
clf.fit(data,tags)
a1 = clf.coef_
b1 = clf.intercept_
all_cost = 0
for i in xrange(1,rows):
    row = sheet.row_values(i)
    predict_price = a1 * float(row[5]) + b1
    print predict_price[0]
    all_cost += abs(predict_price[0] - float(row[3]))
print all_cost
print all_cost * 1.0 / (rows-1)