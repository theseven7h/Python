import unittest
import categorizenumbers

class TestCategorizeNumbers(unittest.TestCase):
	def test_categorize_numbers_function_exists(self):
		self.assertTrue(callable(categorizenumbers.categorize_numbers))
		
	def test_function_contains_arguments(self):
		numbers = [5, 7]
		divisor = 5
		categorizenumbers.categorize_numbers(numbers, divisor)
		
	def test_function_returns_result_when_divisible_number_found(self):
		actual = categorizenumbers.categorize_numbers([5, 7, 20, 33, 35], 5)
		expected = [5, 20, 35]
		self.assertEqual(actual, expected)
		
	def test_function_prints_message_if_no_divisor_found(self):
		actual = categorizenumbers.categorize_numbers([5, 7, 20, 33, 35], 9)
		expected = "No divisible number found"
		self.assertEqual(actual, expected)
		
	def test_if_divisor_is_0(self):
		#actual = categorizenumbers.categorize_numbers([5, 7, 20, 33, 35], 0)
		expected = "Divisor cannot be zero"
		self.assertEqual(expected, categorizenumbers.categorize_numbers([5, 7, 20, 33, 35], 0))
		
	