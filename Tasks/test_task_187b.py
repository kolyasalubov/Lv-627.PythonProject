from Tasks.task_187b import task_187b
from unittest import TestCase
from task_error import TaskError
import pytest


class TestTask187b(TestCase):

    def test_task_187b(self):
        test1 = task_187b.run_body(1)
        self.assertEqual(test1, 0)

        test2 = task_187b.run_body(10)
        self.assertEqual(test2, 0)

        test3 = task_187b.run_body(1000)
        self.assertEqual(test3, 0)

    def test_errors_task_187b(self):
        with pytest.raises(TaskError):
            task_187b.run_body(-1)

        with pytest.raises(TypeError):
            task_187b.run_body("1")

        with pytest.raises(TaskError):
            task_187b.run_body(0)

print(task_187b.run_body(1))