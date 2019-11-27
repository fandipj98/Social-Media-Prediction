from sklearn.cluster import AffinityPropagation
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
import csv
import numpy as np
import matplotlib.pyplot as plt
from itertools import cycle

trainingSet=[]

with open('data_km.csv','r') as csvfile:
    lines = csv.reader(csvfile)
    dataset = list(lines)
    for x in range(1000):
        trainingSet.append(dataset[x])
with open('data_tugas_km.csv', 'r') as csvfileTest:
    linesTest = csv.reader(csvfileTest)
    datasetTest = list(linesTest)

trainData = np.array(trainingSet)
# print(trainData)

np.random.shuffle(trainData)

categoryGet = trainData[:,0].astype(float)
# print(categoryGet)
subcategoryGet = trainData[:,1].astype(float)
# print(subcategoryGet)
labelGet = trainData[:,2].astype(float)
# print(labelGet)
cscGet = trainData[:,0:2].astype(float)
# print(cscGet)

# plt.scatter(subcategoryGet, labelGet)
# plt.show()

testData = np.array(datasetTest)
# print(testData)
testDataGet = testData[:,0:2].astype(float)
# print(testDataGet)

af = AffinityPropagation(preference=-50).fit(cscGet)
cluster_centers_indices = af.cluster_centers_indices_
labels = af.labels_

n_clusters_ = len(cluster_centers_indices)


# plt.close('all')
# plt.figure(1)
# plt.clf()

cluster_center = []
colors = cycle('bgrcmykbgrcmykbgrcmykbgrcmyk')
for k, col in zip(range(n_clusters_), colors):
    class_members = labels == k
    cluster_center.append(cscGet[cluster_centers_indices[k]])
    
centroid = np.array(cluster_center)

closest_centroid = []
for x in range(len(testDataGet)):
    diff = centroid - testDataGet[x,:]
    # print(diff)
    dist = np.sqrt(np.sum(diff**2, axis=-1))
    # print(dist)
    closest_centroid.append(centroid[np.argmin(dist),])
    # print(centroid)

for x in range(len(closest_centroid)):
    print (closest_centroid[x])

#     plt.plot(cscGet[class_members, 0], cscGet[class_members, 1], col + '.')
#     plt.plot(cluster_center[0], cluster_center[1], 'o',markerfacecolor=col,
#              markeredgecolor='k', markersize=14)
    
#     for x in cscGet[class_members]:
#         plt.plot([cluster_center[0], x[0]], [cluster_center[1], x[1]], col)

# plt.title('Estimated number of clusters: %d' % n_clusters_)
# plt.show()

