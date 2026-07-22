print("Welcome to Ilham Banking System!")

import datetime

import random


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
        self.card_number = 0
        self.cvv = 0
        self.expiration_month = 0
        self.expiration_year = 0
        self.debit_card()
        self.monthly_budget = 0
        self.money_spent_this_month = 0

        












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
        
        max_loan = self.get_max_loan()

        if max_loan == 0:
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


    








    def get_max_loan(self):
        if self.credit_score >= 750 and self.credit_score <= 850:
            max_loan = 10000
        

        elif self.credit_score >= 650 and self.credit_score <= 749:
            max_loan = 5000


        elif self.credit_score >= 500 and self.credit_score <= 649:
            max_loan = 2500


        elif self.credit_score >= 300 and self.credit_score <= 499:
            max_loan = 0

        return max_loan 
    








    def debit_card(self):
        lowest_16_digits = 1000000000000000
        largest_16_digits = 9999999999999999
        random.randint(lowest_16_digits, largest_16_digits)
        self.card_number = random.randint(lowest_16_digits, largest_16_digits)


        lowest_cvv_3_digits = 100
        largest_cvv_3_digits = 999
        random.randint(lowest_cvv_3_digits, largest_cvv_3_digits)
        self.cvv = random.randint(lowest_cvv_3_digits, largest_cvv_3_digits)


        lowest_month = 1
        largest_month = 12
        random.randint(lowest_month, largest_month)
        self.expiration_month = random.randint(lowest_month, largest_month)


        lowest_future_year = 2029
        largest_future_year = 2033
        random.randint(lowest_future_year, largest_future_year)
        self.expiration_year = random.randint(lowest_future_year, largest_future_year)
        













def account_exists(name):
    for acc in accounts:
        if acc.name == name:
            return True
    return False








