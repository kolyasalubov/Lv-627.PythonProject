import pytest
from unittest import TestCase

from Tasks.task_330 import task_330
from task_error import TaskError


def test_task_330():
    assert task_330.run_body(5) == []
    assert task_330.run_body(6) == []
    assert task_330.run_body(7) == [6]
    assert task_330.run_body(28) == [6]
    assert task_330.run_body(29) == [6, 28]
    assert task_330.run_body(496) == [6, 28]
    assert task_330.run_body(497) == [6, 28, 496]
    assert task_330.run_body(10000) == [6, 28, 496, 8128]
    assert task_330.run_body(100000) == [6, 28, 496, 8128]


class TestTask330(TestCase):
    def test_task_330(self) -> None:
        test1 = task_330.run_body(2)
        self.assertEqual(test1, [])

        with pytest.raises(TaskError):
            task_330.run_body(0)

        test3 = task_330.run_body(6)
        self.assertEqual(test3, [])
        self.assertNotEqual(test3, [6])

        test4 = task_330.run_body(7)
        self.assertEqual(test4, [6])

        test5 = task_330.run_body(29)
        self.assertEqual(test5, [6, 28])

        test6 = task_330.run_body(99999)
        self.assertEqual(test6, [6, 28, 496, 8128])

        with pytest.raises(TypeError):
            task_330.run_body("six")

        with pytest.raises(TaskError):
            task_330.run_body(-456)

        with pytest.raises(TaskError):
            task_330.run_body(0)
