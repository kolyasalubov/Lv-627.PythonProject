from Tasks.task_226 import task_226
from unittest import TestCase
import pytest
from task_error import TaskError


def test_task_226():
    assert task_226.run_body(1, 1) == []
    assert task_226.run_body(345, 234) == [26910, 53820]
    assert task_226.run_body(100, 99) == []
    assert task_226.run_body(10, 10) == [10, 20, 30, 40, 50, 60, 70, 80, 90]


class TestTask226(TestCase):
    def tearDown(self) -> None:
        """ Executed after every test case """
        print("\ntearDown executing after the test case. Result:")

    def test_task_226(self) -> None:
        test1 = task_226.run_body(345, 234)
        self.assertEqual(test1, [26910, 53820])

        with pytest.raises(TypeError):
            task_226.run_body("5", -5)

        test3 = task_226.run_body(1, 1)
        self.assertEqual(test3, [])
        self.assertNotEqual(test3, [1])

        test4 = task_226.run_body(100, 100)
        self.assertEqual(test4, [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 3000, 3100, 3200, 3300, 3400, 3500, 3600, 3700, 3800, 3900, 4000, 4100, 4200, 4300, 4400, 4500, 4600, 4700, 4800, 4900, 5000, 5100, 5200, 5300, 5400, 5500, 5600, 5700, 5800, 5900, 6000, 6100, 6200, 6300, 6400, 6500, 6600, 6700, 6800, 6900, 7000, 7100, 7200, 7300, 7400, 7500, 7600, 7700, 7800, 7900, 8000, 8100, 8200, 8300, 8400, 8500, 8600, 8700, 8800, 8900, 9000, 9100, 9200, 9300, 9400, 9500, 9600, 9700, 9800, 9900])

        test5 = task_226.run_body(10, 10)
        self.assertEqual(test5, [10, 20, 30, 40, 50, 60, 70, 80, 90])

        with pytest.raises(TaskError):
            task_226.run_body(45, -45)
