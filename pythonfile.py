import sys
import os
def find_files(dir):
	f=os.listdir(os.path.abspath(dir))
	for i in f:
		print (os.path.abspath(dir+'/'+i))
		if os.path.isdir(os.path.abspath(dir+'/'+i)):
			find_files(dir+'/'+i)
find_files(sys.argv[1])
