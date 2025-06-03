import atm

from unittest import TestCase

class TestATM(TestCase):
	def test_withdraw_function_exists(self):
		atm.withdraw(4000, 1000)
		
	def test_withdraw_function_returns_right_balance(self):
		msg,bal = atm.withdraw(4000, 1000)
		self.assertEqual(bal, 2900)
		
	def test_message_insufficient_funds(self):
		msg,bal = atm.withdraw(4000, 7000)
		self.assertEqual(msg, "Insufficient funds")
		
	def test_message_multiples_of_500_1000(self):
		msg,bal = atm.withdraw(4000, 3050)
		self.assertEqual(msg, "Invalid amount! Withdrawals must be in multiples of N500 or N1000")

	def test_message_90percent_balance(self):
		msg,bal = atm.withdraw(4000, 4000)
		self.assertEqual(msg, "You cannot withdraw more than 90% of your balance")
		
	def test_message_zero_amount(self):
		msg,bal = atm.withdraw(4000, 0)
		self.assertEqual(msg, "Amount must be greater than N0")
		
	def test_message_20000_amount(self):
		msg,bal = atm.withdraw(50000, 21000)
		self.assertEqual(msg, "You cannot exceed N20000 per transaction")
		
	def test_message_successful_withdrawal(self):
		msg,bal = atm.withdraw(50000, 3000)
		self.assertEqual(msg, "Transaction successful!")