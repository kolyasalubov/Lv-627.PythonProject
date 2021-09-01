from Tasks.task_555 import task_555


def test_task_555():
    assert task_555.run_body(0) == []
    assert task_555.run_body(1) == [[1]]
    assert task_555.run_body(2) == [[1], [1, 1]]
    assert task_555.run_body(3) == [[1], [1, 1], [1, 2, 1]]
    assert task_555.run_body(8) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1],
                                    [1, 6, 15, 20, 15, 6, 1], [1, 7, 21, 35, 35, 21, 7, 1]]
