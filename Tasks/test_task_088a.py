from Tasks.task_088a import task_088a
import pytest


def test_is_not_digit():
    assert task_088a.run_body(10) == f"3 is not a digit of number {10}^2 = {100}"


def test_is_digit():
    assert task_088a.run_body(19) == f"3 is a digit of number {19}^2 = {361}"


def test_minus_number():
    assert task_088a.run_body(-100) == f"3 is not a digit of number {-100}^2 = {10000}"


def test_type_error():
    with pytest.raises(TypeError):
        task_088a.run_body('s')
