from Tasks.task_562 import task_562
import unittest

class Test562(unittest.TestCase):

    def test_armstrong_number(self):

        result = task_562.find_all_two_to_four_digit_armstrong_numbers()
        self.assertEqual(result, [153, 370, 371, 407, 1634, 8208, 9474])
