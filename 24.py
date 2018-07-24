strr=list(map(str,input().split()))
fq=dict.fromkeys(strr,0)
for i in strr:
    fq[i]+=1;
print(fq)
