accounts = []
new_account_number = 1000000000

def create_account(name,phone,bal=0.0):
	if bal < 0.0:
		raise ValueError("Balance cannot be less than zero")
	
	for account in accounts:
		if account[1] == phone:
			raise ValueError("This phone number is in use already")
			
	account_number = generate_account_number()	
	account = [name,phone,bal,account_number]
	accounts.append(account)
	return account                 

def get_name(account):
	return account[0]	
	
def get_phone_number(account):
	return account[1]
	
def get_balance(account):
	return account[2]
	
def generate_account_number():
	global new_account_number
	new_account_number += 1
	return str(new_account_number)
	
def get_account_number(account):
	return account[3]
		
def find_customer_by_phone_number(phone):
	for acc in accounts:
		if phone == acc[1]:
			return acc
						
	raise ValueError("No customer with this phone number")
	
def find_customer_by_account_number(account_number):
	for acc in accounts:
		if account_number == acc[3]:
			return acc
	
	raise ValueError("No customer with this account number")
	
def deposit(account_number, amount):
	if amount == 0.0:
		raise ValueError("Deposit amount cannot be 0.0")
	elif amount < 0.0:
		raise ValueError("Deposit amount cannot negative")
	for acc in accounts:
		if account_number == acc[3]:
			acc[2] += amount
			return acc[2]
		
def withdraw(account_number, amount):
	if amount == 0.0:
		raise ValueError("Withdrawal amount cannot be 0.0")
	elif amount < 0.0:
		raise ValueError("Withdrawal amount cannot negative")
	for acc in accounts:
		if account_number == acc[3]:
			acc[2] -= amount
			return acc[2]		 