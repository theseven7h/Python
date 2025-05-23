from random import randrange

mystery_number = randrange(1, 1001, 1)

while True:
	user_number = int(input("\nGuess my number between 1 and 1000 with the fewest guesses: "))
	if user_number == mystery_number:
		print("Congratulations. You guessed the number!") 
		print()
		replay = int(input("Play again(1) or quit(0)?: "))
		mystery_number = randrange(1, 1001, 1)
		if replay == 0:
			print("Thank you for playing ^_^...")
			break
	elif user_number > mystery_number:
		print("Too high. Try again.")
	elif user_number < mystery_number:
		print("Too low. Try again.")