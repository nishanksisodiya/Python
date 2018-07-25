import re
s="the quick brow fox jumps over the lazy dog"
a=str(input())
x=re.findall(a,s)
print(len(x))
