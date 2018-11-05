from sklearn import linear_model
import xlrd

workbook = xlrd.open_workbook('task1.xls')
sheet = workbook.sheet_by_index(0)
rows = sheet.nrows
data = []
tags = []
for i in xrange(1,rows):
    row = sheet.row_values(i)
    if row[4] == 1.0:
        data.append([row[5],row[7]])
        tags.append(row[3])

clf = linear_model.LinearRegression()
clf.fit(data,tags)
print(clf.coef_)
print(clf.intercept_)

a1 = clf.coef_[0]
a2 = clf.coef_[1]
b = clf.intercept_
number = 0
for i in xrange(1,rows):
    row = sheet.row_values(i)
    print a1*row[5]+a2*row[7]+b
    if a1*row[5]+a2*row[7]+b > row[3]:
        number += 1
