class Computer:
    def __init__(self):
        self.__maxprice = 1000
 
    def sell(self):
        print('Laptop Selling Price: {}'.format(self.__maxprice))
 
    def setMaxPrice(self, price):
        self.__maxprice = price
 
laptop = Computer()
laptop.sell()
laptop.__maxprice = 1100
laptop.sell()
laptop.setMaxPrice(1100)
laptop.sell()
