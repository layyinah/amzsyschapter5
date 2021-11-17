import sys
import os

def findall(find):
    for files,path,dir in os.walk(os.getcwd()):
        if find in files:
            print (os.path.join(path,find))
findall(sys.argv[1])