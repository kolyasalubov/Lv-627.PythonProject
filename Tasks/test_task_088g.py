from Tasks.task_088g import task_088g
import unittest

class TestTask088g(unittest.TestCase):

    def test_arguments(self):
        self.assertEqual(task_088g.run_body(0), 101)
        self.assertEqual(task_088g.run_body(89), 1891)
        self.assertEqual(task_088g.run_body(111), 11111)
        self.assertEqual(task_088g.run_body(767854), 17678541)

    def test_values(self):
        self.assertRaises(ValueError, task_088g.run_body, -1)
        self.assertRaises(ValueError, task_088g.run_body, -10)
