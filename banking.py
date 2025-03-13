import csv
from datetime import datetime

TRANSACTION_FILE = "transactions.csv"
BANK_DATA_FILE = "bank.csv"


class Account:
    def __init__(self, balance=0.0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def can_withdraw(self, amount):
        return self.balance - amount >= -100 and amount <= 100

    def withdraw(self, amount):
        if self.can_withdraw(amount):
            self.balance -= amount
            return True
        return False


class Customer:
    def __init__(self, account_id, first_name, last_name, password, checking_balance, savings_balance, active=True, overdraft_count=0):
        self.account_id = account_id
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.checking_account = Account(checking_balance)
        self.savings_account = Account(savings_balance)
        self.active = active
        self.overdraft_count = overdraft_count

    def view_balances(self):
        print(f"Checking Balance: ${self.checking_account.balance:.2f}")
        print(f"Savings Balance: ${self.savings_account.balance:.2f}")

    def apply_overdraft_penalty(self, account):
        account.balance -= 35
        self.overdraft_count += 1
        print("Overdraft occurred! $35 fee charged.")
        if self.overdraft_count > 2:
            self.active = False
            print("Account deactivated due to multiple overdrafts.")

    def check_reactivate_account(self):
        if self.checking_account.balance >= 0 and not self.active:
            self.active = True
            self.overdraft_count = 0
            print("Account reactivated.")


class Bank:
    def __init__(self):
        self.data_file = BANK_DATA_FILE

    def register_customer(self):
        print(" Register New Customer ")
        account_id = input("Account ID: ")
        first = input("First Name: ")
        last = input("Last Name: ")
        pwd = input("Password: ")
        checking = float(input("Initial checking balance: "))
        savings = float(input("Initial savings balance: "))
        with open(self.data_file, "a", newline="") as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerow([account_id, first, last, pwd, checking, savings, "True", 0])
        print("Customer registered successfully.")

    def login(self):
        account_id = input("Account ID: ")
        pwd = input("Password: ")
        with open(self.data_file, "r") as f:
            reader = csv.reader(f, delimiter=';')
            for row in reader:
                if row[0] == account_id and row[3] == pwd:
                    print(f"Welcome {row[1]} {row[2]}!")
                    return Customer(row[0], row[1], row[2], row[3], float(row[4]), float(row[5]), row[6] == "True", int(row[7]))
        print("Login failed.")
        return None
    # After successful login, the customer can perform the following services:
# 1- View account balances (Checking and Savings)
# 2- Deposit money into Checking or Savings account
# 3- Withdraw money from Checking or Savings account
# 4-Transfer money from Checking to Savings and vice versa
# 5- Exit the application

    def update_customer_data(self, customer):
        rows = []
        with open(self.data_file, "r") as f:
            reader = csv.reader(f, delimiter=';')
            for row in reader:
                if row[0] == customer.account_id:
                    row = [
                        customer.account_id,
                        customer.first_name,
                        customer.last_name,
                        customer.password,
                        customer.checking_account.balance,
                        customer.savings_account.balance,
                        str(customer.active),
                        str(customer.overdraft_count)
                    ]
                rows.append(row)
        with open(self.data_file, "w", newline="") as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerows(rows)

    def record_transaction(self, account_id, txn_type, amount, resulting_balance):
        with open(TRANSACTION_FILE, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([account_id, txn_type, amount, resulting_balance, datetime.now().strftime("%Y-%m-%d %H:%M:%S")])


class BankApp:
    def __init__(self):
        self.bank = Bank()

    def run(self):
        print("Welcome to Online Banking ")
        print("1. Login")
        print("2. Register")
        choice = input("Choose: ")
        if choice == "1":
            customer = self.bank.login()
            if customer and customer.active:
                self.menu(customer)
            elif customer and not customer.active:
                print("Account is deactivated. Please deposit to reactivate.")
        elif choice == "2":
            self.bank.register_customer()

    def menu(self, customer):
        while True:
            print("\nBanking Menu ")
            print("1. View Balances")
            print("2. Deposit to Checking")
            print("3. Deposit to Savings")
            print("4. Withdraw from Checking")
            print("5. Withdraw from Savings")
            print("6. Transfer: Checking ➝ Savings")
            print("7. Transfer: Savings ➝ Checking")
            print("8. Exit")
            choice = input("Choose: ")

            if choice == "1":
                customer.view_balances()

            elif choice == "2":
                amt = float(input("Amount: "))
                customer.checking_account.deposit(amt)
                self.bank.record_transaction(customer.account_id, "Deposit-Checking", amt, customer.checking_account.balance)

            elif choice == "3":
                amt = float(input("Amount: "))
                customer.savings_account.deposit(amt)
                self.bank.record_transaction(customer.account_id, "Deposit-Savings", amt, customer.savings_account.balance)

            elif choice == "4":
                amt = float(input("Amount: "))
                if amt > 100:
                    print("Withdrawal denied: Max $100 allowed.")
                    continue
                if customer.checking_account.withdraw(amt):
                    self.bank.record_transaction(customer.account_id, "Withdraw-Checking", amt, customer.checking_account.balance)
                else:
                    customer.apply_overdraft_penalty(customer.checking_account)
                    self.bank.record_transaction(customer.account_id, "Overdraft-Checking", amt, customer.checking_account.balance)

            elif choice == "5":
                amt = float(input("Amount: "))
                if amt > 100:
                    print("Withdrawal denied: Max $100 allowed.")
                    continue
                if customer.savings_account.balance >= amt:
                    customer.savings_account.withdraw(amt)
                    self.bank.record_transaction(customer.account_id, "Withdraw-Savings", amt, customer.savings_account.balance)
                else:
                    print("Insufficient funds.")

            elif choice == "6":
                amt = float(input("Amount: "))
                if customer.checking_account.balance >= amt:
                    customer.checking_account.withdraw(amt)
                    customer.savings_account.deposit(amt)
                    self.bank.record_transaction(customer.account_id, "Transfer-Checking➝Savings", amt, customer.checking_account.balance)
                else:
                    print("Insufficient checking balance.")

            elif choice == "7":
                amt = float(input("Amount: "))
                if customer.savings_account.balance >= amt:
                    customer.savings_account.withdraw(amt)
                    customer.checking_account.deposit(amt)
                    self.bank.record_transaction(customer.account_id, "Transfer-Savings➝Checking", amt, customer.savings_account.balance)
                else:
                    print("Insufficient savings balance.")

            elif choice == "8":
                customer.check_reactivate_account()
                self.bank.update_customer_data(customer)
                print("Thank you for banking with us.")
                break

            else:
                print("Invalid choice.")


if __name__ == "__main__":
    app = BankApp()
    app.run()