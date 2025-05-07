number = (int(input("Enter a five-digit number: ")))

reversed = number
rem = 0
palindrome = 0 
count = 1
while count <= 5:
	rem = number % 10
	palindrome = (palindrome * 10) + rem
	number //= 10
	count = count + 1

if reversed == palindrome:
	print(f"{reversed:} is a palindrome")
if reversed != palindrome:
	print(f"{reversed:} is not a palindrome")

 