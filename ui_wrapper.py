from algo_handler import AlgoHandler
from task_error import TaskError

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
            print(f"\nAvailable registered task names: {', '.join(list(AlgoHandler().tasks.keys()))}.")
            task_name = input("Select a task by entering its name or type 'exit' to terminate this app: ")
            if task_name not in [*AlgoHandler().tasks.keys(), "exit"]:
                print("That's an invalid task name, please try again.")
                continue
            if task_name == "exit":
                print("Good bye.")
                break
            action = input("Select an action, type 'run' to run the task solution, "
                           "'test' to run tests bound to it, "
                           "or 'cancel' to select another task: ")
            while action not in ["run", "test", "cancel"]:
                print("That's not a valid action, please ty again.")
                action = input("Select an action, type 'run' to run the task solution, "
                               "'test' to run tests bound to it, "
                               "or 'cancel' to select another task: ")
            if action == "cancel":
                print("Task aborted.")
                continue
            if action == "run":
                task_data = AlgoHandler().tasks[task_name].body.__annotations__
                input_kwargs = {}
                print("Enter required arguments...")
                for argument_name in task_data:
                    if argument_name == "return":
                        continue
                    raw_argument = input(
                        f"Enter argument '{argument_name}' (of type {task_data[argument_name].__name__}): "
                    )
                    while True:
                        try:
                            converted_argument = task_data[argument_name](raw_argument)
                            break
                        except ValueError:
                            print("Unable to convert given input to target type, please try again.")
                            raw_argument = input(
                                f"Enter argument '{argument_name}' (of type {task_data[argument_name].__name__}): "
                            )
                    input_kwargs[argument_name] = converted_argument
                print("Running the task...")
                try:
                    result = AlgoHandler().run_task(
                        name=task_name,
                        **input_kwargs
                    )
                    print("Task execution successful.")
                    print(f"Result of task {task_name}: {result}.")
                except TaskError as e:
                    print(f"A following exception has occurred during the attempt of running the task: {e}.")
            if action == "test":
                pass


