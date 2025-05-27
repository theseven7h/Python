import todo_list

from unittest import TestCase

class TestTodoList(TestCase):
	def test_add_task_function_exists(self):
		todo_list.add_task()
		
	def test_add_task_function_returns_right_task(self):
		tasks = todo_list.add_task()
		self.assertEqual(1, len(tasks))