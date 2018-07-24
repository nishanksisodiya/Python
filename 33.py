import re
file=open("regular.txt","r+")
t=file.read()
file.seek(0,0)
i=str(input())
f=(f"^{i}")
for i in file:
    if re.search(f,i):
        print(i)
print(len(re.findall("DATE",t)))
file.close()
