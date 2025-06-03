'''
Enter their acct bal at the start

Withdraw money
	Withdrawals must be multiples of 500 or 1000
	withdrawal charge of 100 to every transaction
	cannot withdraw more than 90% of bal
	remaining balance must be 100 or above
	
Display account details after each transaction
	show amount withdrawn, withdrawal fee, remaining bal
	if withdrawal conditions are not met, prompt the user to enter a valid amount
	
Allow multiiple withdrawals until the user chooses to exit

User should be able to log to see their transactions	

only valid numeric inputs should be allowed 
users


your current balance
enter withdrawal amount multiples of 500 or 1000
Transaction successful
withdrawal amount
withdrawal fee
remaining balance

do you want to make another withdrawal
invalid amount. withdrawals muust be in multiples of 500 or 1000
you cannot withdraw more than 90%

Thank you for using James bank
'''	
def withdraw(balance, amount):
	message = ""
	if amount > balance:
		message = "Insufficient funds"
	elif (amount % 500) != 0:
		message = "Invalid amount! Withdrawals must be in multiples of N500 or N1000"
	elif amount > (balance * 0.90):
		message = "You cannot withdraw more than 90% of your balance"
	elif amount <= 0: 	
		message = "Amount must be greater than N0" 
	elif amount > 20000:
		message = "You cannot exceed N20000 per transaction"
	else:
		balance = balance - amount - 100
		message = "Transaction successful!"
	return message,balance
	
	
def main(): 
	print()
	logs = []
	print("---Welcome to THE SEVENTH ATM----")
	balance = float(input("Enter your account balance (above 0): "))
	while balance <= 0:
		balance = float(input("Invalid! Enter your account balance (above 0): "))
	while True:		
		print(f"\nYour current balance: N{balance:,.2f}")
		
		amount = float(input("\nEnter withdrawal amount (multiples of 500 or 1000): "))
		message,balance = withdraw(balance, amount)
		
		while message != "Transaction successful!":	
			print(message)
			amount = float(input("\nEnter withdrawal amount (multiples of 500 or 1000): "))	
			message,balance = withdraw(balance, amount)
		
		details = f"\n{message}\nWithdrawal Amount: N{amount:,.2f}\nWithdrawal Fee: N{100:.2f}\nRemaining Balance: N{balance:,.2f}"
		
		print(details)
		
		logs.append(details)
		
		repeat = ""
		while True:
			repeat = input("\nDo you wish to make another withdrawal (Yes/No): ").lower().strip()
			if repeat in ["yes", "no"]:  break
			else: print("\nInvalid! Yes/No")
			
		if repeat == "no": 
			print("\nThank you for using The Seventh Bank. Have a good day ^_^\n\n---TRANSACTION HISTORY--- ")
			
			for log in logs:
				print(log)
			break 
			
#main()