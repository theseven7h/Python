from random import randrange

mystery_number = randrange(1, 1001, 1)
print("Guess my number between 1 and 1000 with the fewest guesses")
count = 1
while True:
	user_number = int(input(f"Attempt {count}: "))
	if user_number == mystery_number:
		print("Congratulations. You guessed the number!") 
		print()
		mystery_number = randrange(1, 1001, 1)
		while True:	
			replay = int(input("Play again(1) or quit(0)?: "))
			if replay == 0:
				print("Thank you for playing ^_^...")
				break
			else:
				print("Wrong input...")
		break
	elif user_number > mystery_number:
		print("Too high. Try again.")
	elif user_number < mystery_number:
		print("Too low. Try again.")
	print()
	count += 1