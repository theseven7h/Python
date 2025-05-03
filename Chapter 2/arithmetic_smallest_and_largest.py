"""Arithmetic, Smallest and Largest"""
first_number = int(input("Enter first integer: "))
second_number = int(input("Enter second integer: "))
third_number = int(input("Enter third integer: "))

largest = first_number
smallest = first_number

if (second_number > largest): largest = second_number
if (third_number > largest): largest = third_number
if (second_number < smallest): smallest = second_number
if (third_number < smallest): smallest = third_number

print("Largest number is", largest)
print("Smallest number is", smallest)
