class Taxi:
    __number_of_taxis  = 0
    __price_per_km = 3.5
    __opening_price = 5.0
 
    def __init__(self,driver):
        self.driver = driver
        self.__total_earning = 0.0
        Taxi.__number_of_taxis  =  Taxi.__number_of_taxis + 1
 
    def calculate_trip_price(self, km):
        self.trip_price = Taxi.__opening_price + (Taxi.__price_per_km * km)
        self.__total_earning += self.trip_price
        return self.trip_price
              
    def number_of_taxis():
        return Taxi.__number_of_taxis
    
    def total_earning(self):
        return self.__total_earning
    
first_vehicle = Taxi("John")
second_vehicle = Taxi("Jack")
third_vehicle = Taxi("Tom")
print(first_vehicle.calculate_trip_price(20))
print(second_vehicle.calculate_trip_price(30))
print(first_vehicle.calculate_trip_price(10))
print(Taxi.number_of_taxis())
print(first_vehicle.total_earning())
