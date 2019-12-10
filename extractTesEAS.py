import csv
output = open("listSubcategory.txt", "r")

myMap = dict()
counter = 0

fileText = output.readline().replace('\n', '')

while fileText:
    
    counter += 1
    myMap[fileText] = counter
    fileText = output.readline().replace('\n', '')

output.close()

oneHotTemplate = []

for x in range (77):
    oneHotTemplate.append('0')
# x = "".join(oneHotTemplate)
# print(x)
    
newFile = open("data_eas_knn.csv", "a")
testFile = open("EAS_testData.txt", encoding="utf8")
myList = []
counterList = 0

lines = testFile.read()
pos = 132
check = 0
temp = ''

# print (lines[pos])

while True:
    if pos>len(lines)-1:
        break
    count = 1
    tag_count = 1
    while True:
        if pos>len(lines)-1:
            # print ("masuk")
            break
        elif lines[pos]=='\n' and count != 0:
            newFile.write('\n')
            pos += 1
            # print (lines[pos] + '\n')
            break
        else:
            pos += 1
            # print (str(count))
            if lines[pos]=='"':
                count += 1
                pos += 1
            # print(lines[pos] + str(count) + ' ' + str(pos) + '\n')
            #category, conxept, postdate
            if count==5 or count==9 or count==23:
                newFile.write(str(lines[pos]))
                # print(lines[pos] + str(count) + '\n')
            
            elif count==6 or count==10:
                newFile.write(',')
            # subcategory
            elif count==7:
                if lines[pos]==',':
                    # print(myMap[temp])
                    oneHotTemplate[myMap[temp]-1] = '1'
                    myList.append(myMap[temp]-1)
                    temp = ''
                    counterList += 1
                else :
                    temp = temp + str(lines[pos])
                    # print (temp)
            
            elif count==8:
                # print(temp)
                oneHotTemplate[myMap[temp]-1] = '1'
                newFile.write("".join(oneHotTemplate) + ',')
                oneHotTemplate[myMap[temp]-1] = '0'
                temp = ''

                while counterList > 0:
                    oneHotTemplate[myList[counterList - 1]] = '0'
                    myList.pop()
                    counterList -= 1
            #jumlah alltags
            elif count==21:
                if lines[pos]==' ':
                    tag_count += 1 
            elif count==22:
                newFile.write(str(tag_count)+',')
            # print('bawah' + str(count) + ' ' + str(pos) + '\n')
            
testFile.close()
newFile.close()