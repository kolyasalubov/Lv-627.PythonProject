import unittest
from Tasks.task_113a import task_113a

class Test113a(unittest.TestCase):

    def test_double_factorial(self):
        result1 = task_113a._task(1)
        result2 = task_113a._task(5)
        result3 = task_113a._task(6)
        self.assertEqual(result1, 1)
        self.assertEqual(result2, 15)
        self.assertEqual(result3, 48)

if __name__ == '__main__':
    unittest.main()