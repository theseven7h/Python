def multiply_two(first_number, second_number):
	product = 0
	for index in range(second_number):
		product += first_number
	return product
	
first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))

print(f"Product of {first_number} and {second_number} is", multiply_two(first_number, second_number))

