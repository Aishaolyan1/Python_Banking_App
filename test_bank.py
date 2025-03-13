import unittest
from banking import Account, Customer, Bank

class TestAccount(unittest.TestCase):
    def test_deposit(self):
        acc = Account(100)
        acc.deposit(50)
        self.assertEqual(acc.balance, 150)

    def test_withdraw_within_limit(self):
        acc = Account(50)
        result = acc.withdraw(30)
        self.assertTrue(result)
        self.assertEqual(acc.balance, 20)

    def test_withdraw_over_limit(self):
        acc = Account(10)
        result = acc.withdraw(120)  
        self.assertFalse(result)
        self.assertEqual(acc.balance, 10)

    def test_withdraw_exactly_limit(self):
        acc = Account(0)
        result = acc.withdraw(100)
        self.assertTrue(result)
        self.assertEqual(acc.balance, -100)

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("1001", "Ali", "Ahmed", "pass", 200, 300)

    def test_view_balances(self):
        self.assertEqual(self.customer.checking_account.balance, 200)
        self.assertEqual(self.customer.savings_account.balance, 300)

    def test_deposit_to_checking(self):
        self.customer.checking_account.deposit(100)
        self.assertEqual(self.customer.checking_account.balance, 300)

    def test_deposit_to_savings(self):
        self.customer.savings_account.deposit(150)
        self.assertEqual(self.customer.savings_account.balance, 450)

    def test_withdraw_from_checking(self):
        result = self.customer.checking_account.withdraw(50)
        self.assertTrue(result)
        self.assertEqual(self.customer.checking_account.balance, 150)

    def test_withdraw_from_savings(self):
        result = self.customer.savings_account.withdraw(100)
        self.assertTrue(result)
        self.assertEqual(self.customer.savings_account.balance, 200)

    def test_overdraft_checking(self):
        result = self.customer.checking_account.withdraw(280)  # balance = 200
        self.assertTrue(result)
        self.assertEqual(self.customer.checking_account.balance, -80)
        self.customers = []
        self.load_data()
    def test_overdraft_beyond_limit(self):
        result = self.customer.checking_account.withdraw(310)  # balance = 200
        self.assertFalse(result)
        self.assertEqual(self.customer.checking_account.balance, 200)

class TestBank(unittest.TestCase):
    def setUp(self):
        self.bank = Bank("test_bank.csv")

    def test_register_customer_method_exists(self):
        self.assertTrue(hasattr(self.bank, "register_customer"))

    def test_login_method_exists(self):
        self.assertTrue(hasattr(self.bank, "login"))

    def test_data_file_default(self):
        self.assertEqual(self.bank.data_file, "test_bank.csv")


if __name__ == "__main__":
    unittest.main()
