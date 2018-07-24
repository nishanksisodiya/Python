import os
def main():
    c=1
    while c!=6:
        os.system("cls")
        print("press 1 for insert")
        print("press 2 for read")
        print("press 3 for search")
        print("press 4 for update")
        print("press 5 for delete")
        print("press 6 for exit")
        c=int(input(("ENTER YOUR CHOICE \n")))
        if c==1:
            os.system("cls")
            file=open('p.txt','a+')
            ids=input("id: ")
            name=input("name: ")
            branch=input("branch: ")
            file.write(ids+" ")
            file.write(name+" ")
            file.write(branch)
            file.write("\n")
            file.close()

        elif c==2:
            os.system("cls")
            file=open('p.txt','r')
            a=file.read()
            print(a)
            file.close()

        elif c==3:
            os.system("cls")
            s=str(input("enter the id to search \n"))
            file=open('p.txt','r+')
            flag=1
            for word in file:
                for i in list(word.split()):
                    if(i==s):
                        flag=0
                        break
                if(flag==0):
                    break
            if(flag==0):
                print("Found")
            else:
                print("Not Found")
            file.close()

        elif c==4:
            os.system("cls")
            t=input("enter the text you want to be updated: ")
            s=input("enter the text to update: ")
            file=open('p.txt','r+')
            w=open('n.txt','w+')
            for word in file:
              for i in s:
                    word=word.replace(t,s)
                    w.write(word)
            file.close()
            w.close()
            os.remove('p.txt')
            os.rename('n.txt','p.txt')
            print("your data is succesfuly Updated \n")
        elif c==5:
            os.system("cls")
            t=str(input("enter the id to be deleted \n"))
            file=open("p.txt","r+")
            lines=file.readlines()
            file.close()
            file=open("p.txt","w+")
            file.truncate()
            for line in lines:
                if t not in line:
                    file.write(line)
            file.close()
            print("your data is succesfuly deleted \n")
        elif c==6:
            os.system("cls")
            print("Thank You for Using!!")
            print("Exiting!!")
        else:
            print("Invalid choice!!")
        if(c!=6):
            input("\n\n\nPRESS ANY KEY TO CONTINUE")

main()
