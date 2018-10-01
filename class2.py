class student:
    def __init__(self):
        name=str()
        age=int()
        branch=str()
    def fill_data(self,name,age,branch):
        self.name=name
        self.age=age
        self.branch=branch
    def getdata(self):
        print("name: {0}\nage: {1}\nbranch: {2}".format(self.name,self.age,self.branch))
    def concat_obj(self,s1,s2):
        self.name=s1.name+" "+s2.name
        self.age=s1.age+s2.age
        self.branch=s1.branch
def main():
    a=student()
    b=student()
    c=student()
    a.fill_data("Nishank",10,"CS")
    b.fill_data("Singh",10,"CS")
    c.concat_obj(a,b)
    c.getdata()

main()
