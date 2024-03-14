from book_class import Book

class StudentID(Book):
    def __init__(self):
        self.name = str()
        self.kaksha = str()
        self.section = str()
        self.roll = int()
        self.gender = str()
        self.address = str()
        self.sID = str()
        self.books_issued = [Book()] * 5

    def createStudent(self):
        try:
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

            self.assignStudentID()

        except Exception as e:
            print(f"Student Can not be added because of the following error ~ {str(e)}")

    def showDetails(self):
        print(f'{self.name}')
        print(f'{self.kaksha} {self.section}')
        print(f'{self.sID}')

    def updateDetails(self):

        def menu(self):
            while(True):
                # menu
                print("----------------------------------------------------------")
                print("WHAT WOULD YOU LIKE TO UPDATE ?")
                print("1. ENTER 1 TO UPDATE THE NAME OF THE STUDENT ")
                print("2. ENTER 2 TO UPDATE THE KAKSHA OF THE STUDENT")
                print("3. ENTER 3 TO UPDATE THE SECTION OF THE STUDENT")
                print("4. ENTER 4 TO UPDATE THE ROLL NUMBER OF THE STUDENT")
                print("5. ENTER 5 TO UPDATE THE GENDER OF THE STUDENT")
                print("6. ENTER 6 TO UPDATE THE HOUSE ADDRESS OF THE STUDENT")
                print("----------------------------------------------------------")

                choice = int(input("~ "))

                match choice:
                    case 1:
                        updateName()
                    case 2:
                        updateKaksha()
                        self.assignStudentID()
                    case 3:
                        updateSection()
                        self.assignStudentID()
                    case 4:
                        updateRoll()
                        self.assignStudentID()
                    case 5:
                        updateGender()
                        self.assignStudentID()
                    case 6:
                        updateAdd()
                    case _:
                        print("Check your inputs and try again later")

        def updateName(self):
            try:
                newName = input("Enter the new name of the student : ")
                self.name = newName
            except Exception as e:
                print(f"Can not perforn updation because of the following error ~ {str(e)}")
        
        def updateKaksha(self):
            try:
                newKaksha = input("Enter the new kaksha of the student : ")
                self.kaksha = newKaksha
            except Exception as e:
                print(f"Can not perforn updation because of the following error ~ {str(e)}")
        
        def updateSection(self):
            try:
                newSec = input("Enter the new section of the student : ")
                self.section = newSec
            except Exception as e:
                print(f"Can not perforn updation because of the following error ~ {str(e)}")
        
        def updateRoll(self):
            try:
                newRoll = int(input("Enter the new roll number of the student : "))
                self.roll = newRoll
            except Exception as e:
                print(f"Can not perforn updation because of the following error ~ {str(e)}")
        
        def updateGender(self):
            try:
                newGen = input("Enter the gender number of the student : ")
                self.gender = newGen
            except Exception as e:
                print(f"Can not perforn updation because of the following error ~ {str(e)}")
        
        def updateAdd(self):
            try:
                newAdd = input("Enter the new house address of the student : ")
                self.address = newAdd
            except Exception as e:
                print(f"Can not perforn updation because of the following error ~ {str(e)}")

    def assignStudentID(self):
        try:
            self.sID = self.kaksha + self.section + self.roll + self.gender
        except Exception as e:
            print(f"Student ID can not be as assigned due to the following error ~ {str(e)}")

    def borrow_list(self):
        books = len(self.books_issued)

        if (books == 5):
            print("You can not borrow any book. You have exceeded the limit.")
            return False
        elif (books >= 0 and books < 5):
            print(f'You can borrow {books} books.')
            return True
        else:
            print("MANAGEMENT PROBLEM")

    def borrowBook(self):

        if (self.borrow_list()):
            print("YOU ARE IN THE CHECKOUT KIOSK.")
            print('PLEASE CONFIRM YOUR DETAILS ~ ')

            self.showDetails()

            choice = input("Enter Y to confirm your details : ")

            # if (choice = 'Y'):


    def returnBook(self):
        pass

# s1 = StudentID()