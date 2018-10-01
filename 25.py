a=set(map(str,input().split()))
d={}
for i in a:
    if i[0] in d:
        d[i[0]].append(i)
    else:
        d[i[0]]=[i]
print(d);
