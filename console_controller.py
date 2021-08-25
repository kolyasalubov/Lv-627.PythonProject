import volodymyr_solutions


class ConsoleController:
    def __init__(self):
        self.tasks = {
            "108": volodymyr_solutions.Task108(),
            "331": volodymyr_solutions.Task331()
        }


    def work_with_task(self, task):
        print(task.description)
        inp = input("Provide input value/s ").split()
        try:
            task.change_arguments(*map(lambda x: int(x), inp))
        except (TypeError, ValueError):
            print("Your value/s is/are incorrect. Try again.")
            self.work_with_task(task)
        else:
            if task.validate():
                print(f"Solution is {task.solve()}")
            else:
                print("Your value/s is/are incorrect. Try again.")
                self.work_with_task(task)

    def run(self):
        print(f"Hello! This is the console solver for many mathematical tasks.\nHere is the list of available tasks:")
        print('\n'.join(self.tasks))
        task = input("Which task would you like to view? ")
        if task in self.tasks:
            self.work_with_task(self.tasks[task])
            self.run()
        else:
            print("There's no such task :/")
            self.run()


if __name__ == "__main__":
    ConsoleController().run()