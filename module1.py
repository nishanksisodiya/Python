#%%writefile module1.py
#Create class in module

import random
class coin:
    def __init__(self):
        self.__side='H'
    def toss(self):
        if random.randint(0,1):
            self.__side='HEADS'
        else:
            self.__side='TAILS'
        return self.__side

class name:
    def __init__(self):
        self.__name=input()
    def getname(self):
        print("Name is: {}".format(self.__name))
