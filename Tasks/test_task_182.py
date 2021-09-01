from string import Template
from unittest import TestCase

from Tasks.task_182 import task_182
from task_error import TaskError


class TestTask182(TestCase):
    valid_cases = [
        {'number': 4, 'amount': 0, 'sum': 0},
        {'number': 6, 'amount': 1, 'sum': 5},
        {'number': 10, 'amount': 2, 'sum': 15},
        {'number': 35, 'amount': 6, 'sum': 105},
        {'number': 149, 'amount': 25, 'sum': 1825},
    ]

    error_cases = [0, -1, -15, -258]

    template = Template(
        ("In sequence 1...$number is $amount members that are divisible"
         " by 5 and not divisible by 7 and their sum is $sum")
    )

    def test_valid_task182(self):
        for case in self.valid_cases:
            with self.subTest():
                self.assertEqual(
                    task_182.run_body(case.get('number')), self.template.substitute(**case)
                )

    def test_error_task182(self):
        for case in self.error_cases:
            with self.subTest():
                self.assertRaises(TaskError, task_182.run_body, case)

    def test_one_task182(self):
        self.assertEqual(task_182.run_body(1), "Your sequence contains one element.")
