#Simple Intrest

def loan(pri,rate=2,time=10):
    amt=pri*rate*time
    print("amt is :{}".format(amt))

loan(20000)
loan(20000,12.50)
loan(20000,12.5,20)
