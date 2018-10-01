dict1={1:'nony',2:'lalit',3:'shikha',4:'harshal'}
print(dict1)
del(dict1[4])
for i in dict1:
    print(dict1[i])
print(dict1.get(20,'ERROR 404: NOT FOUND'))
#method call with object name
dict1.clear()
#method call with class name
dict.clear(dict1)
dict1={1:[input(x) for x in range(5)]}
print(dict1)
