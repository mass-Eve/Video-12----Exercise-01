class ATM:

    # a static variable to store the count of total bank accounts assosciated with this branch
    total_accounts = 0
    
    def __init__(self):
        self.__pin = 1234
        self.__balance = 0

        # updating the value of total_accounts variables whenever a new instance of this class is created, which basically means a new account has been opened in this branch
        ATM.total_accounts += 1

        # assigning that value as the account number of that account
        self.__accountNumber = 100000 + ATM.total_accounts

        self.menu()

    def menu(self):
        user_input = int(input('''
        ------------------------------------------------------------------
                                    WELCOME
                        HOW WOULD YOU LIKE TO PROCEED ?
                        0. ENTER 0 TO SEE YOUR ACCOUNT NUMBER
                        1. ENTER 1 TO CREATE NEW PIN
                        2. ENTER 2 TO CHANGE YOUR EXISTING PIN
                        3. ENTER 3 TO DEPOSIT CASH
                        4. ENTER 4 TO WTIHDRAW CASH
                        5. ENTER 5 TO SEE YOUR CURRENT BALANCE
                        6. ENTER 6 TO EXIT
        ------------------------------------------------------------------
                        ENTER YOUR CHOICE HERE ~ '''))
        if user_input == 0:
            self.displayAccountHolderDetails()
        elif user_input == 1:
            self.createPin()
        elif user_input == 2:
            self.updatePin()
        elif user_input == 3:
            self.deposit()
        elif user_input == 4:
            self.withdraw()
        elif user_input == 5:
            self.check_balance()
        elif user_input == 6:
            print("\t\t\tVISIT US AGAIN. BYE.......")
            exit(0)
        else:
            print("CHECK YOUR INPUT AND TRY AGAIN .........")

    def displayAccountHolderDetails(self):
        temp = int(input("Verify your pin please : "))
        if (self.__pin == temp):
            print(f'ACCOUNT NUMBER : {self.__accountNumber}')
            print(f'CURRENT BALANCE : {self.__balance}')
        else:
            print("WRONG PIN! CANNOT ACCESS YOUR DETAILS AT THE MOMENT!")

    def createPin(self):
        self.__pin = int(input("Enter your pin here : "))
        print("PIN SET SUCCESSFULLY")
    
    def updatePin(self):
        verify = int(input("Enter your current ATM PIN : "))
        if (verify == self.__pin):
            self.__pin = int(input("Enter your new pin : "))
            print("PIN UPDATED SUCCESSFULLY")
        else:
            print("WRONG PIN! Please try again later ........")

    def deposit(self):
        amt = int(input("Enter the amount to be deposited in your bank account : "))

        pin = int(input("Enter your pin : "))
        if (pin == self.__pin):
            self.__balance += amt
            print(f"Rs. {amt} DEPOSITED SUCCESSFULLY IN YOUR BANK ACCOUNT")
        else:
            print("WRONG PIN! Please try again later ........")

    def withdraw(self):
        amt = int(input("Enter the amount to be withdrawn from your bank account : "))
        pin = int(input("Enter your pin : "))
        if (pin == self.__pin and (self.__balance - amt) > 0 ):
            self.__balance -= amt
            print(f"Rs. {amt} WITHDRAWED SUCCESSFULLY FROM YOUR BANK ACCOUNT")
        else:
            if (pin != self.__pin):
                print("WRONG PIN! Please try again later ........")
            else:
                print("INSUFFICIENT BALANCE")

    def check_balance(self):
        pin = int(input("Enter your ATM pin :"))
        if (pin == self.__pin):
            print(f"Your current balance is : Rs {self.__balance}")
        else:
            print("Invalid PIN!")

sbi = ATM()