#slicing
st="I am a superhuman"
print("Q. what am I?\nA. {}".format("not a {}".format(st[-5::])))
if 'super' in st:
    print("found")
else:
    print("not found")
