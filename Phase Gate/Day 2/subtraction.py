from random import randint

def check(num1,num2,diff):
	return num1 - num2 == diff
	
correct = 0
for count in range(1,11): 
	num1 = int(randint(0,21))
	num2 = int(randint(0,21))
	while num1 < num2:
		num1 = int(randint(0,21))
		num2 = int(randint(0,21))
	
	for i in range(2):
		diff = int(input(f"{num1} - {num2} = "))
		if check(num1,num2,diff) == True:
			print("Correct!")
			correct += 1
			break

		print()
		if i == 0: 
			print("One more try!")
			continue
			
		print("Wrong!")

print(f"Total score = {correct}/10")