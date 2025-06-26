import unittest
import create_list


class TestCreateList(unittest.TestCase):
    def test_random_list(self):
        rand_list = create_list.random_list()
        self.assertEqual(type(rand_list), list)
        self.assertEqual(len(rand_list), 10)
        rand_list.append(3)
        self.assertEqual(len(rand_list), 11)

    def test_get_length(self):
        nums = [1,2,3,4,5]
        #rand_list = create_list.random_list()
        self.assertEqual(create_list.get_length(nums), 5)
        nums.append(6)
        self.assertEqual(create_list.get_length(nums), 6)

    def test_sum_even_positions(self):
        numbers = [1,2,3,4,5,6,7,8,9]
        self.assertEqual(create_list.sum_even_positions(numbers), 20)
        numbers.append(10)
        self.assertEqual(create_list.sum_even_positions(numbers), 30)

    def test_sum_odd_positions(self):
        numbers = [1,2,3,4,5,6,7,8,9]
        self.assertEqual(create_list.sum_odd_positions(numbers), 25)
        numbers.append(10)
        numbers.append(11)
        self.assertEqual(create_list.sum_odd_positions(numbers), 36)

    def test_multiply_elements_at_third_positions(self):
        numbers = [1,2,3,4,5,6,7,8,9]
        self.assertEqual(create_list.multiply_elements_at_third_positions(numbers), 162)
        numbers.append(10)
        numbers.append(11)
        numbers.append(12)
        self.assertEqual(create_list.multiply_elements_at_third_positions(numbers), 1944)

    def test_calculate_average(self):
        numbers = [1,2,3,4,5,6,7,8,9]
        self.assertEqual(create_list.calculate_average(numbers), 5)
        numbers.append(10)
        self.assertEqual(create_list.calculate_average(numbers), 5.5)

if __name__ == '__main__':
    unittest.main()
