from random import randrange

def mystery_number():
	mystery_number = randrange(1, 1001, 1)
	print(mystery_number,"Guess my number between 1 and 1000 with the fewest guesses")
	count = 1
	while True:
		if count == 11:
			print("You should be able to do better!\n")
		user_number = int(input(f"Attempt {count}: "))
		if user_number == mystery_number:
			print("\nCongratulations. You guessed the number!") 
			if count <= 10:
				print(f"{count} guess{'es' if count > 1 else ''}? Either you know the secret or you got lucky!")
			return
		elif user_number > mystery_number:
			print("Too high. Try again.")
		elif user_number < mystery_number:
			print("Too low. Try again.")
		print()
		count += 1
				
while True:	
	mystery_number()
	replay = int(input("\nPlay again(1) or quit(0)?: "))
	print()
	if replay == 0:
		print("Thank you for playing ^_^...")
		break
	elif replay == 1:
		continue
	else:
		print("Wrong input...")
