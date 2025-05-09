count = 1
count_2 = 3 
pi_value = 0
while pi_value <= 3.14159: 
	if count % 2 == 0:
		pi_value = -pi_value -(4 / count)	
		print(pi_value, sep=',')

count += 2