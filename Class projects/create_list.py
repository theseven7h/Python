from random import randint

def random_list():
	rand_list = []
	for number in range(10):
		rand_list.append(randint(1, 51))
	return rand_list
	
def get_length(nums):
	count = 0
	for _ in nums:
		count += 1
	return count
	
def sum_even_positions(numbers):
	total = 0
	for position,number in enumerate(numbers):
		if position % 2 == 1:
			total += number
	return total

def sum_odd_positions(numbers):
	total = 0
	for position,number in enumerate(numbers):
		if position % 2 == 0:
			total += number
	return total

def multiply_elements_at_third_positions(numbers):
	product = 1
	for number in range(2, len(numbers), 3):
			product *= numbers[number]
	return product
	
def calculate_average(numbers):
	total = 0
	for number in numbers:
		total += number
	average = total / get_length(numbers)
	return average