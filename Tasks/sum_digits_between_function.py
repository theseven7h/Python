def sum_digits_betweeen(number):
	sum = 0	
	for index in str(number):
		rem = number % 10
		sum += rem
		number //= 10
	return sum

number = int(input("Enter a number(1 - 999): "))
while number < 1 or number > 999:
	number = int(input("\nInvalid. Enter a number(1 - 999): "))
print("Sum of digit(s) between is", sum_digits_betweeen(number))
