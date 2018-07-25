import re
s="the quick brow_fox jumps over the lazy dog"
s=s.replace(" ","+")
s=s.replace("_"," ")
s=s.replace("+","_")
print(s)
