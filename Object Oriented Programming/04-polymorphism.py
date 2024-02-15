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

    # fuel method
    def fuelType(self):
        return "Petrol/Diesel"

# ElctricCar class
class ElectricCar(Car):
    def __init__(self, user_brand, user_model, battery_size):
        super().__init__(user_brand, user_model)
        self.battery_size = battery_size

    # fuel method
    def fuelType(self):
        return "Electric Charge"


# An instance
# A Object of the class Car
myCar = Car("Toyota", "Corolla")
print(f'This is a non EV car. It takes {myCar.fuelType()} as fuel.')
# print(myCar.brand)
# print(myCar.model)

# print(myCar.fullName())

myEV = ElectricCar("Tesla", "Model X", "85kWh")
print(f'This is a EV. It takes {myEV.fuelType()} as fuel.')
# print(myEV.brand)
# print(myEV.model)
# print(myEV.battery_size)
# print(myEV.fullName())