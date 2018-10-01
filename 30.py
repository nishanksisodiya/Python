#file concatination

f=[open("f1.txt","r"),open("f2.txt","r")]
s1=sum(1 for line in f[0])
s2=sum(1 for line in f[1])
f[0].seek(0)
f[1].seek(0)
min=s1
if(min>s2):
    min=s2
for i in range(0,min):
    print(("{0}. {1}").format(f[0].readline().rstrip("\n"),f[1].readline().rstrip("\n")))
