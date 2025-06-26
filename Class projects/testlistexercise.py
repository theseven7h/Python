import unittest

import listexercise


class MyTestCase(unittest.TestCase):
    def test_access_third_element(self):
        numbers = [10,20,30,40,50]
        self.assertEqual(30, listexercise.access_third_element(numbers))

    def test_change_last_element(self):
        colours = ["red","green","blue"]
        listexercise.change_last_item(colours)
        self.assertEqual(["red","green","yellow"], colours)

    def test_append_element(self):
        colours = ["red", "green", "blue"]
        listexercise.append_element(colours)
        self.assertEqual(["red", "green", "blue", "purple"], colours)

    def test_remove_element_3(self):
        numbers = [1,2,3,4,5]
        listexercise.remove_element_3(numbers)
        self.assertEqual([1,2,4,5], numbers)

    def test_return_list_of_lengths(self):
        names = ["Alice", "Bob", "Charlie"]
        self.assertEqual([5,3,7], listexercise.return_list_of_lengths(names))

    def test_sort_in_ascending_order(self):
        numbers = [4, 1, 3, 9, 2]
        self.assertEqual([1, 2, 3, 4, 9], listexercise.sort_list_in_ascending_order(numbers))

    def test_obtain_even_numbers(self):
        numbers = [1,2,3,4,5,6,7,8,9,9,12]
        self.assertEqual([2,4,6,8,12], listexercise.obtain_even_numbers(numbers))

    def test_combine_two_lists(self):
        list1 = [1,2,3]
        list2 = [4,5,6]
        self.assertEqual([1,2,3,4,5,6], listexercise.combine_two_lists(list1, list2))

    def test_obtain_strings_with_more_than_3_characters(self):
        words = ["lamb", "kit", "yam", "kings", "dogs", "man"]
        self.assertEqual(["lamb", "kings", "dogs"], listexercise.obtain_strings_with_more_than_3_characters(words))

if __name__ == '__main__':
    unittest.main()
