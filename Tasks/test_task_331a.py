import pytest
from Tasks.task_331a import task_331a


def test_answer_is_present():
    assert task_331a.run_body(9) == f"a={1}, b={2}, c={2}"
    assert task_331a.run_body(12) == f"a={2}, b={2}, c={2}"
    assert task_331a.run_body(29) == f"a={2}, b={3}, c={4}"
    assert task_331a.run_body(121) == f"a={2}, b={6}, c={9}" or f"a={6}, b={6}, c={7}"
    assert task_331a.run_body(600) == f"a={2}, b={14}, c={20}" or f"a={4}, b={10}, c={22}" or f"a={10}, b={10}, c={20}"


def test_answer_is_absent():
    assert task_331a.run_body(15) == "There is no such a, b and c"
    assert task_331a.run_body(31) == "There is no such a, b and c"
    assert task_331a.run_body(47) == "There is no such a, b and c"
    assert task_331a.run_body(327) == "There is no such a, b and c"
    assert task_331a.run_body(831) == "There is no such a, b and c"


def test_type_error():
    with pytest.raises(TypeError):
        task_331a.run_body("123")
