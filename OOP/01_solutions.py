class Car:
    total_car = 0
    def __init__(self, brand, model):
        self.__brand = brand  # Private attribute
        self.__model = model
        Car.total_car += 1

    def get_brand(self):  
        return self.__brand + "!"  # Access private attribute correctly

    def full_name(self):
        return f"{self.__brand} {self.__model}"  # Correct attribute usage

    def fuel_type(self):
     return "petrol and diesel"
    @staticmethod
    def general_desc():
     return "cars are awesome"
    @property
    def model(self):
     return self.__model 
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    def fuel_type(self):
     return "Electricity" 

my_tesla = ElectricCar("Tesla", "Model S",
 "85KWH")
print (isinstance(my_tesla, ElectricCar))
print (isinstance(my_tesla, Car))
# my_tesla.model = "Model X"
# print(my_tesla.model)  # Now this will work

# # safare = Car("tata", "safari")
# # print(safare.general_desc())

# print(Car.general_desc())