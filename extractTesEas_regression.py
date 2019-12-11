import csv
output = open("listCategory.txt", "r")

myMap = dict()
counter = 0

fileText = output.readline().replace('\n', '')

while fileText:
    
    counter += 1
    myMap[fileText] = counter
    fileText = output.readline().replace('\n', '')

output.close()

subcategory_output = open("listSubcategory.txt", "r")
subMap = dict()
counter = 0

subFileText = subcategory_output.readline().replace('\n', '')

while subFileText:

    counter += 1
    subMap[subFileText] = counter
    subFileText = subcategory_output.readline().replace('\n', '')

subcategory_output.close()

oneHotTemplate = []

for x in range (77):
    oneHotTemplate.append('0')
# x = "".join(oneHotTemplate)
# print(x)
    
newFile = open("data_eas_regression.csv", "a")
testFile = open("EAS_testData.txt", encoding="utf8")
myList = []
counterList = 0

lines = testFile.read()
pos = 132
check = 0
temp = ''
subtemp = ''
comma_check = 0
data= [[]]
container = []
baris = 0

# print (lines[pos])

while True:
    if pos>len(lines)-1:
        # print (data)
        break
    count = 1
    tag_count = 1
    while True:
        if pos>len(lines)-1:
            # print ("masuk")
            break
        elif lines[pos]=='\n' and count != 0:
            # newFile.write('\n')
            pos += 1
            # print (lines[pos] + '\n')
            break
        else:
            pos += 1
            # print (str(count))
            if lines[pos]=='"':
                count += 1
                pos += 1
                if comma_check == 1:
                    comma_check = 0
            # print(lines[pos] + str(count) + ' ' + str(pos) + '\n')
            #category
            if count==5:
                temp = temp + lines[pos]
                # print(lines[pos] + str(count) + '\n')
            
            elif count==6:
                # newFile.write( str(myMap[temp]) + ',')
                container.append(myMap[temp])
                temp = ''

            # subcategory
            elif count==7:
                if lines[pos]==',':
                    comma_check = 1
                if comma_check == 0:
                    subtemp = subtemp + lines[pos]
            
            elif count==8:
                container.append(subMap[subtemp])
                # newFile.write(str(subMap[subtemp]) + ',')
                subtemp = ''

            #jumlah alltags
            elif count==21:
                if lines[pos]==' ':
                    tag_count += 1 
            elif count==22:
                container.insert(0, tag_count)
                # newFile.write(str(tag_count)+',')
            # print('bawah' + str(count) + ' ' + str(pos) + '\n')
            # for x in range(3):
            #     data[baris].append(container[x])
    # print(container)
    for x in range(3):
        data[baris].append(container[x])
    # print (data)
    data.append([])
    baris += 1
    for x in range(3):
        container.pop()
data.pop()
# print (data)
for x in data:
    count = 0
    for y in x:
        count += 1
        if count < 3:
            newFile.write(str(y) + ',')
        else:
            newFile.write(str(y))
    newFile.write('\n')

testFile.close()
newFile.close()