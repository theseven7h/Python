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


number = rand_tuple()
correct = get_correct_answer(number)
user = get_user_answer(number)
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
		
		number = rand_tuple()
		correct = get_correct_answer(number)
		user = get_user_answer(number)
		print()
	else:
		get_responses_when_wrong()	
		user = get_user_answer(number)
		print()
