# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 14:41:54 2018

@author: ADMIN
"""

#FILE LOGIN


def login( f , l, i):
    iid=f[0:3]+l[0:3]+i[0:3]
    return iid

def password(strin):
    a=0
    b=0
    c=0
    for i in strin:
        if(i.isupper()):
            a+=1
        elif(i.islower()):
            b+=1
        elif(i.isdigit()):
            c+=1
    if(a>=1 and b>=1 and c>=1 and len(strin)>=7):
        print("Account Created")
    else:
        print("Incorrect Password")