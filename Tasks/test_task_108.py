import pytest
from Tasks.task_108 import task_108


def test_small_numbers():
    assert task_108.run_body(1) == 2
    assert task_108.run_body(5) == 3
    assert task_108.run_body(17) == 5


def test_big_numbers():
    assert task_108.run_body(123) == 12
    assert task_108.run_body(1041) == 33
    assert task_108.run_body(123139) == 351


def test_type_error():
    with pytest.raises(TypeError):
        task_108.run_body("123")
