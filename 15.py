#perfect numbeir

def check_perfect_number(num):
    sum=0
    for i in range(1,num):
        if(num%i==0):
            sum=sum+i
    flag=0
    if(sum==num):
        flag=1
    return flag

def main():
    n=int(input())
    for i in range(1,(n+1)):
        c=check_perfect_number(i)
        if(c==1):
            print(i)

main()
