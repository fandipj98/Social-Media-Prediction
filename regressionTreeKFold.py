import numpy as np  
import csv
import random
import math
import operator
import matplotlib.pyplot as plt 
import pandas as pd  
from sklearn.tree import DecisionTreeRegressor 
from sklearn.preprocessing import LabelBinarizer

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

def getMSE(testSet, predictions):
	nilai = 0.0
	for x in range(len(testSet)):
		nilai += pow((float(testSet[x][-1]) - float(predictions[x])), 2)
	return nilai/float(len(testSet))

def main():
    loadDataset('data_rt_random.csv')
    totalMSE = 0.0

    trainingSet=[]
    testSet=[]
    y_pred = []

    #set 1 become tes set
    for x in range(2000):
        testSet.append(set1[x])
        trainingSet.append(set2[x])
        trainingSet.append(set3[x])
        trainingSet.append(set4[x])
        trainingSet.append(set5[x])

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
    # print(y_pred)

    mse = getMSE(testSet, y_pred)
    print('MSE Set 1: ' + repr(mse))
    totalMSE += mse

    trainingSet=[]
    testSet=[]
    y_pred = []

    #set 2 become tes set
    for x in range(2000):
        testSet.append(set2[x])
        trainingSet.append(set1[x])
        trainingSet.append(set3[x])
        trainingSet.append(set4[x])
        trainingSet.append(set5[x])

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
    # print(y_pred)

    mse = getMSE(testSet, y_pred)
    print('MSE Set 2: ' + repr(mse))
    totalMSE += mse

    trainingSet=[]
    testSet=[]
    y_pred = []

    #set 3 become tes set
    for x in range(2000):
        testSet.append(set3[x])
        trainingSet.append(set1[x])
        trainingSet.append(set2[x])
        trainingSet.append(set4[x])
        trainingSet.append(set5[x])

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
    # print(y_pred)

    mse = getMSE(testSet, y_pred)
    print('MSE Set 3: ' + repr(mse))
    totalMSE += mse

    trainingSet=[]
    testSet=[]
    y_pred = []

    #set 4 become tes set
    for x in range(2000):
        testSet.append(set4[x])
        trainingSet.append(set1[x])
        trainingSet.append(set2[x])
        trainingSet.append(set3[x])
        trainingSet.append(set5[x])

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
    # print(y_pred)

    mse = getMSE(testSet, y_pred)
    print('MSE Set 4: ' + repr(mse))
    totalMSE += mse

    trainingSet=[]
    testSet=[]
    y_pred = []

    #set 5 become tes set
    for x in range(2000):
        testSet.append(set5[x])
        trainingSet.append(set1[x])
        trainingSet.append(set2[x])
        trainingSet.append(set3[x])
        trainingSet.append(set4[x])

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
    # print(y_pred)

    mse = getMSE(testSet, y_pred)
    print('MSE Set 5: ' + repr(mse))
    totalMSE += mse

    totalMSE = totalMSE / 5
    print('Average MSE: ' + repr(totalMSE))
   

main()