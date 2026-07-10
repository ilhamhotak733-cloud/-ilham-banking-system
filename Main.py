print("Welcome to Ilham Banking System!")

accounts = []
found_account = None


class BankAccount:
    def __init__(self, name, age, pin, balance):
        self.name = name
        self.age = age
        self.__pin = pin
        self.balance = balance
        self.debt = 0
        self.max_borrow = 10000
        self.transaction_history = []



    def show_info(self):
        print("---------------")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Balance:", self.balance)



    def check_pin(self, pin):
        return pin == self.__pin



    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append("Deposited: " + str(amount))



    def withdraw(self, amount):
        if amount > self.balance:
            return False
        self.balance -= amount
        self.transaction_history.append("Withdrawn: " + str(amount))
        return True



    def borrow(self, amount):
        if amount <= 0:
            return False

        if self.debt + amount > self.max_borrow:
            return False

        self.balance += amount
        self.debt += amount
        self.transaction_history.append("Borrowed: " + str(amount))
        return True
    

    def repay(self, amount):
        self.balance -= amount
        self.debt -= amount
        self.transaction_history.append("Repaid: " + str(amount))
        return True
    def show_transactions(self):
        print("---------------")
        print("Transaction History:")

        for transaction in self.transaction_history:
            print(transaction)
    

    def get_pin(self):
        return self.__pin
    
    



def account_exists(name):
    for acc in accounts:
        if acc.name == name:
            return True
    return False


def save_accounts():
    file = open("bank_data.txt", "w")

    for acc in accounts:
        line = acc.name + "," + str(acc.age) + "," + acc.get_pin() + "," + str(acc.balance) + "," + str(acc.debt)
        file.write(line + "\n")

    file.close()


def load_accounts():
    file = open("bank_data.txt", "r")

    for line in file:
        if line.strip() == "":
            continue

        data = line.strip().split(",")

        name = data[0]
        age = int(data[1])
        pin = data[2]
        balance = int(data[3])
        debt = int(data[4])

        account = BankAccount(name, age, pin, balance)
        account.debt = debt

        accounts.append(account)

    file.close()







load_accounts()

while True:

    print("\n1. Create Account")
    print("2. Login")
    print("3. Deposit Money")
    print("4. Withdrawal Money")
    print("5. Transfer Money")
    print("6. Borrow Money")
    print("7. Repay Debt")
    print("8. Show Transaction History")
    print("9. Show All Accounts")
    print("10. Exit")


    choice = input("Choose an option: ")





    if choice == "1":
        name = input("Enter name to create account: ")

        if account_exists(name):
            print("Account already exists!")
            continue

        age = int(input("Enter age to create account: "))

        if age < 18:
            print("You must be 18 or older!")
            continue

        pin = input("Please enter a PIN: ")
        balance = int(input("Please enter starting balance: "))

        if balance < 0:
            print("Balance cannot be negative!")
            continue

        account = BankAccount(name, age, pin, balance)
        accounts.append(account)
        save_accounts()

        print("Account successfully created!")








    elif choice == "2":
        name = input("Please enter your name: ")
        pin = input("Please enter your PIN: ")

        found_account = None

        for acc in accounts:
            if name == acc.name:
                if acc.check_pin(pin):
                    found_account = acc
                    print("Login successful!")
                else:
                    print("Invalid PIN!")
                break
        else:
            print("Account not found!")









    elif choice == "3":
        if found_account is None:
            print("Please log in first.")
            continue

        deposit = int(input("Please enter deposit amount: "))

        if deposit < 0:
            print("Deposit amount cannot be negative!")
            continue

        found_account.deposit(deposit)

        print("Deposit was successful!")
        print("New balance:", found_account.balance)
        save_accounts()








    elif choice == "4":
        if found_account is None:
            print("Please log in first.")
            continue

        withdraw_amount = int(input("Please enter the amount you would like to withdraw: "))

        if withdraw_amount < 0:
            print("Withdrawal amount cannot be negative!")
            continue

        success = found_account.withdraw(withdraw_amount)

        if success:
            print("Withdrawal successful!")
            print("New balance:", found_account.balance)
            save_accounts()
        else:
            print("Insufficient funds!")








    elif choice == "5":
        if found_account is None:
            print("Please log in first.")
            continue

        transfer_amount = int(input("Please enter the amount you would like to transfer: "))

        if transfer_amount < 0:
            print("Transfer amount cannot be negative!")
            continue

        recipient_name = input("Please enter the recipient's name: ")

        recipient_account = None

        for acc in accounts:
            if acc.name == recipient_name:
                recipient_account = acc
                break

        if recipient_account is None:
            print("Recipient account not found!")
            continue

        if recipient_account == found_account:
            print("You cannot transfer money to yourself!")
            continue

        if found_account.withdraw(transfer_amount):
            recipient_account.deposit(transfer_amount)
            print("Transfer successful!")
            print("Your new balance:", found_account.balance)
            found_account.transaction_history.append("Transferred: " + str(transfer_amount))
            recipient_account.transaction_history.append("Received: " + str(transfer_amount))
            save_accounts()
        else:
            print("Insufficient funds for transfer!")









    elif choice == "6":
        if found_account is None:
            print("Please log in first")
            continue

        borrow_amount = int(input("Pls enter the amount you would like to borrow:"))

        if borrow_amount <= 0:
            print("Borrow amount cannot be negative!")
            continue

        success = found_account.borrow(borrow_amount)

        if success:
            print("Borrow successful!")
            print("New balance:", found_account.balance)
            print("New debt:", found_account.debt)
            save_accounts()
        else:
            print("Borrow failed (limit reached or invalid amount)")








    elif choice == "7":
        if found_account is None:
            print("Please log in first")
            continue

        if found_account.debt == 0:
            print("You have no Debt to Repay")
            continue

        repay_amount = int(input("Pls enter the amount you would like to repay debt:"))

        if repay_amount <= 0:
            print("Repay amount cannot be a negative!")
            continue

        if repay_amount > found_account.balance:
            print("You cannot Repay more then the current balance")
            continue

        if repay_amount > found_account.debt:
            print("You cannot repay more then the remaining debt!")
            continue

        success = found_account.repay(repay_amount)

        if success:
            print("Repay successful")
            print("New Balance:", found_account.balance)
            print("New Debt:", found_account.debt)
            save_accounts()
        else:
            print("Repayment failed")
    




    elif choice == "8":
        if found_account is None:
            print("Pls log in first")
            continue
        if len(found_account.transaction_history) == 0:
            print("You have no transactions yet!")
        else:
            found_account.show_transactions()














    elif choice == "9":
        if len(accounts) == 0:
            print("No accounts created yet.")
        else:
            for acc in accounts:
                acc.show_info()






    elif choice == "10":
        print("Have a good day. Bye!")
        break


    else:
        print("Invalid option. Please try again.")
