number = int(input("Enter a five-digit integer: "))

rem = 0
spacedNumber = 0;
for digit in range(5):
	rem = number // (10 ** (4 - digit))
	print(f"{rem}", end='  ')
	number = number % (10 ** (4 - digit))