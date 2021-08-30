from Tasks.task_086b import task_086b


def test_task_086a():
    assert task_086b.run_body(10) == 1
    assert task_086b.run_body(999) == 27
    assert task_086b.run_body(5) == 5
    assert task_086b.run_body(1575) == 18
    assert task_086b.run_body(2021) == 5
    assert task_086b.run_body(12345) == 15
