import todo_list

from unittest import TestCase

class TestTodoList(TestCase):
	'''def test_add_task_function_exists(self):
		tasks = []
		todo_list.add_task(tasks)
		
	def test_add_task_function_returns_right_task(self):
		tasks = []
		added_tasks = todo_list.add_task(tasks)
		self.assertEqual(1, len(tasks))
		
	def test_view_tasks_function_exists(self):
		tasks = []
		todo_list.view_tasks([])  
	
	def test_view_tasks_function_informs_for_empty_list(self):
		tasks = []
		self.assertEqual(todo_list.view_tasks([]), "There are no tasks to view")

	def test_mark_tasks_function_exists(self):
		tasks = []
		todo_list.mark_tasks([])'''
		
	def test_delete_tasks_function_exists(self):
		tasks = [1]
		todo_list.delete_tasks([1])
	