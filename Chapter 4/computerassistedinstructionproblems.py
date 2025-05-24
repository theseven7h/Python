from random import randint

def get_correct_answer(number, operator):
	num1, num2 = number	
	sign = ""
	if operator == 1:
		correct_answer = num1 + num2
		sign = "plus"
	if operator == 2:
		correct_answer = num1 - num2
		sign = "minus"
	if operator == 3:
		correct_answer = num1 * num2
		sign = "times"
	if operator == 4:
		if num2 == 0:
			print("Divisor cannot be 0")
			return
		correct_answer = num1 / num2
		sign = "divided by"
	return correct_answer
	
def rand_tuple(level):
	if level == 1:
		num1 = randint(1,9)
		num2 = randint(1,9)
	if level == 2:
		num1 = randint(10,99)
		num2 = randint(10,99)
	return (num1,num2)

def get_user_answer(number, operator):
	if operator == 1:
		sign = "plus"
	if operator == 2:
		sign = "minus"
	if operator == 3:
		sign = "times"
	if operator == 4:
		sign = "divided by"
	user_answer = input(f"How much is {number[0]} {sign} {number[1]}? ")
	if operator == 4:
		user_answer = float(user_answer)
	return user_answer

def get_responses_when_correct():
	response = randint(1,3)
	match response:
		case 1: print("Very good!")
		case 2: print("Nice work!")
		case 3: print("Keep up the good work!")
		
def get_responses_when_wrong():
	response = randint(1,3)
	match response:
		case 1: print("No. Please try again.")
		case 2: print("Wrong. Try once more.")
		case 3: print("No. Keep trying.")

operator = int(input("Addition(1), Subtraction(2), Multiplication(3), Division(4): "))
level = int(input("Enter difficulty level (1/2): "))
number = rand_tuple(level)
correct = get_correct_answer(number, operator)
user = get_user_answer(number, operator)
print()


while True:
	if correct == user:
		get_responses_when_correct()
		replay = input("Next question? (Yes/No): ").strip().lower()
		print()
		while replay != "yes" and replay != "no":
			replay = input("Wrong input!, Try again: ").strip().lower()
			print()
		if replay == "no":
			break
		level = int(input("Enter difficulty level (1/2): "))
		number = rand_tuple(level)
		correct = get_correct_answer(number, operator)
		user = get_user_answer(number, operator)
		print()
	else:
		get_responses_when_wrong()	
		user = get_user_answer(number, operator)
		print()


