import math
n=int(input())
w=(n//2)+1
for i in range(0,n):
    for j in range(0,w):
        if(i==0 or i==n-1):
            if(j!=w-1):
                print("*",end=" ")
        elif((i!=0 or i!=n-1) and (j==0 or j==w-1)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
