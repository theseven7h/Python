password = input("Enter a password: ")
count = int(0);
for character in password:
	count = count + 1
	
if count < 8: 
	print("Very Weak")
elif count == 8:
	print("Weak")
elif count >= 8 and count <= 16:
	print("Strong")
else: 
	print("Very Strong")