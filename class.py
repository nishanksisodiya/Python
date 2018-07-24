#note:
#class and object:
# __var_name = private
#_var_name = protected
#var_name = public

import random
class coin:
    def __init__(self):
        self.side='heads'
    def toss(self):
        x=random.randint(0,1)
        if(x==1):
            self.side='tails'

def main():
    c=coin()
    c.toss()
    print(c.side)

main()
