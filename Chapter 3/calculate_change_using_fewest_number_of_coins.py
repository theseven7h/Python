purchase_price = int(input("Enter price of item in cents: "))
bill_paid_in_dollar = 1
dollar_in_cents = 1 * 100

if purchase_price == 100:
	print("You have no change")
elif purchase_price == 0:
	print("You have not made any purchase")
else:
	change = dollar_in_cents - purchase_price
	print("Your change is:")
	
	quarter_change = change // 25
	if quarter_change > 0:
		print(quarter_change, "quarter(s)")
	dime_change = (change % 25) // 10
	if dime_change > 0:
		print(dime_change, "dime(s)")
	penny_change = ((change % 25) % 10)
	if penny_change > 0:
		print(penny_change, "pennies")
