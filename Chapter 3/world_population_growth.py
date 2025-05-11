CURRENT_WORLD_POPULATION = 8220836679
GROWTH_RATE = 0.84 / 100
sub_world_population = CURRENT_WORLD_POPULATION
year = 2026
row = 1

print(f"{"Year":<10}{"World Population":<20}{"Numerical Increase":<20}")
while row <= 100:
	numerical_increase = sub_world_population * GROWTH_RATE
	sub_world_population += numerical_increase
	print(f"{year:<10}{sub_world_population:<20,.0f}{numerical_increase:<20,.0f}")	
	year += 1
	row += 1	

CURRENT_WORLD_POPULATION = 8220836679
sub_world_population = CURRENT_WORLD_POPULATION	
year = 2026

while sub_world_population <= CURRENT_WORLD_POPULATION * 2:
	numerical_increase = sub_world_population * GROWTH_RATE
	sub_world_population += numerical_increase
	year += 1
	
print(f"\nThe current world population is doubled by year {year}")