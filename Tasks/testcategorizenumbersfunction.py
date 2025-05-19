import unittest
import categorizenumbers

class TestCategorizeNumbers(unittest.TestCase):
	def test_categorize_numbers_function_exists(self):
		self.assertTrue(callable(categorizenumbers.categorize_numbers))
		
	def test_function_contains_arguments(self):
		numbers = [5, 7]
		divisor = 5
		categorizenumbers.categorize_numbers(numbers, divisor)
		
	def test_list_function_returns_results(self):
		actual = categorizenumbers.categorize_numbers([5, 7, 20, 33, 35], 5)
		expected = (5, 20, 35)
		self.assertEqual(actual, expected)