import pytest
from Tasks.task_331b import task_331b


def test_answer_is_present():
    assert task_331b.run_body(9) == "(1, 2, 2)"
    assert task_331b.run_body(12) == "(2, 2, 2)"
    assert task_331b.run_body(29) == "(2, 3, 4)"
    assert task_331b.run_body(121) == "(2, 6, 9)\n(6, 6, 7)"
    assert task_331b.run_body(600) == "(2, 14, 20)\n(4, 10, 22)\n(10, 10, 20)"


def test_answer_is_absent():
    assert task_331b.run_body(15) == ""
    assert task_331b.run_body(31) == ""
    assert task_331b.run_body(47) == ""
    assert task_331b.run_body(327) == ""
    assert task_331b.run_body(831) == ""


def test_type_error():
    with pytest.raises(TypeError):
        task_331b.run_body("123")
