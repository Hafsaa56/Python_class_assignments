class ATM :

    def __init__(self):
        self.pin =1234
        self.balance = 1000
        self.is_authenticated = False

    def check_pin(self ,input_pin):
        if input_pin ==1234:
            print("Correct")
        else:
            print("Incorrect!, Please Try Again!")

    def check_balance(self):
        if self.is_authenticated:
            print(f"Current Balance: Rs. {self.balance} .0")
        else:
            ("Please enter the correct pin! ")

    def deposit(self, amount):
        if self.is_authenticated:
            if amount > 0:
             print(f"Rs. {amount} deposit successfully!" )
            else:
                print("Deposit amount must be positive.")
        else:
            print("Please inter the correct pin first! ")


    def withdraw (self , amount ):
        if self.is_authenticated:
            if amount <= 0:
                print("Withdrawal amount must be positive!")
            elif amount > self.balance :
                print("Insufficient Balance. ")
            else:
                self.balance -= amount
                print("Rs. " , {amount}, "Successfully withdraw. ")
        else:
                print("Please enter the correct pin first! ")


    def exit(self):
        print("Thank You! For Using the ATM. GOOD BEY!")

    def manu(self):
        ("-----WELLCOME TOTHE ATM-----")
        attemps = 0
        while attemps < 3:
            input_Pin = input("First enter your 4-digit PIN: ")
            if input_Pin == self.pin:
                self.is_authenticated = True 
                print("Successfully Varified your PIN! ")
                break
            else:
                attemps += 1
                print(f"Incorrect PIN!  {3 - attemps}")
        else:
            print(f"To many incorrect attempts. Exiting.")
            return
        while True:
             print("---- ATM MANU ----")
             print("1. check_balance ")
             print("2. deposit")
             print("3. withdraw")
             print("4. exit")
             choice = input("Please select an option (1- 4): ")
             
             if choice == "1":
                 self.check_balance()
             elif choice == "2":
                try:
                    amount = float(input("Enter amount to deposit: "))
                    self.deposit
                except ValueError:
                     print("Invalid. Please enter numeric value: ")
             elif choice == "3":
                 try:
                     amount = float(input("Enter amount to withdraw: "))
                     self.withdraw(amount)
                 except ValueError:
                     print("Invalid. Pleaseenter a numeric value.  ")
             elif choice == "4":
                 if not self.exit():
                     break
                 else:
                    print("Invalid selection. Please choose a valid option. ")

if __name__ == '__main__':
    atm = ATM()
    atm.manu()
                     

                 
                 







