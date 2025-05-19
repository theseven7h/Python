def categorize_numbers(numbers, divisor):
	result = []
	count = 0
	if divisor == 0:
		return "Divisor cannot be zero"
	else:
		for number in numbers:
			if number % divisor == 0:
				result.append(number)
				count += 1
		if count > 0:
			return result
		else:
			return "No divisible number found"
			
while True:			
	try:			
		amount = int(input("How many numbers are you entering: "))
		
		numbers = []
		
		for index in range(amount):
			number = int(input(f"Enter number {index + 1}: "))
			numbers.append(number)
			
		divisor = int(input("\nEnter the divisor: "))
		break
		
	except ValueError:
		print("Please enter integers only. Start again\n")	
		
print(f"{categorize_numbers(numbers, divisor)}")
	