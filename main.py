from task_182 import task_182
from task_323 import task_323
from task_560 import task_560

if __name__ == "__main__":
    tasks_mapper = {
        "182": task_182,
        "323": task_323,
        "560": task_560
    }

    task_name = input("Input number if task\n")
    if task_name in tasks_mapper.keys():
        result = tasks_mapper[task_name]()
        print(result)
    else:
        print("Wrong number")
