sum = 0
average = 0.0
product = 1
smallest = 2000000000000
largest = -2000000000000

for digit in range(1, 5):
	number = int(input(f"Enter integer {digit}: "))
	if number > largest:
		largest = number
	if number < smallest:
		smallest = number
	sum += number
	product *= number
	
average = float(sum / 4)

print(f"""
	Sum: {sum}
	Average: {average}
	Product: {product}
	Smallest: {smallest}
	Largest: {largest}
""")
	 