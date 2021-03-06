from Tasks.task_243a import task_243a
import pytest


def test_body():
    assert task_243a.run_body(20) == (4, 2)
    assert task_243a.run_body(100) == (8, 6)
    assert task_243a.run_body(29) == (5, 2)
    assert task_243a.run_body(45) == (6, 3)


def test_none_result():
    assert task_243a.run_body(19) == "There is no pair of such x, y"
    assert task_243a.run_body(16) == "There is no pair of such x, y"
    assert task_243a.run_body(28) == "There is no pair of such x, y"
    assert task_243a.run_body(33) == "There is no pair of such x, y"

def test_invalid_input():
    with pytest.raises(TypeError):
        task_243a.run_body('b')
