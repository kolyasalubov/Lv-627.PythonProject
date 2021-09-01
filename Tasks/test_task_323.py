from Tasks.task_323 import task_323


def test_cases_task323_solve():
    cases = [
        {'number': 16, 'result': [1, 3, 5, 7, 9, 11, 13, 15]},
        {'number': 5, 'result': [1, 2, 3, 4]},
        {'number': 20, 'result': [1, 3, 7, 9, 11, 13, 17, 19]},
    ]
    for case in cases:
        assert task_323.run_body(case.get('number')) == case.get('result')
