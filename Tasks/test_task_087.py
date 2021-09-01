from unittest import TestCase
from Tasks.task_087 import task_087
import pytest
from task_error import TaskError


def test_task_087():
    assert task_087.run_body(123456, 3) == 15
    assert task_087.run_body(100000, 5) == 0
    assert task_087.run_body(48565834, 8) == 43
    assert task_087.run_body(123, 2) == 5
    with pytest.raises(TypeError):
        task_087.run_body(100000, "six")


class TestTask087(TestCase):
    def tearDown(self) -> None:
        """ Executed after every test case """
        print("\ntearDown executing after the test case. Result:")

    def test_task_087(self) -> None:
        test1 = task_087.run_body(123456, 3)
        self.assertEqual(test1, 15)

        with pytest.raises(TaskError):
            task_087.run_body(100000, -5)

        test3 = task_087.run_body(485658034, 8)
        self.assertEqual(test3, 39)
        self.assertNotEqual(test3, 43)

        test4 = task_087.run_body(123, 2)
        self.assertEqual(test4, 5)

        with pytest.raises(TypeError):
            task_087.run_body(100000, "six")
