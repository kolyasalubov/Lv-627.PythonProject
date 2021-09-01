from Tasks.task_332 import task_332

import pytest


def test_zero():
    assert task_332.run_body(0) == "x = 0, y = 0, z = 0, t = 0"


def test_one_digit():
    assert task_332.run_body(7) == "x = 2, y = 1, z = 1, t = 1"


def test_two_digits():
    assert task_332.run_body(27) == "x = 3, y = 3, z = 3, t = 0"


def test_three_digits():
    assert task_332.run_body(100) == "x = 0, y = 0, z = 0, t = 10"


def test_value_error():
    with pytest.raises(ValueError):
        task_332.run_body(-100)


def test_type_error():
    with pytest.raises(TypeError):
        task_332.run_body('s')