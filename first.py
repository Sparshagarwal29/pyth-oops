# create a class car with brands and model as attributes,then create an instance of this class 
class Car:  # classes name is always in captical letter 
    def __init__(self, brand,model):  # this __init__ is method constructor 
        self.brand = brand
        self.model = model
    def fullname(self):
        return f"{self.brand} {self.model}"


my_car = Car("Toyota", "Corolla")  
print(f"My car is a {my_car.brand} {my_car.model}.")  
print(f"{my_car.fullname()}.")  



# make a electric car that inherit the car and has attribute of batter size 

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size
my_tesla =  ElectricCar("Tesla", "Model S","100kwh")
print(my_tesla.fullname())


#  encapsulation --> to make a attribute private we need to put "__ "  for eg self.__brand would make the brand attribute pvt

