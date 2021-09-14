from Tasks.task_559 import task_559
from unittest import TestCase
import pytest
from task_error import TaskError


def test_task_559():
    assert task_559.run_body(2) == []
    assert task_559.run_body(3) == []
    assert task_559.run_body(5) == [3]
    assert task_559.run_body(7) == [3]
    assert task_559.run_body(8) == [3, 7]
    assert task_559.run_body(14) == [3, 7]
    assert task_559.run_body(34) == [3, 7, 31]


class TestTask559(TestCase):
    def tearDown(self) -> None:
        """ Executed after every test case """
        print("\ntearDown executing after the test case. Result:")

    def test_task_559(self) -> None:
        test1 = task_559.run_body(2)
        self.assertEqual(test1, [])

        with pytest.raises(TaskError):
            task_559.run_body(0)

        test3 = task_559.run_body(485)
        self.assertEqual(test3, [3, 7, 31, 127])
        self.assertNotEqual(test3, [])

        test4 = task_559.run_body(14)
        self.assertEqual(test4, [3, 7])

        test5 = task_559.run_body(34)
        self.assertEqual(test5, [3, 7, 31])

        with pytest.raises(TypeError):
            task_559.run_body("six")

        with pytest.raises(TaskError):
            task_559.run_body(-456)
