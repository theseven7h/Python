from unittest import TestCase

import bank_app

class TestBank(TestCase):
	
	def test_if_create_account_function_exists(self):
		bank_app.accounts.clear()
		account_1 = bank_app.create_account("Abdul", "08011111111")
		
	def test_create_account_function_works(self):
		bank_app.accounts.clear()
		account_1 = bank_app.create_account("Abdul", "08011111111")
		self.assertEqual(1, len(bank_app.accounts))

	def test_multiple_accounts_can_be_created(self):
		bank_app.accounts.clear()
		account_1 = bank_app.create_account("Abdul", "08011111111")
		account_2 = bank_app.create_account("Similoluwa", "08022222222")
		account_3 = bank_app.create_account("Obiagazie", "08033333333")
		self.assertEqual(3, len(bank_app.accounts))
		
	def test_account_name_is_correct(self):
		bank_app.accounts.clear()
		account_1 = bank_app.create_account("Abdul", "08011111111")
		self.assertEqual("Abdul", bank_app.get_name(account_1))
	
	def test_phone_number_can_be_found(self):
		bank_app.accounts.clear()
		account_1 = bank_app.create_account("Abdul", "08011111111")
		self.assertEqual("08011111111", bank_app.get_phone_number(account_1))
	
	def test_phone_number_is_unique(self):
		bank_app.accounts.clear()
		account_1 = bank_app.create_account("Abdul", "08011111111", 150)
		self.assertRaises(ValueError, bank_app.create_account, "Similoluwa", "08011111111", 250)
	
	def test_initial_balance_is_zero(self):
		bank_app.accounts.clear()
		account_1 = bank_app.create_account("Abdul", "08011111111")
		self.assertEqual(0.0, bank_app.get_balance(account_1))
	
	def test_initial_balance_can_be_added(self):
		bank_app.accounts.clear()
		account_1 = bank_app.create_account("Abdul", "08011111111", 150)
		self.assertEqual(150.0, bank_app.get_balance(account_1))
		
	def test_balance_can_not_be_negative(self):
		bank_app.accounts.clear()
		self.assertRaises(ValueError, bank_app.create_account, "Abdul", "08011111111", -20)
		
	def test_generate_account_number_function_exists(self):
		bank_app.accounts.clear()
		account_1 = bank_app.create_account("Abdul", "08011111111", 150)
		bank_app.generate_account_number()	
			
	def test_account_number_is_generated(self):
		bank_app.accounts.clear()
		bank_app.new_account_number = 1000000000
		account_1 = bank_app.create_account("Abdul", "08011111111", 150)
		self.assertEqual("1000000001", account_1[3])
		
	def test_get_account_number_function_exists(self):
		bank_app.accounts.clear()
		account_1 = bank_app.create_account("Abdul", "08011111111", 150)
		new_account_number_1 = bank_app.generate_account_number()
		
	def test_account_number_is_unique(self):
		bank_app.accounts.clear()
		bank_app.new_account_number = 1000000000
		account_1 = bank_app.create_account("Abdul", "08011111111", 150)
		self.assertEqual("1000000001", account_1[3])

		account_2 = bank_app.create_account("Similoluwa", "08022222222", 250)
		account_number_2 = bank_app.generate_account_number()	
		self.assertEqual("1000000002", account_2[3])

	def test_get_account_number_function_works(self):
		bank_app.accounts.clear()
		bank_app.new_account_number = 1000000000
		account_1 = bank_app.create_account("Abdul", "08011111111", 150)
		self.assertEqual("1000000001", account_1[3])
		
	def test_find_customer_by_phone_number_function_exists(self):
		bank_app.accounts.clear()
		account_1 = bank_app.create_account("Abdul", "08011111111", 150)
		bank_app.find_customer_by_phone_number("08011111111")
			
	def test_find_customer_by_phone_number_function_returns_the_account(self):
		bank_app.accounts.clear()
		account_1 = bank_app.create_account("Abdul", "08011111111", 150)
		customer = bank_app.find_customer_by_phone_number("08011111111")
		self.assertEqual(account_1, customer)
	
	def test_find_customer_by_phone_number_function_informs_absence_info(self):
		bank_app.accounts.clear()
		account_1 = bank_app.create_account("Abdul", "08011111111", 150)
		self.assertRaises(ValueError, bank_app.find_customer_by_account_number, "08011111115")
		
	def test_find_customer_by_account_number_function_exists(self):
		bank_app.accounts.clear()
		bank_app.new_account_number = 1000000000
		account_1 = bank_app.create_account("Abdul", "08011111111", 150)
		bank_app.find_customer_by_account_number("1000000001")
		
	def test_find_customer_by_account_number_function_works(self):
		bank_app.accounts.clear()
		bank_app.new_account_number = 1000000000
		account_1 = bank_app.create_account("Abdul", "08011111111", 150)
		customer = bank_app.find_customer_by_account_number("1000000001")
		self.assertEqual(customer, account_1)
	
	def test_find_customer_by_account_number_function_informs_absence_info(self):
		bank_app.accounts.clear()
		bank_app.new_account_number = 1000000000
		account_1 = bank_app.create_account("Abdul", "08011111111", 150)
		self.assertRaises(ValueError, bank_app.find_customer_by_account_number, "1000000004")
		
	def test_deposit_function_exists(self):
		bank_app.accounts.clear()
		bank_app.new_account_number = 1000000000
		account_1 = bank_app.create_account("Abdul", "08011111111", 150)
		bank_app.deposit(1000000001, 500)
		
	def test_deposit_function_returns_right_balance(self):
		bank_app.accounts.clear()
		bank_app.new_account_number = 1000000000
		account_1 = bank_app.create_account("Abdul", "08011111111", 150)
		balance = bank_app.deposit("1000000001", 50)
		self.assertEqual(200, balance)
		
	def test_deposit_amount_is_greater_than_zero(self):
		bank_app.accounts.clear()
		bank_app.new_account_number = 1000000000
		account_1 = bank_app.create_account("Abdul", "08011111111", 150)
		self.assertRaises(ValueError, bank_app.deposit, "1000000001", 0)
		
	def test_deposit_amount_is_negative(self):
		bank_app.accounts.clear()
		bank_app.new_account_number = 1000000000
		account_1 = bank_app.create_account("Abdul", "08011111111", 150)
		self.assertRaises(ValueError, bank_app.deposit, "1000000001", -50)
		
	def test_withdraw_function_exists(self):
		bank_app.accounts.clear()
		bank_app.new_account_number = 1000000000
		account_1 = bank_app.create_account("Abdul", "08011111111", 150)
		bank_app.withdraw(1000000001, 50)
		
	def test_withdraw_function_returns_right_balance(self):
		bank_app.accounts.clear()
		bank_app.new_account_number = 1000000000
		account_1 = bank_app.create_account("Abdul", "08011111111", 150)
		balance = bank_app.withdraw("1000000001", 50)
		self.assertEqual(100, balance)
		
	def test_withdrawal_amount_is_greater_than_zero(self):
		bank_app.accounts.clear()
		bank_app.new_account_number = 1000000000
		account_1 = bank_app.create_account("Abdul", "08011111111", 150)
		self.assertRaises(ValueError, bank_app.withdraw, "1000000001", 0)
		
	def test_withdrawal_amount_is_negative(self):
		bank_app.accounts.clear()
		bank_app.new_account_number = 1000000000
		account_1 = bank_app.create_account("Abdul", "08011111111", 150)
		self.assertRaises(ValueError, bank_app.withdraw, "1000000001", -50)