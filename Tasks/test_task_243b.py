task_243b = lambda x: [x, x^2]
import pytest


def test_body():
    assert task_243b.run_body(20) == (4, 2)
    assert task_243b.run_body(100) == (8, 6)
    assert task_243b.run_body(29) == (5, 2)
    assert task_243b.run_body(45) == (6, 3)


def test_none_result():
    assert not task_243b.run_body(19)
    assert not task_243b.run_body(16)
    assert not task_243b.run_body(28)
    assert not task_243b.run_body(33)

def test_invalid_input():
    with pytest.raises(TypeError):
        task_243b.run_body('b')
