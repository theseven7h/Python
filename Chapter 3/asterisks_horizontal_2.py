for row in range(1, 11):
	print(f"{"*" * row:<13}{"*" * (11 - row):<13}{" " * (row)}{"*" * (11 - row)}{" " * (13 - row):}{"*" * row}")