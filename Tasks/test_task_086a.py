from Tasks.task_086a import task_086a


def test_task_086a():
    assert task_086a.run_body(10) == 2
    assert task_086a.run_body(999) == 3
    assert task_086a.run_body(5) == 1
    assert task_086a.run_body(1575) == 4
    assert task_086a.run_body(2021) == 4
    assert task_086a.run_body(12345) == 5
