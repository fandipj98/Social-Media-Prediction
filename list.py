getList = open("train_category.json","r")
output = open("listCategory.txt", "a")

listSubcategory = set()
textList = set()
compare = set()

lines = getList.read()
pos4 = -1
check = -1

text = ''

while True:
        
    pos4 = lines.find('Category', pos4+1)
    check = lines.find('Category', pos4+1)
    index = pos4+12

    if check == -1:
        break

    # print(index)
    while True:

        if lines[index] =='"':
            textList.add(text)
            # print('sini')
            # print (textList)
            if textList & listSubcategory == set():
                # print('sana')
                listSubcategory.add(text)
                # print(listSubcategory)
                output.write(text + '\n')          
            
            textList.clear()
            text = ''

            check = -1

            break

        elif lines[index] == ',' :
            textList.add(text)
            # print('sini')
            # print (textList)
            if textList & listSubcategory == set():
                # print('sana')
                listSubcategory.add(text)
                # print(listSubcategory)
                output.write(text + '\n')          
            
            textList.clear()
            text = ''

            index+=1
            
        else :
            text = text + lines[index]
            index += 1

        # if pos4 > 16:
        #     break

output.close()
getList.close()



