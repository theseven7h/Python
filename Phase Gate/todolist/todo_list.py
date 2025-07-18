
def add_task(tasks):
	task = input("Enter the task: ").strip()
	tasks.append(task)
	print("Task added!")
	return tasks

def view_tasks(tasks, check):
	if len(tasks) == 0:
		notice = "There are no tasks to view" 
		print(notice)
		return notice
	else:
		count = 1
		for task in tasks:
			if count in check:
				status = "X" 
			else: status = " " 
			print(f"({status})Task {count}: {task}")
			count += 1

def mark_tasks(tasks,check):
	view_tasks(tasks,check)
	mark = int(input("Which task number is completed: "))
	check.append(mark)
	return check
	
def delete_tasks(tasks):
	delete = input("Which task number do you intend deleting: ")
	delete = int(delete)
	count = delete - 1
	for index in range(len(tasks)):
		if (index) == count:
			tasks.pop(index)
	return tasks



def main():
	check = []
	tasks = []
	while True:
		main_menu = input("""
----TO-DO LIST MANAGER----
1. Add a task
2. View tasks
3. Mark task as complete
4. Delete a task
5. Exit
		""").strip()
		
		match main_menu:
			case "1": add_task(tasks)
			case "2": view_tasks(tasks,check)
			case "3": mark_tasks(tasks,check) 
			case "4": delete_tasks(tasks)
			case "5": break
			case _: print("Invalid input")
			
	
main()
	