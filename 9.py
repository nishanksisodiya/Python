def name():
    fname=input("first name: ")
    lname=input("last name: ")
    return fname,lname

def main():
    n, m=name()
    print("{0} {1}".format(n,m))

main()
