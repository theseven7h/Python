number = 1
count = number
factorial = 1
num = number
e = 0;

while count >= number:
	factorial *= (count)
	count = count - 1
	for number in range(1):
		e += (1 / factorial)
		print(e, end=',')
		
	number += 1
	if number == 11:
		break