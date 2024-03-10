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

        # Calling the menu as soon as an instance is created
        self.menu()

    def menu(self):
        user_input = int(input('''
        ------------------------------------------------------------------
                                    WELCOME
                        HOW WOULD YOU LIKE TO PROCEED ?
                        0. ENTER 0 TO SEE YOUR ACCOUNT BALANCE
                        1. ENTER 1 TO CREATE NEW PIN
                        2. ENTER 2 TO CHANGE YOUR EXISTING PIN
                        3. ENTER 3 TO DEPOSIT CASH
                        4. ENTER 4 TO WTIHDRAW CASH
                        5. ENTER 5 TO SEE YOUR CURRENT BALANCE
                        6. ENTER 6 TO EXIT
        ------------------------------------------------------------------
                        ENTER YOUR CHOICE HERE ~ '''))

        match user_input:
            case 0:
                self.displayAccountHolderDetails()
            case 1:
                self.createPin()
            case 2:
                self.updatePin()
            case 3:
                self.deposit()
            case 4:
                self.withdraw()
            case 5:
                self.check_balance()
            case 6:
                print("\t\t\tVISIT US AGAIN. BYE.......")
                exit(0)
            case _:
                print("CHECK YOUR INPUT AND TRY AGAIN .........")

    # A method to display the details of the account holder
    def displayAccountHolderDetails(self):

        try:
            temp = int(input("Verify your pin please : "))

            if (self.__pin == temp):
                print(f'ACCOUNT NUMBER : {self.__accountNumber}')
                print(f'CURRENT BALANCE : {self.__balance}')
            else:
                print("WRONG PIN! CANNOT ACCESS YOUR DETAILS AT THE MOMENT!")

        except Exception as e:
            print(f"Can not process your request at the moment due to the following error ~\n{str(e)}")

    # A method to create ATM PIN for the newly alloted/issued ATM CARDS
    def createPin(self):

        try:
            self.__pin = int(input("Enter your pin here : "))
            print("PIN SET SUCCESSFULLY")
        except Exception as e:
            print(f"Can not create your ATM PIN right now due to the following error ~\n{str(e)}")

    # A method to update the existing ATM PIN
    def updatePin(self):

        try:
            temp_pin = int(input("Enter your current ATM PIN : "))

            if (temp_pin == self.__pin):
                self.__pin = int(input("Enter your new pin : "))
                print("PIN UPDATED SUCCESSFULLY")
            else:
                print("WRONG PIN! Please try again later ........")

        except Exception as e:
            print(f"Can not update your ATM PIN at this moment due to the following error ~\n{str(e)}")

    # A method to help the user deposit money in the bank account
    def deposit(self):

        try:
            amt = int(input("Enter the amount to be deposited in your bank account : "))
            temp_pin = int(input("Enter your ATM PIN : "))

            if (temp_pin == self.__pin):
                self.__balance += amt
                print(f"Rs. {amt} DEPOSITED SUCCESSFULLY IN YOUR BANK ACCOUNT")
            else:
                print("WRONG PIN! Please try again later ........")

        except Exception as e:
            print(f"Can not deposit money in the bank at this moment due to the following error ~\n{str(e)}")

    # A method to help the user in withdrawing money from his bank account
    def withdraw(self):

        try:
            amt = int(input("Enter the amount to be withdrawn from your bank account : "))
            temp_pin = int(input("Enter your pin : "))

            if (temp_pin == self.__pin and (self.__balance - amt) > 0 ):
                self.__balance -= amt
                print(f"Rs. {amt} WITHDRAWED SUCCESSFULLY FROM YOUR BANK ACCOUNT")
            else:
                if (temp_pin != self.__pin):
                    print("WRONG PIN! Please try again later ........")
                else:
                    print("INSUFFICIENT BALANCE")

        except Exception as e:
            print(f"Can not withdraw the money because of the following error ~ \n{str(e)}")

    # A method to check the balance in the bank account
    def check_balance(self):

        try:
            temp_pin = int(input("Enter your ATM pin :"))

            if (temp_pin == self.__pin):
                print(f"Your current balance is : Rs {self.__balance}")
            else:
                print("Invalid PIN!")

        except Exception as e:
            print(f"Can not check the balance due to the following error ~\n{str(e)}")

sbi = ATM()