import algo_tasks


def get_task_number():
    """Returns a valid task number"""
    while 1:
        print('List of tasks: {}'.format(sorted(task_mapper.keys())))
        x = input('Please, enter a task number: ')
        if x in task_mapper.keys():
            return x
        print('You have not entered a correct task number. Please, try again.')


if __name__ == "__main__":
    task_mapper = {
        87: algo_tasks.task_87,
        226: algo_tasks.task_226,
        559: algo_tasks.task_559
    }
    while 1:
        num = get_task_number()
        print('The result is: {}.'.format(task_mapper[num]()))
        if input("Press y to continue, any other key to exit: ") != 'y':
            break
