from sklearn import svm
import xlrd
from  sklearn.externals import joblib
from sklearn.cross_validation import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
workbook = xlrd.open_workbook('task1.xls')
sheet = workbook.sheet_by_index(0)
rows = sheet.nrows
data = []
tags = []
for i in xrange(1,rows):
    row = sheet.row_values(i)
    data.append([float(row[3]),float(row[5]),int(row[6]),float(row[7])])
    tags.append(int(row[4]))

# X_train,X_test, y_train, y_test = train_test_split(data,tags,test_size=0.2, random_state=0)
# a = 0
# 33 2
# for j in xrange(5,100):
#     for z in xrange(2,10):
#         clf = RandomForestClassifier(n_estimators=j,min_samples_leaf=z)
#         clf.fit(X_train,y_train)
#         pre_y = clf.predict(X_test)
#         # print pre_y
#         count = 0
#         for i in xrange(len(pre_y)):
#             if pre_y[i] == y_test[i]:
#                 count += 1
#         # print len(pre_y)
#         # print count
#         if count * 1.0 / len(pre_y) > a:
#             print j,z,count * 1.0 / len(pre_y)
#             a = count * 1.0 / len(pre_y)


# clf = RandomForestClassifier(n_estimators=33,min_samples_leaf=2)
# clf.fit(data[:668],tags[:668])
# x_test = data[668:]
# print x_test
# for i in xrange(len(x_test)):
#     x_test[i][0] += 1
# print x_test
# pre_y = clf.predict(x_test)
# y_test = tags[668:]
# print pre_y
# count = 0
# for i in xrange(len(pre_y)):
#     if pre_y[i] == 1:
#         count += 1
# print len(pre_y)
# print count

clf = svm.SVC()
clf.fit(data[:668],tags[:668])
x_test = data[668:]
print x_test
for i in xrange(len(x_test)):
    x_test[i][0] += 0
print x_test
pre_y = clf.predict(x_test)
y_test = tags[668:]
print pre_y
count = 0
for i in xrange(len(pre_y)):
    if pre_y[i] == y_test[i]:
        count += 1
print len(pre_y)
print count

joblib.dump(clf,'model')