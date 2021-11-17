import os.path
import sys


def getdir(dir):
    for dirnme in os.listdir(dir):
        yield os.path.join(dir,dirnme)
def pythonext(dir='.'):
    c=0
    for i in getdir(dir):
        if os.path.isfile(i):
            if i[-3:] == '.py':
                c+=1
        else:
            pythonext(i)
    if c>0:
        print ("number of python files :",c ,"\t","directory where"
                                                  " python file exist=" ,dir)

if len(sys.argv)>1:
    pythonext(sys.argv[1])
else:
    pythonext()