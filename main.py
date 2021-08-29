from algo_handler import AlgoHandler


def main():
    handler = AlgoHandler()
    handler.load_tasks("Tasks")
    handler.tasks["task_113a"].run_test()


if __name__ == '__main__':
    main()
