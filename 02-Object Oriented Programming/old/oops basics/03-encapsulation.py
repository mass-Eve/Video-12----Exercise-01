# Modify the Car class to encapsulate (private) the brand attribute, making it private, and provide a better method for it.abs

# A car class
class Car:
    def __init__(self, user_brand, user_model):
        # attributes
        self.__brand = user_brand
        self.model = user_model

    def getBrandName(self):
        return self.__brand

    # method
    def fullName(self):
        return self.__brand + " " + self.model

# An instance
# A Object of the class Car
myCar = Car("Toyota", "Corolla")
# print(myCar.__brand)
print(myCar.getBrandName())

print(myCar.fullName())