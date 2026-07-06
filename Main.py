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
        self.max_borrow = 2000


    def show_info(self):
        print("---------------")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Balance:", self.balance)


    def check_pin(self, pin):
        return pin == self.__pin


    def deposit(self, amount):
        self.balance += amount


    def withdraw(self, withdraw_amount):
        if withdraw_amount > self.balance:
            return False
        self.balance -= withdraw_amount
        return True


    def borrow(self, amount):
        if amount <= 0:
            return False

        if self.debt + amount > self.max_borrow:
            return False

        self.balance += amount
        self.debt += amount
        return True


def account_exists(name):
    for acc in accounts:
        if acc.name == name:
            return True
    return False


while True:

    print("\n1. Create Account")
    print("2. Login")
    print("3. Deposit Money")
    print("4. Withdrawal Money")
    print("5. Transfer Money")
    print("6. Borrow Money")
    print("7. Show All Accounts")
    print("8. Exit")

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
        else:
            print("Borrow failed (limit reached or invalid amount)")



    elif choice == "7":
        if len(accounts) == 0:
            print("No accounts created yet.")
        else:
            for acc in accounts:
                acc.show_info()



    elif choice == "8":
        print("Have a good day. Bye!")
        break


    else:
        print("Invalid option. Please try again.")
