import unittest
from bank_account import BankAccount

class AccountBalanceTestCase(unittest.TestCase):
    def setUp(self):
        self.account_yangu = BankAccount()

    def test_balance(self):
        self.assertEqual(self.account_yangu.balance, 3000, msg = 'Account balance is invalid')
    
    def test_withdraw(self):
        self.account_yangu.withdraw(500)
        self.assertEqual(self.account_yangu.balance, 2500, msg = 'Withdraw method is invalid')

    def test_deposit(self):
        self.account_yangu.deposit(5000)
        self.assertEqual(self.account_yangu.balance, 8000, msg = 'Deposit method is invalid')
        