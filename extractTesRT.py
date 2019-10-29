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
    
newFile = open("data_tugas_rt.csv", "a")
testFile = open("testSet.txt", encoding="utf8")
myList = []
counterList = 0

lines = testFile.read()
pos = 0
check = 0
temp = ''

while True:
    if pos>len(lines)-1:
        break
    count = 0
    tag_count = 1
    while True:
        if pos>len(lines)-1:
            break
        elif lines[pos]=='\n' and count != 0:
            newFile.write('\n')
            pos += 1
            break
        else:
            if lines[pos]=='"':
                count += 1
            pos += 1

            if count==11 or count==19 or count==47:
                if lines[pos]=='"':
                    count += 1
                    pos += 1
                else:
                    newFile.write(str(lines[pos]))
                    # print(lines[pos] + str(count) + '\n')
            
            if count==12 or count==20:
                newFile.write(',')
            # subcategory
            elif count==15:
                if lines[pos]=='"':
                    count += 1
                    pos += 1
                else:
                    if lines[pos]==',':
                        # print(myMap[temp])
                        oneHotTemplate[myMap[temp]-1] = '1'
                        myList.append(myMap[temp]-1)
                        temp = ''
                        counterList += 1
                    else :
                        #print(str(lines2[index2]))
                        temp = temp + str(lines[pos])
            
            if count==16:
                #print(',\n')
                oneHotTemplate[myMap[temp]-1] = '1'
                newFile.write("".join(oneHotTemplate) + ',')
                oneHotTemplate[myMap[temp]-1] = '0'
                temp = ''

                while counterList > 0:
                    oneHotTemplate[myList[counterList - 1]] = '0'
                    myList.pop()
                    counterList -= 1
            
            #jumlah alltags
            elif count==43:
                if lines[pos]==' ':
                    tag_count += 1 
            elif count==44:
                newFile.write(str(tag_count)+',')
testFile.close()
newFile.close()