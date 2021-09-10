from Tasks.task_330 import task_330


def test_task_330():
    assert task_330.run_body(5) == []
    assert task_330.run_body(6) == []
    assert task_330.run_body(7) == [6]
    assert task_330.run_body(28) == [6]
    assert task_330.run_body(29) == [6, 28]
    assert task_330.run_body(496) == [6, 28]
    assert task_330.run_body(497) == [6, 28, 496]
    assert task_330.run_body(10000) == [6, 28, 496, 8128]
    assert task_330.run_body(100000) == [6, 28, 496, 8128]
