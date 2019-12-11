import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
from sklearn.svm import SVC
from sklearn                        import metrics, svm

# import warnings filter
from warnings import simplefilter
# ignore all future warnings
simplefilter(action='ignore', category=FutureWarning)

# from sklearn.model_selection import train_test_split
# %matplotlib inline

def loadDataset(filename, filenameTest, trainingSet=[] , testSet=[]):
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

# def getMSE(testSet, predictions):
# 	nilai = 0.0
# 	for x in range(len(testSet)):
# 		nilai += pow((float(testSet[x]) - float(predictions[x])), 2)
# 	return nilai/float(len(testSet))

def main():
    trainingSet=[]
    testSet=[]
    loadDataset('data_rt_random.csv', 'data_eas_regression.csv', trainingSet, testSet)

    AtrainData = np.array(trainingSet)
    # print(AtrainData)

    aTrainDataGet = AtrainData[:,0:3].astype(float)
    # print(aTrainDataGet)

    bTrainDataGet = AtrainData[:,3].astype(float)
    # print(bTrainDataGet)

    AtestData = np.array(testSet)
    aTestDataGet = AtestData[:,0:3].astype(float)

    clf = svm.SVR()
    clf.fit(aTrainDataGet, bTrainDataGet) 
    y_pred = clf.predict(aTestDataGet)
    
    print(y_pred)

    # mse = getMSE(testSet, y_pred)
    # print('MSE Set 5: ' + repr(mse))


main()