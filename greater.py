import sys

a=int(input())
b=int(input())
c=int(input())
if(a>b):
    if(a>c):
        print("a is greatest i.e {}".format(a))
    elif(a==c):
        print("a and c are greatest i.e {}".format(a))
    else:
        print("c is greatest i.e {}".format(c))
elif(b>a):
    if(b>c):
        print("b is greatest i.e {}".format(b))
    elif(b==c):
        print("b and c are greatest i.e {}".format(b))
    else:
        print("c is greatest i.e {}".format(c))
elif(a==b and a!=c):
    print("a and b are greatest i.e {}".format(a))
elif(a==b and a==c):
    print("a, b and c are equal i.e {}".format(a))
