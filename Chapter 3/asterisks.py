for i in range(1, 11):
	for j in range(i):
		print('*', end='')
	print()
print()

for i in range(10, 0, -1):
	for j in range(i):
		print('*', end='')
	print()
print()

for i in range(1, 11):
	for j in range(i):
		print(' ', end='')
	
	for k in range(11, i, -1):
		print('*', end='')
	print()
print()

for i in range(10, 0, -1):
	for j in range(i):
		print(' ', end='')
	
	for k in range(i, 10, 1):
		print('*', end='')
	print()
print()
