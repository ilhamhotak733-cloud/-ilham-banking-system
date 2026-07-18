print("Welcome to Ilham Banking System!")

accounts = []
found_account = None

correct_admin_password = "admin1290"


class BankAccount:
    def __init__(self, name, age, pin, balance):
        self.name = name
        self.age = age
        self.__pin = pin
        self.balance = balance
        self.debt = 0
        self.transaction_history = []
        self.failed_login_attempts = 0
        self.account_locked = False
        self.credit_score = 650
        self.saving_balance = 0






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
            return (False, "Loan amount can not be a NEGATIVE")
        

        if self.credit_score >= 750 and self.credit_score <= 850:
            max_loan = 10000
        

        elif self.credit_score >= 650 and self.credit_score <= 749:
            max_loan = 5000


        elif self.credit_score >= 500 and self.credit_score <= 649:
            max_loan = 2500


        elif self.credit_score >= 300 and self.credit_score <= 499:
            max_loan = 0
            return (False, "Loan was Unsuccessful because Credit Score was to LOW to reach the Minimum Credit Score needed to Loan the Amount")


        
        if amount > max_loan:
            return (False, "Loan was Unsuccessful because it was OVER the Maximum Amount of Loan!")


        

        self.balance += amount
        self.debt += amount

        self.credit_score = self.credit_score - amount//50 
        if self.credit_score < 300:
            self.credit_score = 300

        self.transaction_history.append("Borrowed: " + str(amount))
        return (True, "Loan was SUCCESSFUL and approved!")
    

    def repay(self, amount):
        self.balance -= amount
        self.debt -= amount

        self.credit_score = self.credit_score + amount//50
        if self.credit_score > 850:
            self.credit_score = 850

        self.transaction_history.append("Repaid: " + str(amount))
        return True
 
    


    def show_transactions(self):
        print("---------------")
        print("Transaction History:")

        for transaction in self.transaction_history:
            print(transaction)
    

    def get_pin(self):
        return self.__pin
    

    def update_pin(self, pin):
        self.__pin = pin
        return True
    

    def credit_rating(self):
        if self.credit_score >= 800 and self.credit_score <= 850:
            return "Excellent"
        
        elif self.credit_score >= 740 and self.credit_score <= 499:
            return "Very Good"
        
        elif self.credit_score >= 670 and self.credit_score <= 739:
            return "Good"
        
        elif self.credit_score >= 580 and self.credit_score <= 669:
            return "Fair"
        
        elif self.credit_score >= 300 and self.credit_score <= 579:
            return "Poor"
        
    

    def transfer_to_savings(self, amount):
        if amount > self.balance:
            return False
        self.balance -= amount
        self.saving_balance += amount
        self.transaction_history.append("Transferred to Savings: " + str(amount))
        return True
    


    


    def transfer_to_checkings(self, amount):
        if amount > self.saving_balance:
            return False
        self.saving_balance -= amount
        self.balance += amount
        self.transaction_history.append("Transferred to Checking: " + str(amount))
        return True






    def apply_interest(self, rate):
        interest = self.saving_balance * rate
        self.saving_balance = self.saving_balance + interest
        self.transaction_history.append("Apply interest: " + str(interest))









        







    








def account_exists(name):
    for acc in accounts:
        if acc.name == name:
            return True
    return False


