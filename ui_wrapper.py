from algo_handler import AlgoHandler


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
            print(f"Available registered task names: {' '.join(list(AlgoHandler().tasks.keys()))}")
            task_name = input("Select a task by entering its name or type 'exit' to terminate this app: ")
            if task_name not in [*AlgoHandler().tasks.keys(), "exit"]:
                print("That's an invalid task name, please try again.")
                continue
            if task_name == "exit":
                print("Good bye.")
                break
            action = input("Select an action, type 'run' to run the task solution, "
                           "'test' to run rests bound to it, "
                           "or 'cancel' to select another task: ")
            while action not in ["run", "test", "cancel"]:
                print("That's not a valid action, please ty again.")
                action = input("Select an action, type 'run' to run the task solution, "
                               "'test' to run rests bound to it, "
                               "or 'cancel' to select another task: ")
            if action == "cancel":
                print("Task aborted.")
                continue
            if action == "run":
                pass
            if action == "test":
                pass


