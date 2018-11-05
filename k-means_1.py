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
# K = range(1, 10)
# meandistortions = []
# for k in K:
#     kmeans = KMeans(n_clusters=k)
#     kmeans.fit(data)
#     meandistortions.append(sum(np.min(
#         cdist(data, kmeans.cluster_centers_,
#               'euclidean'), axis=1)) / len(data))
# plt.plot(K, meandistortions, 'bx-')
# plt.xlabel('k')
# plt.ylabel(u'平均畸变程度')
# plt.title(u'用肘部法则来确定最佳的K值')
# plt.show()

plt.xlim([22, 24])
plt.ylim([112,116])
for j in xrange(4,9):
    kmeans_model = KMeans(n_clusters=j).fit(data)
    print metrics.calinski_harabaz_score(data,kmeans_model.labels_)
    # print kmeans_model.cluster_centers_
    print metrics.silhouette_score(data, kmeans_model.labels_, metric = 'euclidean')
    for i,l in enumerate(kmeans_model.labels_):
        plt.plot(data1[i],data2[i],color=colors[l],marker=markers[l],ls='None')
# plt.show()

# for j in xrange(2,5):
#     for z in xrange(2,14):
#         DBSCAN_model = DBSCAN(eps=(j*1.0/100), min_samples=z).fit(data)
#         # for i,l in enumerate(DBSCAN_model.labels_):
#         #     plt.plot(data1[i],data2[i],color=colors[l],marker=markers[l],ls='None')
#         # print DBSCAN_model.
#         print j,z,metrics.calinski_harabaz_score(data, DBSCAN_model.labels_)
# plt.show()

# 7 8 450