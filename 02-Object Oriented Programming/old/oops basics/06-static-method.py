# Add a static method to the car class that returns a general description of the car

# These are the methods that belong to a class and not to a instance of that class

# A car class
class Car:
    def __init__(self, user_brand, user_model):
        # attributes
        self.brand = user_brand
        self.model = user_model

    # method
    def fullName(self):
        return self.brand + " " + self.model

    @staticmethod
    def generalDescription():
        return "This is a good car"

# An instance
# A Object of the class Car
myCar = Car("Toyota", "Corolla")

# print(myCar.generalDescription())
print(Car.generalDescription())