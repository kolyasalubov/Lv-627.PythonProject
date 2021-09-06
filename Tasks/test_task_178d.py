from Tasks.task_178d import task_178d
from unittest import TestCase
from task_error import TaskError
import pytest


class TestTask178e(TestCase):

    def test_task_178e(self):
        test1 = task_178d.run_body(1)
        self.assertEqual(test1, 0)

        test2 = task_178d.run_body(10)
        self.assertEqual(test2, 0)

        test3 = task_178d.run_body(1000)
        self.assertEqual(test3, 0)

        with pytest.raises(TaskError):
            task_178d.run_body(-1)

        with pytest.raises(TypeError):
            task_178d.run_body("1")

        with pytest.raises(TaskError):
            task_178d.run_body(0)