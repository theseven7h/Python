import encrypt

from unittest import TestCase

class TestEncryptText(TestCase):
	def test_encrypt_text_function_exists(self):
		encrypt.encrypt_text("ABC")
		
	def test_encrypt_text_function_retuns_correct_result(self):
		actual = encrypt.encrypt_text("Hello,World!")
		expected = "Uryyb,Jbeyq!"
		self.assertEqual(actual, expected)