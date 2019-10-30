import numpy as np  
import csv
import random
import math
import operator
import matplotlib.pyplot as plt 
import pandas as pd  
from sklearn.tree import DecisionTreeRegressor 
from sklearn.preprocessing import LabelBinarizer


def loadDataset(filename, filenameTest, split, trainingSet=[] , testSet=[]):
    with open(filename, 'r') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        for x in range(1500):
            trainingSet.append(dataset[x])
    with open(filenameTest, 'r') as csvfileTest:
	    linesTest = csv.reader(csvfileTest)
	    datasetTest = list(linesTest)
	    for x in range(len(datasetTest)):
	        testSet.append(datasetTest[x])

def getMSE(testSet, predictions):
	nilai = 0.0
	for x in range(len(testSet)):
		nilai += pow((float(testSet[x][-1]) - float(predictions[x])), 2)
	return nilai/float(len(testSet))

def main():
    trainingSet=[]
    testSet=[]
    split = 0.67
    loadDataset('data_rt.csv', 'data_tugas_rt.csv', split, trainingSet, testSet)

    newFile = open("17-041_17-053_17-056_RegressionTree.csv","a")

    AtrainData = np.array(trainingSet)
    # print(AtrainData)

    aTrainDataGet = AtrainData[:,0:3].astype(float)
    # print(aTrainDataGet)

    bTrainDataGet = AtrainData[:,3].astype(float)
    # print(bTrainDataGet)

    AtestData = np.array(testSet)
    aTestDataGet = AtestData[:,0:3].astype(float)
    # print(aTestDataGet)
    # print('\n')

    # create a regressor object 
    regressor = DecisionTreeRegressor(random_state = 0)  
    regressor.fit(aTrainDataGet, bTrainDataGet)

    y_pred = regressor.predict(aTestDataGet)
    print(y_pred)
    rate = 0.0
    for x in range(len(y_pred)):
        newFile.write(str(y_pred[x]) + '\n')
        rate += y_pred[x]
    rate /= len(y_pred)
    print (rate)
    newFile.close()

    # mse = getMSE(testSet, y_pred)
    # print('MSE: ' + repr(mse))
    # print("Predicted price: %d \n"% y_pred)


   

main()