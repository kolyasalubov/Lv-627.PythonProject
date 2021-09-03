from unittest import TestCase
import pytest
from Tasks.task_086a import task_086a
from task_error import TaskError


def test_task_086a():
    assert task_086a.run_body(10) == 2
    assert task_086a.run_body(999) == 3
    assert task_086a.run_body(5) == 1
    assert task_086a.run_body(1575) == 4
    assert task_086a.run_body(2021) == 4
    assert task_086a.run_body(12345) == 5


class TestTask086a(TestCase):
    def test_task_330(self) -> None:
        test1 = task_086a.run_body(2)
        self.assertEqual(test1, 1)

        with pytest.raises(TaskError):
            task_086a.run_body(0)

        test3 = task_086a.run_body(485)
        self.assertEqual(test3, 3)
        self.assertNotEqual(test3, 2)

        test4 = task_086a.run_body(14)
        self.assertEqual(test4, 2)

        test5 = task_086a.run_body(3444)
        self.assertEqual(test5, 4)

        with pytest.raises(TypeError):
            task_086a.run_body("six")

        with pytest.raises(TaskError):
            task_086a.run_body(-456)

        with pytest.raises(TaskError):
            task_086a.run_body(0)
