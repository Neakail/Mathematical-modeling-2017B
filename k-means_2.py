# -*- coding:utf-8 -*-
import xlrd
from sklearn.cluster import KMeans,DBSCAN
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist
import numpy as np
from sklearn import metrics
workbook = xlrd.open_workbook('task1.xls')
sheet = workbook.sheet_by_index(0)
rows = sheet.nrows
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'b', 'c', 'm', 'y', 'k','b', 'g', 'r','k','b', 'g', 'r']
markers = ['o', 's', 'D', 'v', '^', 'p', '*', '+', 'D', 'v', '^', 'p', 's', 'D', 'v', 's', 'D', 'v','p']
data1 = []
data2 = []
data = []
for i in xrange(1,rows):
    temp = sheet.row_values(i)
    data1.append(temp[1])
    data2.append(temp[2])
    data.append([temp[1],temp[2]])

plt.xlim([22, 24])
plt.ylim([112,116])
kmeans_model = KMeans(n_clusters=6).fit(data)
print metrics.calinski_harabaz_score(data,kmeans_model.labels_)
# print kmeans_model.cluster_centers_
print metrics.silhouette_score(data, kmeans_model.labels_, metric = 'euclidean')
for i,l in enumerate(kmeans_model.labels_):
    plt.plot(data1[i],data2[i],color=colors[l],marker=markers[l],ls='None')
plt.show()