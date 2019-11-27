from fcmeans import FCM
from sklearn.datasets import make_blobs
from matplotlib import pyplot as plt
from seaborn import scatterplot as scatter
import csv
import numpy as np

trainingSet=[]

with open('data_km.csv','r') as csvfile:
    lines = csv.reader(csvfile)
    dataset = list(lines)
    for x in range(len(dataset)):
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

fcm = FCM(n_clusters=3)
fcm.fit(cscGet)

fcm_centers = fcm.centers
fcm_labels  = fcm.u.argmax(axis=1)

f, axes = plt.subplots(1, 2, figsize=(11,5))
scatter(cscGet[:,0], cscGet[:,1], ax=axes[0])
scatter(cscGet[:,0], cscGet[:,1], ax=axes[1], hue=fcm_labels)
scatter(fcm_centers[:,0], fcm_centers[:,1], ax=axes[1],marker="*",s=200)

closest_centroid = []
for x in range(len(testDataGet)):
    diff = fcm_centers - testDataGet[x,:]
    # print(diff)
    dist = np.sqrt(np.sum(diff**2, axis=-1))
    # print(dist)
    closest_centroid.append(fcm_centers[np.argmin(dist),])
    # print(fcm_centers)

for x in range(len(closest_centroid)):
    print (closest_centroid[x])


# plt.show()


