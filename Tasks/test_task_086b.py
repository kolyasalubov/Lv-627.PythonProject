import pytest
from unittest import TestCase

from Tasks.task_086b import task_086b
from task_error import TaskError


def test_task_086a():
    assert task_086b.run_body(10) == 1
    assert task_086b.run_body(999) == 27
    assert task_086b.run_body(5) == 5
    assert task_086b.run_body(1575) == 18
    assert task_086b.run_body(2021) == 5
    assert task_086b.run_body(12345) == 15


class TestTask086b(TestCase):
    def tearDown(self) -> None:
        """ Executed after every test case """
        print("\ntearDown executing after the test case. Result:")

    def test_task_559(self) -> None:
        test1 = task_086b.run_body(2)
        self.assertEqual(test1, 2)

        with pytest.raises(TaskError):
            task_086b.run_body(0)

        test3 = task_086b.run_body(485)
        self.assertEqual(test3, 17)
        self.assertNotEqual(test3, 3)

        test4 = task_086b.run_body(14)
        self.assertEqual(test4, 5)

        test5 = task_086b.run_body(3444)
        self.assertEqual(test5, 15)

        with pytest.raises(TypeError):
            task_086b.run_body("six")

        with pytest.raises(TaskError):
            task_086b.run_body(-456)
