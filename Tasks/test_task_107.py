task_107 = lambda x: x^2
import pytest


def test_body():
    assert task_107.run_body(20) == 2
    assert task_107.run_body(80) == 3
    assert task_107.run_body(2000) == 5
    assert task_107.run_body(16000) == 6


def test_invalid_input():
    with pytest.raises(TypeError):
        task_107.run_body('b')
