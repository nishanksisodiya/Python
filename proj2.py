import re
def main():
#    help(re)
    file=open("regular.txt","r+")
    s="SISTec Sistec bhopal."
    ul=re.findall("[A-z]*.$",s)
    print(ul)

main()
