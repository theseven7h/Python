number = int(input("Enter an integer: "))
count = number - 1
factorial = number
num = number

for number in range(number - 1):
	factorial *= (count)
	count = count - 1
		
print(f"{num} factorial is {factorial}")