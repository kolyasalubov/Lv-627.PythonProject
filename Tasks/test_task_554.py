from Tasks.task_554 import task_554
from unittest import TestCase
import pytest
from task_error import TaskError


def test_task_554():
    assert task_554.run_body(3) == []
    assert task_554.run_body(5) == []
    assert task_554.run_body(7) == [(3, 4, 5)]
    assert task_554.run_body(8) == [(3, 4, 5)]
    assert task_554.run_body(12) == [(3, 4, 5), (6, 8, 10)]
    assert task_554.run_body(15) == [(3, 4, 5), (6, 8, 10), (5, 12, 13)]
    assert task_554.run_body(20) == [(3, 4, 5), (6, 8, 10), (5, 12, 13), (9, 12, 15), (8, 15, 17)]



class TestTask554(TestCase):
    def test_task_554(self):
        test1 = task_554.run_body(3)
        self.assertEqual(test1, [])

        test2 = task_554.run_body(7)
        self.assertEqual(test2, [(3, 4, 5)])

        test3 = task_554.run_body(15)
        self.assertEqual(test3, [(3, 4, 5), (6, 8, 10), (5, 12, 13)])

    def test_errors_task_554(self):
        #with pytest.raises(TaskError):
          #  task_554.run_body(-1)

        with pytest.raises(TypeError):
            task_554.run_body("1")

        #with pytest.raises(TaskError):
         #   task_554.run_body(0)



