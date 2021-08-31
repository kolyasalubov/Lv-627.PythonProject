from Tasks.task_088b import task_088b
import pytest


def test_right_answer():
    assert task_088b.run_body(805) == f"Reversed number = {508} "


def test_one_digit():
    assert task_088b.run_body(7) == f"Reversed number = {7} "


def test_value_error():
    with pytest.raises(ValueError):
        task_088b.run_body('819s8189')

