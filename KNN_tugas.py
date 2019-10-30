import csv
import random
import math
import operator
 
def loadDataset(filename, filenameTest, split, trainingSet=[] , testSet=[]):
    with open(filename, 'r') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        for x in range(153):
            trainingSet.append(dataset[x])
    with open(filenameTest, 'r') as csvfileTest:
	    linesTest = csv.reader(csvfileTest)
	    datasetTest = list(linesTest)
	    for x in range(len(datasetTest)):
	        testSet.append(datasetTest[x])

def euclideanDistance(instance1, instance2, x, y):
    # print (instance1[x] + ' ' + instance2[y])
    distance = 0
    distance += pow((float(instance1[x]) - float(instance2[y])), 2)
    return math.sqrt(distance)

def hammingDistance(instance1, instance2, x, y):
    # print (instance1[x] + ' ' + instance2[y])
    distance = 0
    if instance1[x] != instance2[y]:
    	distance = 1
    return distance

def getNeighbors(trainingSet, testInstance, k):
    distances = []
    for x in range(len(trainingSet)):
        dist = 0.0
        dist += float(hammingDistance(testInstance, trainingSet[x], 0, 1))
        dist += float(hammingDistance(testInstance, trainingSet[x], 1, 3))
        dist += float(hammingDistance(testInstance, trainingSet[x], 2, 2))
        dist += euclideanDistance(testInstance, trainingSet[x], 3, 0)
        dist += euclideanDistance(testInstance, trainingSet[x], 4, 4)/10000000
        # print (dist)
        distances.append((trainingSet[x], dist))
    # print (distances[0][0])
    distances.sort(key=operator.itemgetter(1))
    # print (distances[0][0])
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors
 
def getResponse(neighbors, jumlah):
	hasil = 0.0
	for x in range(len(neighbors)):
		response = float(neighbors[x][-1])
		hasil += response
	hasil /= jumlah
	return hasil
 
def getAccuracy(testSet, predictions):
	correct = 0
	for x in range(len(testSet)):
		if float(testSet[x][-1]) == float(predictions[x]):
			correct += 1
	return (correct/float(len(testSet))) * 100.0

def getMSE(testSet, predictions):
	nilai = 0.0
	for x in range(len(testSet)):
		nilai += pow((float(testSet[x]) - float(predictions[x])), 2)
	return nilai/float(len(testSet))
	
def main():
	# prepare data
    trainingSet=[]
    testSet=[]
    split = 0.67
    loadDataset('data.csv', 'data_tugas.csv', split, trainingSet, testSet)
    print ('Train set: ' + repr(len(trainingSet)))
    print ('Test set: ' + repr(len(testSet)))
	# generate predictions
    predictions=[]
    rate = 0.0
    # k = int(math.sqrt(len(testSet)))
    k = 9
    print ('Nilai K: ' + repr(k))
    
    newFile = open("17-041_17-053_17-056_KNN.csv", "a")
    
    for x in range(len(testSet)):
        # print(testSet[x])
        neighbors = getNeighbors(trainingSet, testSet[x], k)
        result = getResponse(neighbors, k)
        predictions.append(result)
        newFile.write(str(result) + '\n')
        print('> predicted=' + repr(result))
        rate += result
    rate /= len(testSet)
    newFile.close()
    # print (rate)
    # cobaSet = [6.51,8.63,11.17,15.15,8.67,11.17,11.17,16.3,15.15,15.15,8.67,15.15,15.15,15.15,15.15,15.15,15.15,15.15,6.51,6.51,15.15,6.51,6.31,8.63,16.3,16.3,9.025,15.15,15.15,8.63,15.15,15.15,8.63,8.63,11.17,15.15,11.17,15.15,8.63,6.31,11.17,6.51,6.51,8.63,15.15,8.63,16.3,8.67,8.67,8.63,15.15]
    # cobaSet = [6.94,11.17,11.17,13.7,11.17,11.17,11.17,16.3,13.7,13.7,11.17,13.7,13.7,13.7,13.7,13.7,13.7,13.7,6.51,6.51,13.7,6.51,11.17,11.17,16.3,16.3,5.32,13.7,13.7,11.17,13.7,13.7,11.17,11.17,11.17,13.7,11.17,13.7,11.17,12.74,11.17,6.51,6.51,8.63,13.7,11.17,16.3,11.17,11.17,8.63,13.7]
    # cobaSet = [6.94,11.17,11.17,10.7,11.17,11.17,11.17,16.3,8.485,8.485,11.17,10.7,10.7,8.485,10.7,8.485,10.7,10.7,6.51,6.51,10.7,6.51,11.17,11.17,5.88,5.88,8.18,10.7,10.63,11.17,10.63,8.485,11.17,11.17,11.17,10.7,11.17,10.7,11.17,7.78,11.17,6.51,6.51,7.78,10.7,11.17,10.3,11.17,11.17,7.78,8.485]
    # cobaSet = [6.94,11.17,11.17,13.7,11.17,11.17,11.17,16.3,13.7,13.7,11.17,13.7,13.7,13.7,13.7,13.7,13.7,13.7,6.51,6.51,13.7,6.51,11.17,11.17,16.3,16.3,5.32,13.7,13.7,11.17,13.7,13.7,11.17,11.17,11.17,13.7,11.17,13.7,11.17,12.74,11.17,6.51,6.51,8.63,13.7,11.17,16.3,11.17,11.17,8.63,13.7]
    # mse = getMSE(cobaSet, predictions)
    # print('MSE: ' + repr(mse))
	# print('Accuracy: ' + repr(accuracy))
	
main()