#zip function
name=['nishank','prateek','lalit','harshal','shankhabrata das']
roll_no=[2,3,4,5,33]
marks=[100,23,56,90,101]
m=list(zip(name,roll_no,marks))
print("{0:35s}{1:20s}{2:}".format("NAME","ROLL NO","MARKS"))
for i in range(len(m)):
    print("{0:20s}{1:20d}{2:20d}".format(m[i][0],m[i][1],m[i][2]))
