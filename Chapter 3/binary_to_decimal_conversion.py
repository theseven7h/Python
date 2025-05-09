number = int(input("Enter a binary number: "))
decimal = 0
power = 1

print(number, end='')
while number != 0:
	binary = number % 10
	decimal += (binary * power)
	power *= 2
	number //= 10
	
print(f" decimal equivalent is {decimal}")