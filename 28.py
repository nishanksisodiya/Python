#file wrl to a file
import random
class filewrt:
    def __init__(self):
        self.__l=list(map(str,input().split()))
    def writedata(self):
        file=open("list.txt","a+")
        for i in self.__l:
            file.write(i+" ")
        file.write("\n")
        file.close()

class filerd:
    def __init__(self):
        self.__n=int()

    def print_lines(self):
        file=open("list.txt","r")
        for i in file:
            print(i,end='')
        file.close()

    def max_word(self):
        file=open("list.txt","r")
        max=0
        for i in file:
            j=list(map(str,i.split()))
            for word in j:
                if(max<len(word)):
                    max=len(word)
        print(max)
        file.close()

    def print_nthline(self):
        self.__n=int(input("number of line to print: "))
        file=open("list.txt","r+")
        f=file.readlines()
        print(f[self.__n-1])
        file.close()

    def print_rndmline(self):
        file=open("list.txt","r+")
        sm=sum(1 for line in file)
        file.seek(0,0)
        self.__n=random.randrange(1,sm)
        f=file.readlines()
        print(f[self.__n-1])
        file.close()

    def print_nlines(self):
        j=1
        file=open("list.txt","r")
        for i in file:
            if(j>self.__n):
                break
            else:
                print(i,end='')
                j+=1
        file.close()

def main():
    a=filewrt()
    a.writedata()
    b=filerd()
    b.max_word()

main()
