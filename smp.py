import time

newFile = open("data.csv","a")
tag = open("train_tags.json", "r")
category = open("train_category.json", "r")
temporal = open("train_temporalspatial.json", "r")
label = open("train_label.txt", "r")

lines = tag.read()
pos = -1

lines2 = category.read()
pos2 = -1
pos3 = -1
pos4 = -1

lines3 = temporal.read()
pos_postdate = -1

lines4 = label.read()
pos5 = 0

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
            newFile.write(',')
            break
        else :
            #print(str(lines2[index2]))
            newFile.write(str(lines2[index2]))
            index2 += 1

    pos3 = lines2.find('Concept', pos3+1)
    #print(pos3)
    index3 = pos3+11
    while True:
        #print (lines3[index3])
        if lines2[index3]=='"':
            #print(',\n')
            newFile.write(',')
            break
        else :
            #print(str(lines2[index2]))
            newFile.write(str(lines2[index3]))
            index3 += 1
    
    pos4 = lines2.find('Subcategory', pos4+1)
    #print(pos4)
    index4 = pos4+15
    while True:
        #print (lines3[index3])
        if lines2[index4]=='"':
            #print(',\n')
            newFile.write(',')
            break
        # else if lines2[index4]==',':
        #     newFile.write(' ')
        else :
            #print(str(lines2[index2]))
            newFile.write(str(lines2[index4]))
            index4 += 1

    
    pos_postdate = lines3.find('Postdate', pos_postdate+1)
    #print(pos4)
    index_postdate = pos_postdate+12
    my_second = 0
    while True:
        #print (lines3[index3])
        if lines3[index_postdate]=='"':
            #print(',\n')
            # newFile.write(',\n')
            break
        else :
            #print(str(lines2[index2]))
            my_second=my_second*10+int(lines3[index_postdate])
            index_postdate +=1
            # newFile.write(str(lines3[index_postdate]))
            # lines3[index_postdate]

    #print(my_second)
    timeArray = time.localtime(my_second)
    datetime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    newFile.write(str(datetime) + ',')

    
    while True:
        if lines4[pos5]=='\n':
            newFile.write('\n')
            pos5 += 1
            break
        else:
            newFile.write(str(lines4[pos5]))
            pos5 += 1
    
label.close()
temporal.close()
category.close()
tag.close()
newFile.close()