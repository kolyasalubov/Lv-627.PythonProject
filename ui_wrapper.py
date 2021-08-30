from algo_handler import AlgoHandler
from task_error import TaskError


class _TextFormat:
    """
    An inner class used to decorate the text in the console.
    """

    BLUE = '\033[94m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


class UIWrapper:
    """
    A static class that wraps the AlgoHandler and serves as a proxy to create a more
    user-friendly interface that uses basic easily understandable commands
    instead of actual python code.
    """

    @staticmethod
    def main() -> None:
        """
        Method that contains all the actual logic for the UI, such as awaiting for
        user input and handling user requests.
        """

        # Set up the AlgoHandler.
        AlgoHandler.load_tasks("Tasks")
        # Run the function until explicitly broken.
        while True:
            print(
                "\nAvailable registered task names: " +
                _TextFormat.BOLD + _TextFormat.BLUE +
                f'{_TextFormat.END}, {_TextFormat.BOLD + _TextFormat.BLUE}'
                .join(sorted(map(lambda x: x[5:], AlgoHandler().tasks.keys()), key=lambda x: int(x.strip('abcdefg')))) +
                _TextFormat.END +
                "."
            )
            task_name = input(
                "Select a task by entering its name or type " +
                _TextFormat.BOLD + _TextFormat.BLUE +
                "exit" +
                _TextFormat.END +
                " to terminate this app: " +
                _TextFormat.BOLD + _TextFormat.YELLOW
            )
            print(_TextFormat.END, end="")
            if task_name not in [*AlgoHandler().tasks.keys(), "exit"]:
                print("That's an invalid task name, please try again.")
                continue
            if task_name == "exit":
                print("Good bye.")
                break
            print(
                _TextFormat.BOLD + _TextFormat.GREEN +
                AlgoHandler().tasks[task_name].description +
                _TextFormat.END
            )
            action = input(
                "Select an action, type " +
                _TextFormat.BOLD + _TextFormat.BLUE +
                "run" +
                _TextFormat.END +
                " to run the task solution, " +
                _TextFormat.BOLD + _TextFormat.BLUE +
                "test" +
                _TextFormat.END +
                " to run tests bound to it, or " +
                _TextFormat.BOLD + _TextFormat.BLUE +
                "cancel " +
                _TextFormat.END +
                "to select another task: " +
                _TextFormat.BOLD + _TextFormat.YELLOW
            )
            print(_TextFormat.END, end="")
            while action not in ["run", "test", "cancel"]:
                print("That's not a valid action, please ty again.")
                action = input(
                    "Select an action, type " +
                    _TextFormat.BOLD + _TextFormat.BLUE +
                    "run" +
                    _TextFormat.END +
                    " to run the task solution, " +
                    _TextFormat.BOLD + _TextFormat.BLUE +
                    "test" +
                    _TextFormat.END +
                    " to run tests bound to it, or " +
                    _TextFormat.BOLD + _TextFormat.BLUE +
                    "cancel " +
                    _TextFormat.END +
                    "to select another task: " +
                    _TextFormat.BOLD + _TextFormat.YELLOW
                )
                print(_TextFormat.END, end="")
            if action == "cancel":
                print("Task aborted.")
                continue
            if action == "run":
                task_data = AlgoHandler().tasks[task_name].body.__annotations__
                input_kwargs = {}
                if len(task_data) != 1:
                    print("Enter required arguments...")
                else:
                    print("No arguments required.")
                for argument_name in task_data:
                    if argument_name == "return":
                        continue
                    raw_argument = input(
                        f"Enter argument " +
                        _TextFormat.BOLD + _TextFormat.BLUE +
                        argument_name +
                        _TextFormat.END +
                        " of type " +
                        _TextFormat.BOLD + _TextFormat.BLUE +
                        task_data[argument_name].__name__ +
                        _TextFormat.END +
                        ": " +
                        _TextFormat.BOLD + _TextFormat.YELLOW
                    )
                    print(_TextFormat.END, end="")
                    while True:
                        try:
                            converted_argument = task_data[argument_name](raw_argument)
                            break
                        except ValueError:
                            print("Unable to convert given input to target type, please try again.")
                            raw_argument = input(
                                f"Enter argument " +
                                _TextFormat.BOLD + _TextFormat.BLUE +
                                argument_name +
                                _TextFormat.END +
                                " of type " +
                                _TextFormat.BOLD + _TextFormat.BLUE +
                                task_data[argument_name].__name__ +
                                _TextFormat.END +
                                ": " +
                                _TextFormat.BOLD + _TextFormat.YELLOW
                            )
                            print(_TextFormat.END, end="")
                    input_kwargs[argument_name] = converted_argument
                print("Running the task...")
                try:
                    result = AlgoHandler().run_task(
                        name=task_name,
                        **input_kwargs
                    )
                    print(
                        "Task execution successful. Result: " +
                        _TextFormat.BOLD + _TextFormat.GREEN +
                        result.__str__() +
                        _TextFormat.END +
                        "."
                    )
                except TaskError as e:
                    print(
                        "A following exception has occurred during the attempt of running the task: " +
                        _TextFormat.BOLD + _TextFormat.RED +
                        e.message +
                        _TextFormat.END +
                        "."
                    )
            if action == "test":
                AlgoHandler().run_test(task_name)


