def enumerate(itr):
   ind=0
   for val in itr:
        print( ind, val)
        ind+=1

for i ,c in enumerate(["a","b","c"]):
    print(i,c)