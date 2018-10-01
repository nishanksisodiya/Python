#class and object to store data of student

class student:
    def __init__(self,rno,name):
        self.rollno=rno
        self.__name=name
    def getdata(self):
        print("Name: {0}\nRoll No.: {1}".format(self.__name,self.rollno))

def main():
    name=input()
    rno=int(input())
    s=student(rno,name)
    s.getdata()

main()
