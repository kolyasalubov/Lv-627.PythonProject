from Tasks.task_108 import task_108
import pytest


def test_small_numbers():
    assert task_108.run_body(1) == 2
    assert task_108.run_body(5) == 2
    assert task_108.run_body(17) == 3


def test_big_numbers():
    assert task_108.run_body(123) == 4
    assert task_108.run_body(1041) == 6
    assert task_108.run_body(123139) == 19


def test_type_error():
    with pytest.raises(TypeError):
        task_108.run_body("123")
