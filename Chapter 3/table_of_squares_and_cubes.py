for number in range(-1, 6):
	if number == -1:
		print(f"{'number':>9}{'square':>9}{'cube':>9}")
	else:
		print(f"{number:>9}{number ** 2:>9}{number ** 3:>9}")