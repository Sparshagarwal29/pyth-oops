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

