from  sklearn.externals import joblib
import xlrd

with open('dabao1.txt','r') as f:
    dabao_id = [i.strip() for i in f.readlines() ]
clf = joblib.load('model')
workbook = xlrd.open_workbook('task2.xls')
sheet = workbook.sheet_by_index(0)
rows = sheet.nrows
for i in xrange(1,rows):
    row = sheet.row_values(i)
    a = 0
    if row[0] in dabao_id:
        print float(row[6])
    else:
        while clf.predict([[float(row[6])+a,float(row[3]),int(row[4]),float(row[5])]])[0] != 1:
            a += 0.5
        print float(row[6])+a


