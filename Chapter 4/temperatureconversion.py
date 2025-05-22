def temperature_conversion(celcius):
	return (9 / 5) * celcius + 32

print(f"{'Celcius':<10}{'Fahrenheit'}")	
for celcius in range(0, 101):
	print(f"{celcius:>7}{temperature_conversion(celcius):12.1f}")