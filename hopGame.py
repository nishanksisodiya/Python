import numpy as np, queue as q
def main():
    N=int(input())
    arr=np.array(list(map(int,input().split(","))))
    s2=list()
    s1=list()
    for i in range(-1,N-3):
        s2.append(3*(arr[i+3]))
    skip2=np.array(s2)
    for i in range(-1,N-2):
        s1.append(2*(arr[i+2]))
    skip1=np.array(s1)
    print(skip2)
    print(skip1)
    score=0
    doubleJump=0
    i=0
    while(i<N):
        j=
        if()

main()
