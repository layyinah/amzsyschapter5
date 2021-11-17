import sys


def reverseiter(list):
    for i in reversed(list):
        yield i
    raise StopIteration()
reverseiter(sys.argv[1])