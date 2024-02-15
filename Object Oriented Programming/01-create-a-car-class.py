# A car class
class Car:
    def __init__(self, user_brand, user_model):
        # attributes
        self.brand = user_brand
        self.model = user_model

    # method
    def fullName(self):
        return self.brand + " " + self.model

# An instance
# A Object of the class Car
myCar = Car("Toyota", "Corolla")
print(myCar.brand)
print(myCar.model)

print(myCar.fullName())