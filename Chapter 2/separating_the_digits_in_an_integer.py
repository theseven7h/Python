"""Separating the Digits in an Integer"""
number = int(input("Enter a five-digit integer: "))
num_1 = number % 10
num_2 = (number // 10) % 10
num_3 = (number // 100) % 10
num_4 = (number // 1000) % 10
num_5 = number // 10000 

print(f"{num_5:<3d} {num_4:<3d} {num_3:<3d} {num_2:<3d} {num_1:<3d}")