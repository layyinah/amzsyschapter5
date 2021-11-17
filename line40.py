import sys


def readfiles(filenames):
    for f in filenames:
        for line in open(f):
            yield line

def printlines(files):
    for line in files:
        if len(line)>40:
            print(line)
        else:
            print("file doesnt exist")

def main():
    if len(sys.argv)>1:
        filenames=sys.argv[1:]
        files=readfiles(filenames)
        printlines(files)
