class ATM:
    def __init__(self):
        self.pin = 1234
        self.balance = 0

        self.menu()

    def menu(self):
        user_input = int(input('''
        ------------------------------------------------------------------
                                    WELCOME
                        HOW WOULD YOU LIKE TO PROCEED ?
                        1. ENTER 1 TO CREATE NEW PIN
                        2. ENTER 2 TO CHANGE YOUR EXISTING PIN
                        3. ENTER 3 TO DEPOSIT CASH
                        4. ENTER 4 TO WTIHDRAW CASH
                        5. ENTER 5 TO SEE YOUR CURRENT BALANCE
                        6. ENTER 6 TO EXIT
        ------------------------------------------------------------------
                        ENTER YOUR CHOICE HERE ~ '''))

        if user_input == 1:
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

    def createPin(self):
        self.pin = int(input("Enter your pin here : "))
        print("PIN SET SUCCESSFULLY")
    
    def updatePin(self):
        verify = int(input("Enter your current ATM PIN : "))
        if (verify == self.pin):
            self.pin = int(input("Enter your new pin : "))
            print("PIN UPDATED SUCCESSFULLY")
        else:
            print("WRONG PIN! Please try again later ........")

    def deposit(self):
        amt = int(input("Enter the amount to be deposited in your bank account : "))

        pin = int(input("Enter your pin : "))
        if (pin == self.pin):
            self.balance += amt
            print(f"Rs. {amt} DEPOSITED SUCCESSFULLY IN YOUR BANK ACCOUNT")
        else:
            print("WRONG PIN! Please try again later ........")

    def withdraw(self):
        amt = int(input("Enter the amount to be withdrawn from your bank account : "))

        pin = int(input("Enter your pin : "))
        if (pin == self.pin and (self.balance - amt) > 0 ):
            self.balance -= amt
            print(f"Rs. {amt} WITHDRAWED SUCCESSFULLY FROM YOUR BANK ACCOUNT")
        else:
            if (pin != self.pin):
                print("WRONG PIN! Please try again later ........")
            else:
                print("INSUFFICIENT BALANCE")

    def check_balance(self):
        pin = int(input("Enter your ATM pin :"))
        if (pin == self.pin):
            print(f"Your current balance is : Rs {self.balance}")
        else:
            print("Invalid PIN!")

sbi = ATM()