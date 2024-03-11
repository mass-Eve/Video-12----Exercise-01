class StudentID:
    def __init__(self):
        self.name = str()
        self.kaksha = str()
        self.section = str()
        self.roll = int()
        self.gender = str()
        self.address = str()

    def createStudent(self):
        
        sname = input('Enter the name of the student : ')
        self.name = sname
        
        skaksha = input('Enter the kaksha of the student :')
        self.kaksha = skaksha
        
        sec = input('Enter the section student :')
        self.section = sec
        
        rollno = input('Enter the roll number of the student :')
        self.roll = rollno
        
        sgender = input('Enter the gender of the student :')
        self.gender = sgender
        
        add = input('Enter the address of the student :')
        self.address = add

    def updateDetails(self):

        # menu
        def menu(self):
            print("WHAT WOULD YOU LIKE TO UPDATE ?")
            print("1. ENTER 1 TO UPDATE THE NAME OF THE STUDENT ")
            print("2. ENTER 2 TO UPDATE THE KAKSHA OF THE STUDENT")
            print("3. ENTER 3 TO UPDATE THE SECTION OF THE STUDENT")
            print("4. ENTER 4 TO UPDATE THE ROLL NUMBER OF THE STUDENT")
            print("5. ENTER 5 TO UPDATE THE GENDER OF THE STUDENT")
            print("6. ENTER 6 TO UPDATE THE HOUSE ADDRESS OF THE STUDENT")

            choice = int(input("~ "))

        def updateName(self):
            newName = input("Enter the new name of the student : ")
            self.name = newName
        
        def updateKaksha(self):
            newKaksha = input("Enter the new kaksha of the student : ")
            self.name = newKaksha
        
        def updateSection(self):
            newSec = input("Enter the new section of the student : ")
            self.name = newSec
        
        def updateRoll(self):
            newRoll = input("Enter the new roll number of the student : ")
            self.name = newRoll
        
        def updateGender(self):
            newGen = input("Enter the gender number of the student : ")
            self.name = newGen
        
        def updateAdd(self):
            newAdd = input("Enter the new house address of the student : ")
            self.name = newAdd