#check range

def in_range(num1,num2):
    a=int(input("enter number: "))
    flag=0
    if(a in range(num1,num2)):
        flag=1
    return flag
def main():
    n1=int(input("enter lower bound: "))
    n2=int(input("enter upper bound: "))
    fg=in_range(n1,n2)
    if(fg==1):
        print("in range")
    else:
        print("out of range")
main()
