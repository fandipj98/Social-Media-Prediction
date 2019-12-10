import csv
import numpy as np

trainingSet=[]

with open('data_rt_kfold.csv','r') as csvfile:
    lines = csv.reader(csvfile)
    dataset = list(lines)
    for x in range(len(dataset)):
        trainingSet.append(dataset[x])

trainData = np.array(trainingSet)
# print(trainData)
np.random.shuffle(trainData)

newFile = open("data_rt_random.csv", "a")

maks_count = 0
for x in trainData:
    if maks_count >= 30000:
        break
    count = 0
    for y in x:
        count += 1
        if count < 4:
            newFile.write(y + ',')
        else:
            newFile.write(y)
    newFile.write('\n')
    maks_count += 1
