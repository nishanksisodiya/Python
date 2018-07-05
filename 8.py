import sys
def even(n):
    if(n%2==0):
        print("even")
    else:
        print("odd")

a=int(sys.argv[1])
even(a)
