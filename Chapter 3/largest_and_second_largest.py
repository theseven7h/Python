count = 0
largest = -200000000000000000
largest_2 = -200000000000000000
while count < 10:
	number = int(input("Enter number: "))
	if number > largest:
		largest_2 = largest
		largest = number
	elif number > largest_2:
		largest_2 = number
	count += 1
	
print(f"Largest number is {largest}\nSecond largest is {largest_2}")