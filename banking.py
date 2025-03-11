import csv

class Customer:
    def __init__(self, account_id, first_name, last_name, password):
        self.account_id = account_id
        self.first_name = first_name
        self.last_name = last_name
        self.password = password


class Account:
    def __init__(self, checking_balance=0.0, savings_balance=0.0):
        self.checking_balance = checking_balance
        self.savings_balance = savings_balance
        self.overdraft_count = 0
        self.is_active = True

    def show_balances(self):
        print(f"Checking: ${self.checking_balance:.2f}, Savings: ${self.savings_balance:.2f}")


class Transaction:
    def __init__(self, customer, account):
        self.customer = customer
        self.account = account

    def deposit(self, amount, account_type):
        if not self.account.is_active:
            print("Account is deactivated.")
            return

        if account_type == "checking":
            self.account.checking_balance += amount
        elif account_type == "savings":
            self.account.savings_balance += amount
        else:
            print("Invalid account type.")
            return

        print(f"Deposited ${amount:.2f} to {account_type}.")

        if self.account.checking_balance >= 0 and self.account.savings_balance >= 0:
            self.account.is_active = True  # Reactivate if account is solvent

    def withdraw(self, amount, account_type):
        if amount > 100:
            print("Withdrawal limit is $100 per transaction.")
            return

        if account_type == "checking":
            projected_balance = self.checking_balance - amount
            if projected_balance < -100:
                print("Cannot withdraw: account balance cannot go below -$100.")
                return
            if amount <= self.checking_balance:
                self.checking_balance -= amount
                print(f"Withdrew ${amount} from Checking Account.")
            else:
                self.checking_balance -= amount
                self.overdrafts += 1
                self.checking_balance -= 35  # overdraft fee
                print(f"Overdraft! ${amount} withdrawn from Checking. $35 overdraft fee charged.")
        elif account_type == "savings":
            projected_balance = self.savings_balance - amount
            if projected_balance < -100:
                print("Cannot withdraw: account balance cannot go below -$100.")
                return
            if amount <= self.savings_balance:
                self.savings_balance -= amount
                print(f"Withdrew ${amount} from Savings Account.")
            else:
                self.savings_balance -= amount
                self.overdrafts += 1
                self.savings_balance -= 35  # overdraft fee
                print(f"Overdraft! ${amount} withdrawn from Savings. $35 overdraft fee charged.")
        else:
            print("Invalid account type.")



class NewCustmer:
    @staticmethod
    def register_new_customer(account_id, first_name, last_name, password, checking=0.0, savings=0.0):
        with open("bank.csv", "a", newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow([account_id, first_name, last_name, password, checking, savings, True, 0])
        print("Customer registered successfully.")

    @staticmethod
    def login(account_id, password):
        with open("bank.csv", "r") as file:
            reader = csv.reader(file, delimiter=';')
            for row in reader:
                if len(row) < 8:
                    continue
                if row[0] == account_id and row[3] == password:
                    customer = Customer(row[0], row[1], row[2], row[3])
                    account = Account(float(row[4]), float(row[5]))
                    account.is_active = row[6] == "True"
                    account.overdraft_count = int(row[7])
                    return customer, account
        print("Login failed.")
        return None, None


NewCustmer.register_new_customer("1001", "Ali", "Salem", "pass123", 200, 300)
customer, account = NewCustmer.login("1001", "pass123")
if customer:
    t = Transaction(customer, account)
    account.show_balances()
    t.deposit(50, "savings")
    t.withdraw(80, "checking")
    t.transfer_between_accounts(50, "savings", "checking")
    t.transfer_to_another_customer(50, "1002")
    account.show_balances()
