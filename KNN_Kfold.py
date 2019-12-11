import csv
import random
import math
import operator

set1 = []
set2 = []
set3 = []
set4 = []
set5 = []

def loadDataset(filename):
    with open(filename, 'r') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        for x in range(2000):
            set1.append(dataset[x])
            set2.append(dataset[x+2000])
            set3.append(dataset[x+4000])
            set4.append(dataset[x+6000])
            set5.append(dataset[x+8000])

def euclideanDistance(instance1, instance2, x):
	distance = 0
	distance += pow((float(instance1[x]) - float(instance2[x])), 2)
	return math.sqrt(distance)

def hammingDistance(instance1, instance2, x):
	distance = 0
	if instance1[x] != instance2[x]:
		distance = 1
	return distance

def getNeighbors(trainingSet, testInstance, k):
	distances = []
	for x in range(len(trainingSet)):
		dist = euclideanDistance(testInstance, trainingSet[x], 0)
		dist += euclideanDistance(testInstance, trainingSet[x], 1)
		dist += euclideanDistance(testInstance, trainingSet[x], 2)
		distances.append((trainingSet[x], dist))

	distances.sort(key=operator.itemgetter(1))
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
		nilai += pow((float(testSet[x][-1]) - float(predictions[x])), 2)
	return nilai/float(len(testSet))
	
def main():
	# prepare data
    trainingSet=[]
    testSet=[]
    totalMSE = 0.0
    loadDataset('data_rt_random.csv')
    print ('Jumlah Data Set 1: ' + repr(len(set1)))
    print ('Jumlah Data Set 2: ' + repr(len(set2)))
    print ('Jumlah Data Set 3: ' + repr(len(set3)))
    print ('Jumlah Data Set 4: ' + repr(len(set4)))
    print ('Jumlah Data Set 5: ' + repr(len(set5)))

    #set 1 become tes set
    for x in range(2000):
        testSet.append(set1[x])
        trainingSet.append(set2[x])
        trainingSet.append(set3[x])
        trainingSet.append(set4[x])
        trainingSet.append(set5[x])

    print ('Jumlah Train set: ' + repr(len(trainingSet)))
    print ('Jumlah Test set: ' + repr(len(testSet)))

    # generate predictions
    predictions=[]
    k = int(math.sqrt(len(trainingSet)))
    # k = 9
    print ('Nilai K: ' + repr(k))
        
    for x in range(len(testSet)):
        # print(testSet[x])
        neighbors = getNeighbors(trainingSet, testSet[x], k)
        result = getResponse(neighbors, k)
        predictions.append(result)
        # print('> predicted=' + repr(result))
    mse = getMSE(testSet, predictions)
    print('MSE Set 1: ' + repr(mse))
    totalMSE += mse
	# print('Accuracy: ' + repr(accuracy))

    # set 2 become tes set
    trainingSet=[]
    testSet=[]
    predictions=[]
    for x in range(2000):
        testSet.append(set2[x])
        trainingSet.append(set1[x])
        trainingSet.append(set3[x])
        trainingSet.append(set4[x])
        trainingSet.append(set5[x])
    
    for x in range(len(testSet)):
        # print(testSet[x])
        neighbors = getNeighbors(trainingSet, testSet[x], k)
        result = getResponse(neighbors, k)
        predictions.append(result)
        # print('> predicted=' + repr(result))
    mse = getMSE(testSet, predictions)
    print('MSE Set 2: ' + repr(mse))
    totalMSE += mse

    # set 3 become tes set
    trainingSet=[]
    testSet=[]
    predictions=[]
    for x in range(2000):
        testSet.append(set3[x])
        trainingSet.append(set1[x])
        trainingSet.append(set2[x])
        trainingSet.append(set4[x])
        trainingSet.append(set5[x])
    
    for x in range(len(testSet)):
        # print(testSet[x])
        neighbors = getNeighbors(trainingSet, testSet[x], k)
        result = getResponse(neighbors, k)
        predictions.append(result)
        # print('> predicted=' + repr(result))
    mse = getMSE(testSet, predictions)
    print('MSE Set 3: ' + repr(mse))
    totalMSE += mse

    # set 4 become tes set
    trainingSet=[]
    testSet=[]
    predictions=[]
    for x in range(2000):
        testSet.append(set4[x])
        trainingSet.append(set1[x])
        trainingSet.append(set2[x])
        trainingSet.append(set3[x])
        trainingSet.append(set5[x])
    
    for x in range(len(testSet)):
        # print(testSet[x])
        neighbors = getNeighbors(trainingSet, testSet[x], k)
        result = getResponse(neighbors, k)
        predictions.append(result)
        # print('> predicted=' + repr(result))
    mse = getMSE(testSet, predictions)
    print('MSE Set 4: ' + repr(mse))
    totalMSE += mse

    # set 5 become tes set
    trainingSet=[]
    testSet=[]
    predictions=[]
    for x in range(2000):
        testSet.append(set5[x])
        trainingSet.append(set1[x])
        trainingSet.append(set2[x])
        trainingSet.append(set3[x])
        trainingSet.append(set4[x])
    
    for x in range(len(testSet)):
        # print(testSet[x])
        neighbors = getNeighbors(trainingSet, testSet[x], k)
        result = getResponse(neighbors, k)
        predictions.append(result)
        # print('> predicted=' + repr(result))
    mse = getMSE(testSet, predictions)
    print('MSE Set 5: ' + repr(mse))
    totalMSE += mse

    totalMSE = totalMSE / 5
    print('Average MSE: ' + repr(totalMSE))

main()