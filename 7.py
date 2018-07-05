arr=list(map(int,input().split()))
n=len(arr)
sum=0
for i in range(0,n):
    sum=sum+arr[i]
avg=sum/n
print("SUM: {0}\nAVG: {1}".format(sum,avg))
