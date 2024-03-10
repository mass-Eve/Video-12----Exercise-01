# Customer Class
class Customer:

    # Constructor
    def __init__(self, name, gender, address):
        self.name = name
        self.gender = gender
        self.address = address

        self.customerDetails()

    def customerDetails(self):
        print(f'CUSTOMER NAME : {self.name}')
        print(f'GENDER : {self.gender}')

        # method 1
        print(f'CITY : {self.address.city}')
        print(f'STATE : {self.address.state}')
        print(f'PINCODE : {self.address.pincode}')

        # method 2
        self.address.accessAddress()

class Address:
    
    # Constructor
    def __init__(self, city_name, state_name, pincode_number):
        self.city = city_name
        self.state = state_name
        self.pincode = pincode_number

    def accessAddress(self):
        print(f'CITY : {self.city}')
        print(f'STATE : {self.state}')
        print(f'PINCODE : {self.pincode}')

cust1Add = Address('Banglore', 'Karnataka', 560091)
cust1 = Customer(name = 'Nitish Kumar', gender = "Male", address = cust1Add)