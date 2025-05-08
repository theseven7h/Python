answer1 = input("What is your problem? ")
answer2 = input("Have you had this problem before (yes or no)? ")

if answer2 == "yes":
	print("Well, you have it again")
elif answer2 == "no":
	print("Well, you have it now")
else:
	print("Invalid entry, start again...")