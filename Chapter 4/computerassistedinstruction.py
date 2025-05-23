from random import randint

def rand_tuple():
	num1 = randint(1,9)
	num2 = randint(1,9)
	return (num1,num2)

def get_correct_answer(number):
	num1, num2 = number
	correct_answer = num1 * num2
	return correct_answer

def get_user_answer(number):
	user_answer = int(input(f"How much is {number[0]} times {number[1]}? "))
	return user_answer

number = rand_tuple()
correct = get_correct_answer(number)
user = get_user_answer(number)
print()


while True:
	if correct == user:
		print("Very good!")
		replay = input("Next question? (Yes/No): ").strip().lower()
		print()
		while replay != "yes" and replay != "no":
			replay = input("Wrong input!, Try again: ").strip().lower()
			print()
		if replay == "no":
			break
		
		number = rand_tuple()
		correct = get_correct_answer(number)
		user = get_user_answer(number)
		print()
	else:
		print("No. Please try again.")	
		user = get_user_answer(number)
		print()