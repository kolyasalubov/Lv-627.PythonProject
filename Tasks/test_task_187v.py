from Tasks.task_187b import task_187b
from unittest import TestCase
from task_error import TaskError
import pytest


class TestTask187b(TestCase):

    def test_task_187b(self):
        test1 = task_187b.run_body([1,4,15,45,300,58,75])
        self.assertEqual(test1, 1)

        test2 = task_187b.run_body([16,4,5,25,78])
        self.assertEqual(test2, 2)

        test3 = task_187b.run_body([16,4,5,25,78,36])
        self.assertEqual(test3, 3)

    def test_errors_task_187b(self):
        with pytest.raises(TaskError):
            task_187b.run_body([])
