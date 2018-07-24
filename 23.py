d1={1:'name',2:'name1'}
d2={1:'name',2:'name1'}
d3={1:'name',2:'name3'}

flag=1
for i in d1:
    if(d1[i]==d2[i]):
        flag=0
if(flag==1):
    print("unequal")
else:
    print("equal")
