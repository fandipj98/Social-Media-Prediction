output = open("listSubcategory.txt", "r")

myMap = dict()
index = 0

fileText = output.readline().replace('\n', '')

while fileText:
    # print(str(index) + ' ' + fileText)
    index += 1
    myMap[fileText] = index
    fileText = output.readline().replace('\n', '')

# print(myMap["Good"])

output.close()