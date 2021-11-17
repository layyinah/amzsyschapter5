def peep(itr):
    return iter(list(iter))
it=iter(range(5))
it1=peep(it)
print(it1)