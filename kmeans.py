import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.datasets.samples_generator import make_blobs
from sklearn.cluster import KMeans
import csv

trainingSet=[]

with open('data_km.csv','r') as csvfile:
    lines = csv.reader(csvfile)
    dataset = list(lines)
    for x in range(len(dataset)):
        trainingSet.append(dataset[x])
with open('data_tugas_km.csv', 'r') as csvfileTest:
    linesTest = csv.reader(csvfileTest)
    datasetTest = list(linesTest)

# def predict(data, centroids):
#     distances = []
#     for unit in data:
#         for center in centroids:
#             distances.append(np.sum((unit - center) ** 2))                
#     distances = np.reshape(distances, data.shape)
#     closest_centroid = [np.argmin(dist) for dist in distances]
#     print(closest_centroid)	    

trainData = np.array(trainingSet)
# print(trainData)

categoryGet = trainData[:,0].astype(float)
# print(categoryGet)
subcategoryGet = trainData[:,1].astype(float)
# print(subcategoryGet)
labelGet = trainData[:,2].astype(float)
# print(labelGet)

cscGet = trainData[:,0:2].astype(float)

testData = np.array(datasetTest)
# print(testData)
testDataGet = testData[:,0:2].astype(float)
# print(testDataGet)

# plt.scatter(subcategoryGet, labelGet)
# plt.show()

kmeans = KMeans(n_clusters=3).fit(cscGet)
centroid = kmeans.cluster_centers_
# print(centroids)

plt.scatter(cscGet[:,0], cscGet[:,1])
plt.scatter(centroid[:,0], centroid[:,1], marker='*', c='g', s=150)
# plt.show()

# predict(testDataGet, centroid)


diff = centroid - testDataGet[0,:]
# print(diff)
dist = np.sqrt(np.sum(diff**2, axis=-1))
# print(dist)
closest_centroid = centroid[np.argmin(dist),]
# print(centroid)
# print(closest_centroid)

# Cari Center
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=1000, n_init=10, random_state=0)
    kmeans.fit(cscGet)
    wcss.append(kmeans.inertia_)
plt.plot(range(1, 11), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()

# kmeans = KMeans(n_clusters=4, init='k-means++', max_iter=300, n_init=10, random_state=0)
# pred_y = kmeans.fit_predict(categoryGet)
# print(pred_y)



