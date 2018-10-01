a,b=map(int,input().split())
try:
    c=a/b
    print(c)
except ZeroDivisionError:
    print("Enter a non-zero denominator")
finally:
    print("Exception Handled")
