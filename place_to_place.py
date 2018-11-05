# -*- coding:utf-8 -*-
import xlrd
from scipy.spatial.distance import cdist
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
workbook = xlrd.open_workbook('task2_1.xlsx')
sheet = workbook.sheet_by_index(0)
rows = sheet.nrows
place = {}
for i in xrange(rows):
    row = sheet.row_values(i)
    place[row[0]] = [row[1],row[2]]

yijulei = []
dabao = {}
for i in place:
    temp_distance = 1
    temp_jingweidu = []
    temp_bianhao = ''
    for j in place:
        if i != j and j not in yijulei:
            if cdist([place[i]],[place[j]], metric='euclidean') < 0.001:
                if cdist([place[i]],[place[j]], metric='euclidean') < temp_distance:
                    temp_distance = cdist([place[i]],[place[j]], metric='euclidean')
                    temp_jingweidu = place[j]
                    temp_bianhao = j
    if temp_bianhao != '':
        dabao[i+'-'+temp_bianhao] = [(place[i][0]+temp_jingweidu[0])/2,(place[i][1]+temp_jingweidu[1])/2,temp_distance]
        yijulei.append(i)
        yijulei.append(temp_bianhao)

for i in dabao:
    # print i.split('-')[0]
    # print i.split('-')[1]
    print i,dabao[i][2][0][0]