from Tasks.task_088v import task_088v

import pytest


def test_zero():
    assert task_088v.run_body(0) == 0


def test_one_digit():
    assert task_088v.run_body(3) == 3


def test_two_digits():
    assert task_088v.run_body(27) == 72


def test_three_digits():
    assert task_088v.run_body(389) == 983


def test_lots_of_digits():
    assert task_088v.run_body(67249872) == 27249876


def test_value_error():
    with pytest.raises(ValueError):
        task_088v.run_body(-100)
