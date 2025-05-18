
def multiply_two(first_number, second_number):
	if isinstance(first_number, float) and isinstance(second_number, float):
		product = 0
		product_2 = 0
		equal_1 = 0
		equal_2 = 0
		rem_1 = 0
		rem_2 = 0
		if second_number < 0 or first_number < 0:
			equal_1 = first_number
			equal_2 = second_number
			first_number  = abs(first_number)
			second_number = abs(second_number)
		
		if second_number % 1 != 0 and first_number % 1 != 0:
			rem_1 = first_number % 10
			rem_2 = second_number % 10
			second_number //= 10
			first_number //= 10
			
			for index in range(int(rem_2)):
				product += first_number
				product_2 += rem_1
			product += product_2
			product /= 10
			product_2 - 0
			
			for index in range(int(second_number)):
				product += first_number
				product_2 += rem_1
			product += product_2
		
			if equal_1 < 0 and equal_2 < 0:
				return product
			elif equal_1 < 0 or equal_2 < 0:
				return -product
			else:
				return product

	elif isinstance(first_number, float) and isinstance(second_number, int):
		equal_1 = 0
		equal_2 = 0
		product = 0
		
		if second_number < 0 or first_number < 0:
			equal_1 = first_number
			equal_2 = second_number
			first_number  = abs(first_number)
			second_number = abs(second_number)
			
		for index in range(second_number):
			product += first_number
			
		if equal_1 < 0 and equal_2 < 0:
			return product
		elif equal_1 < 0 or equal_2 < 0:
			return -product
		else:
			return product
		
	elif isinstance(first_number, int) and isinstance(second_number, float):	
		equal_1 = 0
		equal_2 = 0
		product = 0
		
		if second_number < 0 or first_number < 0:
			equal_1 = first_number
			equal_2 = second_number
			first_number  = abs(first_number)
			second_number = abs(second_number)
			
		for index in range(first_number):
			product += second_number
			
		if equal_1 < 0 and equal_2 < 0:
			return product
		elif equal_1 < 0 or equal_2 < 0:
			return -product
		else:
			return product
	
	elif isinstance(first_number, int) and isinstance(second_number, int):	
		equal_1 = 0
		equal_2 = 0
		product = 0
		
		if second_number < 0 or first_number < 0:
			equal_1 = first_number
			equal_2 = second_number
			first_number  = abs(first_number)
			second_number = abs(second_number)
			
		for index in range(first_number):
			product += second_number
			
		if equal_1 < 0 and equal_2 < 0:
			return product
		elif equal_1 < 0 or equal_2 < 0:
			return -product
		else:
			return product
			
#first_number = 4.5
#second_number = 2

#print(multiply_two(first_number, second_number))
			
first_number = input("Enter first number: ")
second_number = input("Enter second number: ")

print(f"Product of {first_number} and {second_number} is", multiply_two(first_number, second_number))




