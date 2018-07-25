import re
s="The quick brown fox jumps over the lazy dog"
a=str(input())
x=re.search(a,s)
if x:
    print("FOUND")
else:
    print("NOT FOUND")
