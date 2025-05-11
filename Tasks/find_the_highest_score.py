import math

largest_name = ""
largest_score = -math.inf
number_of_students = int(input("Enter the number of students: "))
for index in range(1, number_of_students + 1):
	student_name = str(input(f"Enter student {index}'s name: "))
	student_score = int(input(f"Enter student {index}'s score: "))
	print()
	if student_score > 100 or student_score < 0:
		print("Invalid score...") 
		break
	elif student_score > largest_score:
		largest_name = student_name
		largest_score = student_score
if student_score > largest_score:
	print(f"HIGHEST SCORE:\nName: {largest_name}\nScore: {largest_score}")
		