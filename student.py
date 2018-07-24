import sys
class student:
    def __init__(self):
        self.__name="NAME"
        self.__sem="SEM"
        self.__branch="BRANCH"
    def fill_data(self,name,sem,branch):
        self.__name=name
        self.__sem=sem
        self.__branch=branch
    def get_details(self):
        return self.__name,self.__sem,self.__branch
    def cpy_obj(self,ob):
        ob.fill_data(self.__name,self.__sem,self.__branch)
    def print_data(self):
        print("NAME: {0}\nSEM: {1}\nBRANCH: {2}".format(self.__name,self.__sem,self.__branch))

def main():
    s1=student()
    s2=student()
    s3=student()
    s1.fill_data(input("NAME: "),input("SEM: "),input("BRANCH: "))
    sys.stdout.flush()
    s2.fill_data(input("NAME: "),input("SEM: "),input("BRANCH: "))
    s2.cpy_obj(s3)
    s2.print_data()
    s3.print_data()

main()
