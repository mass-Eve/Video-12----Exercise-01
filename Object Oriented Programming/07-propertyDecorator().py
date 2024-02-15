# Use a @propertydecorator to make the module attribute read-only

# A car class
class Car:
    def __init__(self, user_brand, user_model):
        # attributes
        self.brand = user_brand
        self.__model = user_model

    # method
    def fullName(self):
        return self.brand + " " + self.__model

    @property   
    def accessModel(self):
        return self.__model

# An instance
# A Object of the class Car
myCar = Car("Toyota", "Corolla")
print(myCar.brand)
# print(myCar.model)
print(myCar.accessModel)

print(myCar.fullName())