class Automobile:
    def __init__(self,make,model,mileage,price):
        self.__make=make
        self.__model=model
        self.__mileage=mileage
        self.__price=price
    def set_make(self):
        self.__make=make
    def set_model(self):
        self.__model=model
    def set_mileage(self):
        self.__mileage=mileage
    def set_price(self):
        self.__price=price
    def get_make(self):
        return self.__make
    def get_model(self):
        return self.__model
    def get_mileage(self):
        return self.__mileage
    def get_price(self):
        return self.__price

class car(Automobile):
    def __init__(self,make,model,mileage,price,doors):
        Automobile.__init__(self,make,model,mileage,price)
        self.__doors=doors
    def set_make(self):
        self.__make=make
    def get_doors(self):
        return self.__doors

def main():
    Batmobil=car("BATMOBIL","2018","Nahi Deti","Aukat K Bahar","NOPE")
    print("MAKE: {0}\nMODEL: {1}\nMILEAGE: {2}\nPRICE: {3}\nDOORS: {4}".format(Batmobil.get_make(),Batmobil.get_model(),Batmobil.get_mileage(),Batmobil.get_price(),Batmobil.get_doors()))
main()
