count = 1
factorial = 1
exponential = 1

while count <= 10:
	factorial *= (count)
	exponential += (1 / factorial)
	print(f"Exponential at {count}: {exponential:.4f}")
	count += 1
		
