gallons_used = float(input("Enter the gallons used (-1 to end): "))
total_miles_driven = 0;
total_gallons_used = 0;

while gallons_used != -1:
	miles_driven = float(input("Enter the miles driven: "))
	miles_per_gallon = miles_driven / gallons_used
	total_miles_driven += miles_driven
	total_gallons_used += gallons_used
	
	print(f"The miles/gallon for this tank was {miles_per_gallon:.6f}")
	gallons_used = float(input("Enter the gallons used (-1 to end): "))
	
print(f"The overall average miles/gallon was {total_miles_driven / total_gallons_used:.6f}")