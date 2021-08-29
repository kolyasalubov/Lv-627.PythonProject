from singleton import Singleton
from unittest import TestResult
from typing import Any, Union
import importlib
import os


class AlgoHandler(metaclass=Singleton):
    """
    A wrapper for all the tasks that will work as an interface to the
    user, created to make interactions with Task class instances more
    straightforward.

    Attributes:
        self.tasks: contains a dictionary of tasks with their names as keys and values as tasks themselves.
    """

    def __init__(self) -> None:
        self.tasks = {}

    @staticmethod
    def load_tasks(directory_path: str) -> None:
        """
        Compile all task files in order to invoke their instantiation and
        thus record them in AlgoHandler.

        Arguments:
            directory_path: path to the directory where task files are stored.
        """
        
        for file in os.listdir(directory_path):
            if file == "__pycache__":
                continue
            if not (file.startswith("test") or file.endswith("test")):
                importlib.import_module('.'.join([directory_path, file])[:-3])

    def add_task(self, task) -> None:
        """
        Standard constructor with basic type checks implemented.

        Arguments:
            task: task to be added to AlgoHandler.

        Returns:
            None

        Raises:
            TypeError: invalid arguments.
        """

        self.tasks[task.name] = task

    def run_task(self, name: str, *args, **kwargs) -> Any:
        """
        Executes the body function of a Task class instance.

        Arguments:
            name: task name, key in self.tasks.
            *args: standard notation, to avoid any possible errors later.
            **kwargs: named arguments for the function.

        Returns:
            Return type depends on function return type. You can access it in
            self.tasks[name].return_type.
        """

        return self.tasks[name].run_body(*args, **kwargs)

    def run_test(self, name: str) -> Union[TestResult, int]:
        """
        Executed the test bound to a Task class instance.

        Arguments:
            name: task name, key in self.tasks.

        Returns:
            Return type is based on the type of test ran. Depending on whether test is
            a pytest or a unittest, return type can be TestResult or int.
        """

        return self.tasks[name].run_test()
