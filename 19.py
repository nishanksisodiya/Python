str=input()
char=0
num=0
oth=0
l=int(len(str))
for i in range(0,l):
    if str[i].isalpha():
        char+=1
    elif str[i].isdigit():
        num+=1
    else:
        oth+=1

print("Characters: {0}\nNumbers: {1}\nOthers: {2}".format(char,num,oth))
