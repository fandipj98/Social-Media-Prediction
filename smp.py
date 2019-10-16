newFile = open("tags.txt","a")
tag = open("train_tags.json", "r")
category = open("train_category.json", "r")

lines = tag.read()
pos = -1

lines2 = category.read()
pos2 = -1

lines3 = category.read()
pos3 = -1

while True:
    pos = lines.find('Alltags', pos+1)
    # print(pos)
    index = pos+11
    count = 1
    while True:
        # print (lines[index])
        index += 1
        if lines[index]==' ':
            count += 1
        if lines[index]=='"':
            break
    # print (count)
    if pos == -1:
        newFile.write(str(count))
        break
    newFile.write(str(count)+',')

    pos2 = lines2.find('Category', pos2+1)
    #print(pos2)
    index2 = pos2+12
    while True:
        #print (lines2[index2])
        if lines2[index2]=='"':
            #print(',\n')
            newFile.write(',\n')
            break
        else :
            #print(str(lines2[index2]))
            newFile.write(str(lines2[index2]))
            index2 += 1
    
    # pos3 = lines3.find('Subcategory')
    # print(pos3)
    # index3 = pos3+15
    # while True:
    #     #print (lines3[index3])
    #     if lines3[index3]=='"':
    #         #print(',\n')
    #         newFile.write(',\n')
    #         break
    #     else :
    #         #print(str(lines2[index2]))
    #         newFile.write(str(lines3[index3]))
    #         index3 += 1

category.close()
tag.close()
newFile.close()