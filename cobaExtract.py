import shutil
import os.path

with open('testSet.txt','wb') as output:
    for path, f_name in files:
        with open(os.path.join(path, f_name), 'rb') as input:
            shutil.copyfileobj(input, output)
        output.write(b'\n') # insert extra newline between files