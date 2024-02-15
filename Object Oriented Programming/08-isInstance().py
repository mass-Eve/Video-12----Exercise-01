# create a clas ElectricCar that inherits from the class Car and has an additional attribute battery_size 

# A car class
class Car:
    def __init__(self, user_brand, user_model):
        # attributes
        self.brand = user_brand
        self.model = user_model

    # method
    def fullName(self):
        return self.brand + " " + self.model

# ElctricCar class
class ElectricCar(Car):
    def __init__(self, user_brand, user_model, battery_size):
        super().__init__(user_brand, user_model)
        self.battery_size = battery_size

# An instance
# A Object of the class Car
myCar = Car("Toyota", "Corolla")

myEV = ElectricCar("Tesla", "Model X", "85kWh")

print(isinstance(myEV, Car))
print(isinstance(myEV, ElectricCar))