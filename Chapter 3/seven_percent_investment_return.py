principal = float(1000)
annual_rate = float(7)

for i in range(1, 31):
	print(f"At year {i}: {principal * ((1 + (annual_rate / 100)) ** i):.2f}")