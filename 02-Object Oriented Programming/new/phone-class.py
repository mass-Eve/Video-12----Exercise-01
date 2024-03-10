class Phone:
    def __init__(self, company, name, price):
        self.brand = company
        self.phone_name = name
        self.selling_price = price

    def accessDetails(self):
        print(f'BRAND : {self.brand}')
        print(f'PHONE NAME : {self.phone_name}')
        print(f'COST : {self.selling_price}')

class FeaturePhone(Phone):
    def __init__(self, company, name, price):
        print("This is a feature phone")
        super().__init__(company, name, price)

class SmartPhone(Phone):
    def __init__(self, company, name, price):

        # calling the init from the parent class to assign the basic phone details
        super().__init__(company, name, price)

        # These attributes are unique to smartphone only
        print("This is a smart phone")
        self.camera_mp = int()
        self.cameras = int()
        self.screen = str()
        self.processor = str()

    def addSmartPhoneDetails(self):
        camera_mp = int(input("Camera Megapixels : "))
        self.camera_mp = camera_mp
        total_cameras = int(input("Enter the total number of cameras in the phone : "))
        self.cameras =  total_cameras
        screen_type = input("Screen Type : ")
        self.screen =  screen_type
        process = input("Processor : ")
        self.processor = process

    def accessDetails(self):
        super().accessDetails()

        print(f'Camera Megapixels : {self.camera_mp}')
        print(f'Total Number Of Cameras{self.cameras}')
        print(f'Type Of Screen or Display{self.screen}')
        print(f'Processor : {self.processor}')

# f1 = FeaturePhone('Itel', "Itel 4G", 1500)
# print(f1.brand)                  # >>>> Itel

s1 = SmartPhone("Samsung", "S40 Ultra", 200000)
s1.addSmartPhoneDetails()
s1.accessDetails()