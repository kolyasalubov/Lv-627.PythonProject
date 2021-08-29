from Tasks.task_113a import task_113a


def test_task_113a():
    assert task_113a.run_body(1) == 1
    assert task_113a.run_body(2) == 2
    assert task_113a.run_body(3) == 3
    assert task_113a.run_body(4) == 8
    assert task_113a.run_body(5) == 15
    assert task_113a.run_body(6) == 48