def save_accounts():
    file = open("bank_data.txt", "w")

    for acc in accounts:
        history = "|".join(acc.transaction_history)
        
        line = acc.name + "," + str(acc.age) + "," + acc.get_pin() + "," + str(acc.balance) + "," + str(acc.debt) + "," + str(acc.failed_login_attempts) + "," + str(acc.account_locked) + "," + str(acc.credit_score) + "," + str(acc.saving_balance) + "," + history
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
        failed_login_attempts = int(data[5])
        account_locked = data[6] == "True"
        credit_score = int(data[7])
        saving_balance = float(data[8])
        transaction_history = data[9].split("|")

        account = BankAccount(name, age, pin, balance)
        account.debt = debt
        account.failed_login_attempts = failed_login_attempts
        account.account_locked = account_locked
        account.credit_score = credit_score
        account.saving_balance = saving_balance
        account.transaction_history = transaction_history

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
    print("9. Change PIN")
    print("10. Admin Log In")
    print("11. Check Current Credit Score")
    print("12. View Current Savings Balance")
    print("13. View Current Checkings Balance")
    print("14. Transfer to Savings")
    print("15. Transfer to Checking")
    print("16. Show All Accounts")
    print("17. Exit")


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
                    found_account = acc
                    break
        else:
            print("Account not found!")
            continue
        if found_account.account_locked:
                print("Account already locked")
                continue
        elif found_account.check_pin(pin):
            found_account.failed_login_attempts = 0
            print("Log in successful")
        else:
            print("Invalid PIN!")

            found_account.failed_login_attempts += 1
            tries_left = 3 - found_account.failed_login_attempts
            print("You got", tries_left, "Tries Left!")

            if found_account.failed_login_attempts == 3:
                found_account.account_locked = True
                save_accounts()
                print("To many tries account has been locked!")











    elif choice == "3":
        if found_account is None:
            print("Please log in first.")
            continue

        if found_account.account_locked:
                print("Account is locked!")
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


        if found_account.account_locked:
                print("Account is locked!")
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

        if found_account.account_locked:
                print("Account is locked!")
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

        if found_account.account_locked:
                print("Account is locked!")
                continue

        borrow_amount = int(input("Pls enter the amount you would like to borrow:"))

        if borrow_amount <= 0:
            print("Borrow amount cannot be negative!")
            continue

        success, message = found_account.borrow(borrow_amount)

        if success:
            print(message)
            print("New balance:", found_account.balance)
            print("New debt:", found_account.debt)
            save_accounts()
        else:
            print(message)











    elif choice == "7":
        if found_account is None:
            print("Please log in first")
            continue

        if found_account.account_locked:
                print("Account is locked!")
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

        if found_account.account_locked:
                print("Account is locked!")
                continue
        
        if len(found_account.transaction_history) == 0:
            print("You have no transactions yet!")
        else:
            found_account.show_transactions()








    
    elif choice == "9":
        if found_account is None:
            print("Pls log in first!")
            continue

        if found_account.account_locked:
                print("Account is locked!")
                continue

        current_pin = input("Pls enter your current pin to change your pin: ")

        found_account.check_pin(current_pin)

        if not found_account.check_pin(current_pin):
            print("Wrong pin pls retry!")
            continue

        new_pin = input("Pls enter your new pin: ")

        if len(new_pin) != 4:
            print("Pin must be exactly 4 digits!")
            continue

        if not new_pin.isdigit():
            print("PIN must contain only numbers!")
            continue

        success = found_account.update_pin(new_pin)
        save_accounts()
        
        if success:
            print("PIN updated successfully!")
        else:
            print("PIN was not updated!")










    elif choice == "10":
        if found_account.account_locked:
                print("Account is locked!")
                continue
        
        admin_password = input("Pls enter the admin password: ")

        if admin_password != correct_admin_password:
            print("Wrong admin password pls retry!")
            continue


        while True:


            print("\n1. Show All Accounts")
            print("2. Search Account")
            print("3. Delete Account")
            print("4. Total Bank Balance")
            print("5. Total Bank Debt")
            print("6. Unlock Account")
            print("7. Exit Admin Panel")

            admin_choice = input("Pls Choose an option Admin: ")


            if admin_choice == "1":
                if len(accounts) == 0:
                    print("No accounts created yet.")
                else:
                    for acc in accounts:
                        acc.show_info()
            
            



            elif admin_choice == "2":
                found_account = None
                for acc in accounts:
                    if acc.name == name:
                        acc.show_info()
                        found_account = acc
                if found_account == None:
                    print("No accounts were found Admin")




            

            elif admin_choice == "3":
                found_account = None
                
                delete_account = input("Pls enter the Account name to Delete!")

                for acc in accounts:
                    if acc.name == delete_account:
                        found_account = acc
                        break

                if found_account is None:
                    print("Account Not Found!")
                    continue

                accounts.remove(found_account)
                print("Account successfully deleted Admin!")
                save_accounts()
            







            elif admin_choice == "4":
                total_balance = 0

                for acc in accounts:
                    total_balance += acc.balance
                print("The Total Bank Balance is:", total_balance, "Admin")




            
            elif admin_choice == "5":
                total_debt = 0
                for acc in accounts:
                    total_debt += acc.debt
                print("The Total Bank Debt is:", total_debt, "Admin")




            elif admin_choice == "6":

                found_account = None

                unlock_account = input("Pls enter the name of the account you would like to unlock Admin: ")


                for acc in accounts:
                    if acc.name == unlock_account:
                        found_account = acc
                        break

                if not found_account:
                        print("No account were found. Admin!")
                        continue
                            
                confirm_unlock = input("Are you SURE admin you want to UNLOCK this account (yes/no)").lower()
                if confirm_unlock == "yes":
                    found_account.account_locked = False
                    found_account.failed_login_attempts = 0 
                    save_accounts()
                    print("Account was successfully unlocked!. Admin!")
                    print("Thank you admin for confirming!")
                elif confirm_unlock == "no":
                    print("Okey admin have a good day!.")
                    print("Thank you admin for confirming!")



            


            elif admin_choice == "7":
                print("Good Bye Admin See You Later!")
                break
            else:
                print("Invalid choice. Admin Pls Retry!")







    

    elif choice == "11":
        if found_account is None:
            print("Pls login first!")
            continue

        if found_account.account_locked:
                print("Account is locked!")
                continue
        

        print(name,"'s", "Current Credit Score is:", found_account.credit_score)
        print("Your Credit Rating is:", found_account.credit_rating())








    

    elif choice == "12":
        if found_account is None:
            print("Pls login first!")
            continue

        if found_account.account_locked:
                print("Account is locked!")
                continue
        
        found_account.apply_interest(0.05)
        save_accounts()
        print(name, "s", "Current Saving Balance Is: ", found_account.saving_balance)




    
    elif choice == "13":
        if found_account is None:
            print("Pls login first!")
            continue

        if found_account.account_locked:
            print("Account is locked!")
            continue

        print(name, "s", "Current Checking Balance Is: ", found_account.balance)











    elif choice == "14":
        if found_account is None:
            print("Pls login first!")
            continue


        if found_account.account_locked:
                print("Account is locked!")
                continue


        transfer_amount_to_savings = int(input("Pls enter the amount you would like to transfer to your savings acccount: "))


        success = found_account.transfer_to_savings(transfer_amount_to_savings)

        if success:
            print("Transferring the amount to your savings account was a success!")
            print("Your New Saving Balance Is: ", found_account.saving_balance)
            print("Your New Checking Balance Is: ", found_account.balance)
            save_accounts()

        else:
            print("Transferring money to savings account was failed!")
    









    elif choice == "15":
        if found_account is None:
            print("Pls login first!")
            continue


        if found_account.account_locked:
                print("Account is locked!")
                continue




        transfer_amount_to_checkings = int(input("Pls enter the amount you would like to transfer to your checkings account: "))



        success = found_account.transfer_to_checkings(transfer_amount_to_checkings)


        if success:
            print("Transferring the amount to your checkings account was a success!")
            print("Your New Checking Balance Is: ", found_account.balance)
            print("Your New Savings Balance Is: ", found_account.saving_balance)
            save_accounts()


        else:
            print("Transferring money to checkings account was failed!")



        









    elif choice == "16":

        if found_account.account_locked:
                print("Account is locked!")
                continue
        

        if len(accounts) == 0:
            print("No accounts created yet.")
        else:
            for acc in accounts:
                acc.show_info()









    elif choice == "17":
        print("Have a good day. Bye!")
        break


    else:
        print("Invalid option. Please try again.")
        
