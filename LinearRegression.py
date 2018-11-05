from sklearn import linear_model
import xlrd

workbook = xlrd.open_workbook('task1.xls')
sheet = workbook.sheet_by_index(0)
rows = sheet.nrows
data = []
tags = []
for i in xrange(1,rows):
    row = sheet.row_values(i)
    data.append([row[6]])
    tags.append(row[3])

clf = linear_model.LinearRegression()
clf.fit(data,tags)
print(clf.coef_)
print(clf.intercept_)



