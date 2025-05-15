number = int(input("Enter a number(1 - 999): "))
while number < 1 or number > 999:
	number = int(input("\nInvalid. Enter a number(1 - 999): "))
sum = 0	
for index in str(number):
	rem = number % 10
	sum += rem
	number //= 10
print(sum)