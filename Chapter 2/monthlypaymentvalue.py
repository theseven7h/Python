"""Calculating monthly payment value for mortgage"""

principal_amount = float(input("Enter the principal amount: "))
annual_interest_rate = float(input("Enter the annual interest rate: "))
duration_in_years = float(input("Enter the duration in years: "))

monthly_interest_rate = annual_interest_rate / 100 / 12
number_of_months = duration_in_years * 12

monthly_payment = principal_amount * (((monthly_interest_rate * (1 + monthly_interest_rate) ** number_of_months) / (((1 + monthly_interest_rate) ** number_of_months) - 1)))

print(f"Your monthly payment is ${monthly_payment: ,.2f}")