def save_accounts():
    file = open("bank_data.txt", "w")

    for acc in accounts:
        history = "|".join(acc.transaction_history)
        
        line = acc.name + "," + str(acc.age) + "," + acc.get_pin() + "," + str(acc.balance) + "," + str(acc.debt) + "," + str(acc.failed_login_attempts) + "," + str(acc.account_locked) + "," + str(acc.credit_score) + "," + str(acc.saving_balance) + "," + str(acc.card_number) + "," + str(acc.cvv) + "," + str(acc.expiration_month) + "," + str(acc.expiration_year) + "," + str(acc.monthly_budget) + "," + str(acc.money_spent_this_month) + "," + history 
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
        card_number = int(data[9])
        cvv = int(data[10])
        expiration_month = int(data[11])
        expiration_year = int(data[12])
        monthly_budget = int(data[13])
        money_spent_this_month = int(data[14])
        transaction_history = data[15].split("|")

        account = BankAccount(name, age, pin, balance)
        account.debt = debt
        account.failed_login_attempts = failed_login_attempts
        account.account_locked = account_locked
        account.credit_score = credit_score
        account.saving_balance = saving_balance
        account.card_number = card_number
        account.cvv = cvv
        account.expiration_month = expiration_month
        account.expiration_year = expiration_year
        account.monthly_budget = monthly_budget
        account.money_spent_this_month = money_spent_this_month
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
    print("16. Bank Statement")
    print("17. ATM")
    print("18. Replace Lost Card")
    print("19. View Debit Card Details")
    print("20. Set Monthly Budget")
    print("21. View Remaining Budget")
    print("22. Reset Monthly Budget")
    print("23. Pay Bills")
    print("24. Show All Accounts")
    print("25. Exit")


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
            found_account.money_spent_this_month += withdraw_amount
            budget_percentage_used = (found_account.money_spent_this_month/found_account.monthly_budget) * 100
            if found_account.money_spent_this_month > found_account.monthly_budget:
                print("MAX BUDGET EXCEEDED!")

            elif found_account.money_spent_this_month >= (found_account.monthly_budget * 0.95):
                print("WARNING ALMOST EXCEEDED!")
                print("you have USED", str(int(budget_percentage_used)) + "% of your BUDGET")
                month_remaining_budget = found_account.monthly_budget - found_account.money_spent_this_month 
                print("Your REMAINING Budget is: ", month_remaining_budget)

            elif found_account.money_spent_this_month >= (found_account.monthly_budget * 0.80):
                print("WARNING!!")
                print("You have used 80% of your monthly budget")
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
            found_account.money_spent_this_month += transfer_amount
            budget_percentage_used = (found_account.money_spent_this_month/found_account.monthly_budget) * 100

            if found_account.money_spent_this_month > found_account.monthly_budget:
                print("MAX BUDGET EXCEEDED!")

            elif found_account.money_spent_this_month >= (found_account.monthly_budget * 0.95):
                print("WARNING ALMOST EXCEEDED!")
                print("you have USED", str(int(budget_percentage_used)) + "% of your BUDGET")
                month_remaining_budget = found_account.monthly_budget - found_account.money_spent_this_month 
                print("Your REMAINING Budget is: ", month_remaining_budget)

            elif found_account.money_spent_this_month >= (found_account.monthly_budget * 0.80):
                print("WARNING!!")
                print("You have used 80% of your monthly budget")
                
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
        
        print(acc.name, "s", "Current Saving Balance Is: ", found_account.saving_balance)










    
    elif choice == "13":
        if found_account is None:
            print("Pls login first!")
            continue

        if found_account.account_locked:
            print("Account is locked!")
            continue

        print(acc.name, "s", "Current Checking Balance Is: ", found_account.balance)













    elif choice == "14":
        if found_account is None:
            print("Pls login first!")
            continue


        if found_account.account_locked:
                print("Account is locked!")
                continue


        transfer_amount_to_savings = int(input("Pls enter the amount you would like to transfer to your savings acccount: "))


        success = found_account.transfer_to_savings(transfer_amount_to_savings)
        found_account.apply_interest(0.05)

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
        if found_account is None:
            print("Pls login first!")
            continue


        if found_account.account_locked:
            print("Account is locked!")
            continue

        date_time = datetime.date.today()
        current_datetime = datetime.datetime.now()
        current_time = current_datetime.strftime("%I:%M:%S %p")

        print("---------------------------------------------")
        print("---------------------------------------------")
        print("               ILHAM BANK                    ")
        print("---------------------------------------------")
        print("---------------------------------------------")

        print("Account Holder: ", found_account.name.upper())
        print("---------------------------------------------")
        print("Current Date: ", datetime.date.today())
        print("---------------------------------------------")
        print("Current Time: ", current_datetime.strftime("%I:%M:%S %p"))
        print("---------------------------------------------")
        

        print("Your Checking Balance is: ", found_account.balance)

        print("---------------")

        print("Your Saving balance is: ", found_account.saving_balance)

        print("---------------")

        print("Your Current Debt is: ", found_account.debt)

        print("---------------")

        print("Your Current Credit Score is: ", found_account.credit_score)

        print("---------------")

        print("Your Max Loan is: ", found_account.get_max_loan())



        print("---------------------------------------------")
        print("---------------------------------------------")
        print("              TRANSACTION HISTORY            ")
        print("---------------------------------------------")
        print("---------------------------------------------")

        print("---------------")
        if len(found_account.transaction_history) == 0:
            print("You have no transactions yet!")
        else:
            found_account.show_transactions()
        print("---------------")


        print("---------------------------------------------")
        print("---------------------------------------------")
        print("                    SUMMARY                  ")
        print("---------------------------------------------")
        print("---------------------------------------------")


        print("---------------")
        print("Your total number of transactions is: ", len(found_account.transaction_history))
        print("---------------")

        status = found_account.account_locked
        if found_account.account_locked is True:
            status = found_account.account_locked
            status = "Locked"
        else:
            status = "Unlocked"
        

        print("---------------")
        print("Your Account Status is: ", status)
        print("---------------")

        print("---------------------------------------------")
        print("---------------------------------------------")
        print("           BANK STATEMENT COMPLETE!          ")
        print("---------------------------------------------")
        print("---------------------------------------------")










    
    elif choice == "17":
        card_number = int(input("Pls enter your card number: "))
        for acc in accounts:
            if card_number == acc.card_number:
                    found_account = acc
                    break
        else:
            print("Card number was not found pls retry!")
            continue

        cvv_number = int(input("Pls enter the your cvv number: "))
        if cvv_number == found_account.cvv:
            found_account.failed_login_attempts = 0

        
        else:
            print("Cvv number was not found pls retry!")
            found_account.failed_login_attempts += 1
            tries_left = 3 - found_account.failed_login_attempts
            print("You got", tries_left, "Tries Left!")
            if found_account.failed_login_attempts == 3:
                found_account.account_locked = True
                save_accounts()
                print("To many tries account has been locked!")
            continue

        
        pin_number = (input("Pls enter your pin: "))
        if found_account.check_pin(pin_number):
            found_account.failed_login_attempts = 0
            print("ATM login was succcessfull")



            while True:



                print("\n1. Check Balance")
                print("2. Withdraw Cash")
                print("3. Deposit Cash")
                print("4. Transfer Money")
                print("5. View Savings Balance")
                print("6. Exit ATM")


                atm_choice = input("Pls choose an option: ")





                if atm_choice == "1": 
                    print("Your Check balance is: ", found_account.balance)









                elif atm_choice == "2":
                    withdraw_cash = int(input("Please enter the amount of Cash you would like to Withdraw: "))

                    if withdraw_cash < 0:
                        print("Withdrawal amount of Cash cannot be Negative!")
                        continue

                    success = found_account.withdraw(withdraw_cash)

                    if success:
                        print("Withdrawal successful!")
                        print("Pls take your cash: ",withdraw_cash)
                        print("New balance:", found_account.balance)
                        found_account.money_spent_this_month += withdraw_cash
                        budget_percentage_used = (found_account.money_spent_this_month/found_account.monthly_budget) * 100

                        if found_account.money_spent_this_month > found_account.monthly_budget:
                            print("MAX BUDGET EXCEEDED!")

                        elif found_account.money_spent_this_month >= (found_account.monthly_budget * 0.95):
                            print("WARNING ALMOST EXCEEDED!")
                            print("you have USED", str(int(budget_percentage_used)) + "% of your BUDGET")

                            month_remaining_budget = found_account.monthly_budget - found_account.money_spent_this_month 
                            print("Your REMAINING Budget is: ", month_remaining_budget)

                        elif found_account.money_spent_this_month >= (found_account.monthly_budget * 0.80):
                            print("WARNING!!")
                            print("You have used 80% of your monthly budget")
                        save_accounts()
                    else:
                        print("Insufficient funds!")
                








                elif atm_choice == "3":
                    deposit_cash = int(input("Pls enter the amount of Cash you would like to Deposit: "))

                    if deposit_cash <= 0:
                        print("Deposit amount of Cash cannot be a Negative")
                        continue

                    found_account.deposit(deposit_cash)

                    print("Deposit amount of Cash was successfully!")
                    print("New Balance: ", found_account.balance)
                    save_accounts()

                








                elif atm_choice == "4":
                    transfer_cash = int(input("Please enter the amount you would like to transfer: "))

                    if transfer_cash < 0:
                        print("Transfer amount cannot be negative!")
                        continue

                    recipient_name_transfer = input("Please enter the recipient's name: ")

                    recipient_transfer_account = None

                    for acc in accounts:
                        if acc.name == recipient_name_transfer:
                            recipient_transfer_account = acc
                            break

                    if recipient_transfer_account is None:
                        print("Recipient account not found!")
                        continue

                    if recipient_transfer_account == found_account:
                        print("You cannot transfer money to yourself!")
                        continue

                    if found_account.withdraw(transfer_cash):
                            recipient_transfer_account.deposit(transfer_cash)
                            print("Transfer successful!")
                            print("Your new balance:", found_account.balance)
                            found_account.money_spent_this_month += transfer_cash
                            budget_percentage_used = (found_account.money_spent_this_month/found_account.monthly_budget) * 100

                            if found_account.money_spent_this_month > found_account.monthly_budget:
                                print("MAX BUDGET EXCEEDED!")

                            elif found_account.money_spent_this_month >= (found_account.monthly_budget * 0.95):
                                print("WARNING ALMOST EXCEEDED!")
                                print("you have USED", str(int(budget_percentage_used)) + "% of your BUDGET")

                                month_remaining_budget = found_account.monthly_budget - found_account.money_spent_this_month 
                                print("Your REMAINING Budget is: ", month_remaining_budget)

                            elif found_account.money_spent_this_month >= (found_account.monthly_budget * 0.80):
                                print("WARNING!!")
                                print("You have used 80% of your monthly budget")
                            found_account.transaction_history.append("Transferred: " + str(transfer_cash))
                            recipient_transfer_account.transaction_history.append("Received: " + str(transfer_cash))
                            save_accounts()
                    else:
                        print("Insufficient funds for transfer!")








                
                elif atm_choice == "5":
                    print(acc.name, "s", "Current Saving Balance Is: ", found_account.saving_balance)

                

                elif atm_choice == "6":
                    print("Good bye")
                    break
                else:
                    print("Invalid choice")



        else:
            print("Pin number was not found pls retry!")


            found_account.failed_login_attempts += 1
            tries_left = 3 - found_account.failed_login_attempts
            print("You got", tries_left, "Tries Left!")

            if found_account.failed_login_attempts == 3:
                found_account.account_locked = True
                save_accounts()
                print("To many tries account has been locked!")



    



    elif choice == "18":
        if found_account is None:
            print("Pls login first!")
            continue



        if found_account.account_locked:
                print("Account is locked!")
                continue
        
        
        
        check_current_pin = input("Pls enter your current pin: ")


        if found_account.check_pin(check_current_pin):
            found_account.failed_login_attempts = 0

        
            found_account.debit_card()
            found_account.transaction_history.append("Debit card replaced")
            save_accounts()
            print("Debit Card replacements was successfully!")
            print("Your new debit card Information is: ", found_account.card_number, found_account.cvv, found_account.expiration_month, found_account.expiration_year)
            print("------------------------------")

        else:
            print("Pin number was not found pls retry!")
            found_account.failed_login_attempts += 1
            tries_left = 3 - found_account.failed_login_attempts
            print("You got", tries_left, "Tries Left!")
            if found_account.failed_login_attempts == 3:
                found_account.account_locked = True
                save_accounts()
                print("To many tries account has been locked!")












    elif choice == "19":
        if found_account is None:
            print("Pls login first!")
            continue



        if found_account.account_locked:
                print("Account is locked!")
                continue

        verify_current_pin = input("Pls enter your current pin: ")

        if found_account.check_pin(verify_current_pin):
            found_account.failed_login_attempts = 0
            save_accounts()
            print("------------------")
            print("Your debit card Number is: ", found_account.card_number)
            print("----------------- ")
            print("Your Debit Card Cvv Number is: ", found_account.cvv)
            print("----------------- ")
            print("Your Debit Card Expiration month is: ", found_account.expiration_month)
            print("----------------- ")
            print("Your Debit Card expiration Year is: ", found_account.expiration_year)
            print("----------------- ")


        else:
            print("Pin number was not found pls retry!")
            found_account.failed_login_attempts += 1
            tries_left = 3 - found_account.failed_login_attempts
            print("You got", tries_left, "Tries Left!")
            if found_account.failed_login_attempts == 3:
                found_account.account_locked = True
                save_accounts()
                print("To many tries account has been locked!")




    


    elif choice == "20":
        if found_account is None:
            print("Pls Login first!")
            continue

        if found_account.account_locked:
            print("Account Locked!")
            continue


        monthly_budget_money = int(input("Pls enter your Monthly Budget: "))

        found_account.monthly_budget = monthly_budget_money 
        save_accounts()
        found_account.transaction_history.append("Monthly Budget is: " +  str(monthly_budget_money))
        print("Congrats Your Monthly Budget is: ", found_account.monthly_budget)









    elif choice == "21":
        if found_account is None:
            print("Pls Login first!")
            continue


        if found_account.account_locked:
            print("Account Locked!")
            continue


        remaining_budget = found_account.monthly_budget - found_account.money_spent_this_month
        print("Your Monthly Budget is: ", found_account.monthly_budget)
        print("You Spent: ", found_account.money_spent_this_month)
        print("Your Remaining Budget is: ", remaining_budget)




    

    elif choice == "22":
        if found_account is None:
            print("Pls Login in first!")
            continue

        if found_account.account_locked:
            print("Account is Locked!")
            continue

        confirm_reset = input("Are YOU SURE you want to RESET YOUR MONTHLY SPENT BUDGET? (YES/NO)").upper()
        if confirm_reset == "YES":
            found_account.money_spent_this_month = 0
            found_account.transaction_history.append("Monthly spent budget Reset!")
            save_accounts()
            print("Monthly Spent Budget Successfully Reseted!")
        
        elif confirm_reset == "NO":
            print("Thank you for confirming your monthly spent budget Has NOT been reseted!")
        

        else:
            print("INVALID Choice pls enter either YES or NO!")









    elif choice == "23":
        if found_account is None:
            print("Pls login first!")
            continue

        if found_account.account_locked:
            print("Account is Locked")
            continue



        while True:
        
        
        
                        print("\n1. Pay Electricity Bill")
                        print("2. Pay Water Bill")
                        print("3. Pay Internet Bill")
                        print("4. Pay Phone Bill")
                        print("5. Pay Gas Bill")
                        print("6. Back")


                        bill_choice = input("Pls enter the Bill You would like to Pay: ")


                        if bill_choice == "1":
                            pay_electricity = int(input("Pls enter the amount you would like to pay your Electricity bill: "))

                            if pay_electricity <= 0:
                                print("Bill cannot be a negative or equal to Zero!")
                                continue


                            if found_account.balance < pay_electricity:
                                print("Insufficient Funds")
                                continue

                            found_account.balance -= pay_electricity
                            found_account.money_spent_this_month += pay_electricity
                            budget_percentage_used = (found_account.money_spent_this_month/found_account.monthly_budget) * 100
                            
                            if found_account.money_spent_this_month > found_account.monthly_budget:
                                print("MAX BUDGET EXCEEDED!")
                            
                            elif found_account.money_spent_this_month >= (found_account.monthly_budget * 0.95):
                                print("WARNING ALMOST EXCEEDED!")
                                print("you have USED", str(int(budget_percentage_used)) + "% of your BUDGET")
                            
                                month_remaining_budget = found_account.monthly_budget - found_account.money_spent_this_month 
                                print("Your REMAINING Budget is: ", month_remaining_budget)
                            
                            elif found_account.money_spent_this_month >= (found_account.monthly_budget * 0.80):
                                print("WARNING!!")
                                print("You have used 80% of your monthly budget")
                            found_account.transaction_history.append("Paid Electricty Bill: " + str(pay_electricity))
                            save_accounts()
                            print("Paid Electricty Bill Successfully")




                        elif bill_choice == "2":
                            pay_water = int(input("Pls enter the amount you would like to pay your Water Bill: "))

                            if pay_water <= 0:
                                print("Bill cannot be a negative or equal to Zero!")
                                continue

                            if found_account.balance < pay_water:
                                print("Insufficient Funds")
                                continue


                            found_account.balance -= pay_water
                            found_account.money_spent_this_month += pay_water
                            budget_percentage_used = (found_account.money_spent_this_month/found_account.monthly_budget) * 100
                            
                            if found_account.money_spent_this_month > found_account.monthly_budget:
                                print("MAX BUDGET EXCEEDED!")
                            
                            elif found_account.money_spent_this_month >= (found_account.monthly_budget * 0.95):
                                print("WARNING ALMOST EXCEEDED!")
                                print("you have USED", str(int(budget_percentage_used)) + "% of your BUDGET")
                            
                                month_remaining_budget = found_account.monthly_budget - found_account.money_spent_this_month 
                                print("Your REMAINING Budget is: ", month_remaining_budget)
                            
                            elif found_account.money_spent_this_month >= (found_account.monthly_budget * 0.80):
                                print("WARNING!!")
                                print("You have used 80% of your monthly budget")
                            found_account.transaction_history.append("Paid Water Bill: " + str(pay_water))
                            save_accounts()
                            print("Paid Water Bill Successfully!")



                        elif bill_choice == "3":
                            pay_interent = int(input("Pls enter the amount you would like to pay your Interent Bill: "))


                            if pay_interent <= 0:
                                print("Bill cannot be a negative or equal to Zero!")
                                continue

                            if found_account.balance < pay_interent:
                                print("Insufficient Funds")
                                continue


                            found_account.balance -= pay_interent
                            found_account.money_spent_this_month += pay_interent
                            budget_percentage_used = (found_account.money_spent_this_month/found_account.monthly_budget) * 100
                            
                            if found_account.money_spent_this_month > found_account.monthly_budget:
                                print("MAX BUDGET EXCEEDED!")
                            
                            elif found_account.money_spent_this_month >= (found_account.monthly_budget * 0.95):
                                print("WARNING ALMOST EXCEEDED!")
                                print("you have USED", str(int(budget_percentage_used)) + "% of your BUDGET")
                            
                                month_remaining_budget = found_account.monthly_budget - found_account.money_spent_this_month 
                                print("Your REMAINING Budget is: ", month_remaining_budget)
                            
                            elif found_account.money_spent_this_month >= (found_account.monthly_budget * 0.80):
                                print("WARNING!!")
                                print("You have used 80% of your monthly budget")
                            found_account.transaction_history.append("Paid Interent Bill: " + str(pay_interent))
                            save_accounts()
                            print("Paid Interent Bill Successfully!")




                        elif bill_choice == "4":
                            pay_phone = int(input("Pls enter the amount you would like to pay your Phone Bill: "))

                            if pay_phone <= 0:
                                print("Bill cannot be a negative or equal to Zero!")
                                continue

                            if found_account.balance < pay_phone:
                                print("Insufficient Funds")
                                continue


                            found_account.balance -= pay_phone
                            found_account.money_spent_this_month += pay_phone
                            budget_percentage_used = (found_account.money_spent_this_month/found_account.monthly_budget) * 100
                            
                            if found_account.money_spent_this_month > found_account.monthly_budget:
                                print("MAX BUDGET EXCEEDED!")
                            
                            elif found_account.money_spent_this_month >= (found_account.monthly_budget * 0.95):
                                print("WARNING ALMOST EXCEEDED!")
                                print("you have USED", str(int(budget_percentage_used)) + "% of your BUDGET")
                            
                                month_remaining_budget = found_account.monthly_budget - found_account.money_spent_this_month 
                                print("Your REMAINING Budget is: ", month_remaining_budget)
                            
                            elif found_account.money_spent_this_month >= (found_account.monthly_budget * 0.80):
                                print("WARNING!!")
                                print("You have used 80% of your monthly budget")
                            found_account.transaction_history.append("Paid Phone Bill: " + str(pay_phone))
                            save_accounts()
                            print("Paid Phone Bill Successfully!")








                        elif bill_choice == "5":
                            pay_gas = int(input("Pls enter the amount you would like to pay your Gas Bill: "))

                            if pay_gas <= 0:
                                print("Bill cannot be a negative or equal to Zero!")
                                continue


                            if found_account.balance < pay_gas:
                                print("Insufficient Funds")
                                continue


                            found_account.balance -= pay_gas
                            found_account.money_spent_this_month += pay_gas
                            budget_percentage_used = (found_account.money_spent_this_month/found_account.monthly_budget) * 100
                            
                            if found_account.money_spent_this_month > found_account.monthly_budget:
                                print("MAX BUDGET EXCEEDED!")
                            
                            elif found_account.money_spent_this_month >= (found_account.monthly_budget * 0.95):
                                print("WARNING ALMOST EXCEEDED!")
                                print("you have USED", str(int(budget_percentage_used)) + "% of your BUDGET")
                            
                                month_remaining_budget = found_account.monthly_budget - found_account.money_spent_this_month 
                                print("Your REMAINING Budget is: ", month_remaining_budget)
                            
                            elif found_account.money_spent_this_month >= (found_account.monthly_budget * 0.80):
                                print("WARNING!!")
                                print("You have used 80% of your monthly budget")
                            found_account.transaction_history.append("Paid Gas Bill: " + str(pay_gas))
                            save_accounts()
                            print("Paid Gas Bill Successfully!")





                        elif bill_choice == "6":
                            print("Have a Great Day Bye!")
                            break

                        else:
                            print("Invalid Choice pls retry!")






        






    elif choice == "24":

        if found_account.account_locked:
                print("Account is locked!")
                continue
        

        if len(accounts) == 0:
            print("No accounts created yet.")
        else:
            for acc in accounts:
                acc.show_info()









    elif choice == "25":
        print("Have a good day. Bye!")
        break


    else:
        print("Invalid option. Please try again.")
        
