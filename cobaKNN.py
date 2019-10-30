import csv
import random
import math
import operator
 
def loadDataset(filename, split, trainingSet=[] , testSet=[]):
	with open(filename, 'r') as csvfile:
	    lines = csv.reader(csvfile)
	    dataset = list(lines)
	    for x in range(204):
	        if random.random() < split:
	            trainingSet.append(dataset[x])
	        else:
	            testSet.append(dataset[x])

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
		dist += hammingDistance(testInstance, trainingSet[x], 1)
		dist += hammingDistance(testInstance, trainingSet[x], 2)
		dist += hammingDistance(testInstance, trainingSet[x], 3)
		dist += euclideanDistance(testInstance, trainingSet[x], 4)/10000000
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
	split = 0.75
	loadDataset('data.csv', split, trainingSet, testSet)
	print ('Train set: ' + repr(len(trainingSet)))
	print ('Test set: ' + repr(len(testSet)))
	# generate predictions
	predictions=[]
	rate = 0.0
	k = int(math.sqrt(len(testSet)))
	print ('Nilai K: ' + repr(k))
	for x in range(len(testSet)):
		neighbors = getNeighbors(trainingSet, testSet[x], k)
		result = getResponse(neighbors, k)
		predictions.append(result)
		print('> predicted=' + repr(result))
		rate += result
	rate /= len(testSet)
	print (rate)
	mse = getMSE(testSet, predictions)
	print('MSE: ' + repr(mse))
	# print('Accuracy: ' + repr(accuracy))
	
main()