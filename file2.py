#file2.py
filewrt=open("name.txt","w")
filewrt.write(".My name is Amit.\nAmit working as professor at SISTec.\nThere are two professor of Amit name at SISTec.")
filewrt.close()
filerd=open("name.txt","r")
d={}
for line in filerd:
    list=line.replace(".","")
    l=set(map(str,list.split()))
    for i in l:
        if i in d:
            d[i]=d[i]+1
        else:
            d[i]=1
max = 0
j= str()
for i in d:
    if(d[i]>max):
        max=d[i]
        j=i
print("{0}: {1}".format(j,d[j]))
