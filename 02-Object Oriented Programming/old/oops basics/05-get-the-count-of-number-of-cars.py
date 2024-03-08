# A car class
class Car:
    totalCars = 0

    def __init__(self, user_brand, user_model):
        # attributes
        self.brand = user_brand
        self.model = user_model

        Car.totalCars += 1

    # method
    def fullName(self):
        return self.brand + " " + self.model

# An instance
# A Object of the class Car
myCar = Car("Toyota", "Corolla")
# print(myCar.brand)
# print(myCar.model)
myCar2 = Car("Tata", "Nexon")
# print(myCar.fullName())

print(Car.totalCars)