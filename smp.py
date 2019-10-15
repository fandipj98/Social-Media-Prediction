file_baru = open("tags.txt","a")
with open("train_tags.json", "r") as f:
    lines = f.read()
    pos = -1
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
            file_baru.write(str(count))
            break
        file_baru.write(str(count)+',')
file_baru.close()