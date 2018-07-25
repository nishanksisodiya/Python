import re
def main():
    file=open("regular.txt","r+")
    s="Sc Sistec BhoPal Sistec  Sisiec"
    ul=re.findall("^[A-Z]{1}[a-z]+|[ ]+[A-Z]{1}[a-z]+[ ]+",s)
    print(ul)

main()
