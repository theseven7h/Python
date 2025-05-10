for i in range(1, 21):
	for j in range(i, 21):
		for k in range(j, 21):
			if i ** 2 + j ** 2 == k ** 2:
				print(f"({i}, {j}, {k})")
			
	gi