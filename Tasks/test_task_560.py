from Tasks.task_560 import task_560, find_sum_of_divisors


def test_task560_find_sum_of_divisors():
    cases = [
        {'number': 5, 'sum': 1},
        {'number': 4, 'sum': 3},
        {'number': 14, 'sum': 10},
        {'number': 37, 'sum': 1},
        {'number': 217, 'sum': 39},
    ]
    for case in cases:
        assert find_sum_of_divisors(case.get('number')) == case.get('sum')


def test_task560():
    assert task_560.run_body() == (220, 284)



