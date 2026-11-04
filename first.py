# create a class car with brands and model as attributes,then create an instance of this class 
class Car:  # classes name is always in captical letter 
    def __init__(self, brand,model):
        self.brand = brand
        self.model = model


my_car = Car("Toyota", "Corolla")  # creating an instance of the Car class
print(f"My car is a {my_car.brand} {my_car.model}.")  # accessing the attributes of the instance

