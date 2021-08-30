from Tasks.task_322 import task_322
import pytest


def test_right_answer():
    assert task_322.run_body() == f"Natural number 9240 has the largest sum of divisors 34560"


def test_type_error():
    with pytest.raises(TypeError):
        task_322.run_body(1)