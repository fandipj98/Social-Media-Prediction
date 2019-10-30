import numpy as np  
import csv
import random
import math
import operator
import matplotlib.pyplot as plt 
import pandas as pd  
from sklearn.tree import DecisionTreeRegressor 
from sklearn.preprocessing import LabelBinarizer


def loadDataset(filename, split, trainingSet=[] , testSet=[]):
	with open(filename, 'r') as csvfile:
	    lines = csv.reader(csvfile)
	    dataset = list(lines)
	    for x in range(204):
	        if random.random() < split:
	            trainingSet.append(dataset[x])
	        else:
	            testSet.append(dataset[x])

def getMSE(testSet, predictions):
	nilai = 0.0
	for x in range(len(testSet)):
		nilai += pow((float(testSet[x][-1]) - float(predictions[x])), 2)
	return nilai/float(len(testSet))

def main():
    trainingSet=[]
    testSet=[]
    split = 0.75
    loadDataset('data_rt.csv', split, trainingSet, testSet)

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
        rate += y_pred[x]
    rate /= len(y_pred)
    print (rate)

    mse = getMSE(testSet, y_pred)
    print('MSE: ' + repr(mse))
    # print("Predicted price: %d \n"% y_pred)


    # print(bTrainDataGet)

    # inputTrain = list()
    # tmp = list()
    # for x in range(len(AtrainData)):
    #     print(x)
    #     tmp.append(AtrainData[x])
    #     tmp.append(BtrainData[x])
    #     tmp.append(CtrainData[x])
    #     inputTrain.append(tmp)
    #     tmp.clear()

    # print(inputTrain)

    # YtrainData = [float(row[3]) for row in trainingSet]

    # AtestData = [float(row[0]) for row in testSet]
    # BtestData = [float(row[1]) for row in testSet]
    # CtestData = [float(row[2]) for row in testSet]

    # BtestData = [row[1] for row in testSet]

    # print(AtrainData)

    # X = AtrainData, BtrainData, CtrainData

    # print(X)
    
    # create a regressor object 
    # regressor = DecisionTreeRegressor(random_state = 0)  
    
    # fit the regressor with X and Y data 
    # regressor.fit(AtrainData, YtrainData) 

    # y_pred = regressor.predict(BtestData)
    # y_pred.reshape(1, -1) 
    
    # # # print the predicted price 
    # print("Predicted price: % d\n"% y_pred)

    # lb = LabelBinarizer() 
    # X_month_dummies = lb.fit_transform(XtrainData)
    # X = np.hstack([np.column_stack([XtrainData2]), X_month_dummies])

    # # print(X_month_dummies)

    # # # create a regressor object 
    # regressor = DecisionTreeRegressor(random_state = 0)  
    # regressor.fit(XtrainData, YtrainData)

    # # X_month_dummies2 = lb.fit_transform(XtestData)
    # # Z = np.hstack([np.column_stack([XtestData2]), X_month_dummies2])
    # print(XtestData[0])
    # y_pred = regressor.predict(testSet[0][0:3]) 
    # # print("Predicted price: % d\n"% y_pred)

main()