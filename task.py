from unittest import TestResult
from typing import Any, Union
from pytest import ExitCode
import pytest
from jsonschema import validate
from algo_handler import AlgoHandler


class Task:
    """
    Task object that is supposed to be inherited from.
    Child classes that implement can run the function stored in
    self.body property and test themselves with pytest or unittest
    stored in self.test property.

    Attributes:
         self.args_schema: jsonschema used to validate arguments with which sef.body is called.
         self.description: a string used to describe the task, later used in end-user interface.
         self.body: function that represents the main logic of the task solution.
         self.body_return_type: body return type.
         self.test: stores pytest/unittest class.
    """

    # Instantiate return_type to mute compiler error that is handled at runtime.
    return_type = Any

    @staticmethod
    def _validate_construction_args(**kwargs) -> None:
        """
        Private method used to validate __init__ arguments.

        Arguments:
            **kwargs: keyword arguments with which __init__ is called.

        Returns:
            None

        Raises:
            TypeError, KeyError: for when validation fails.
        """

        # Check if body has a __call__ property and
        # if test a test file path.

        # If any of mentioned checks fail, raise TypeError.
        if not isinstance(kwargs["name"], str):
            raise TypeError
        if not isinstance(kwargs["description"], str):
            raise TypeError
        if not callable(kwargs["body"]):
            raise TypeError
        if not isinstance(kwargs["test"], str):
            raise TypeError

    def __init__(self, *args, ** kwargs) -> None:
        """
        Standard constructor with basic type checks implemented that also ads the task instance to AlgoHandler.

        Arguments:
            *args: only used for parent class constructor call.
            **kwargs:
                'name': name of the task used to identify it in AlgoHandler.
                'description': a string used to describe the task, later used in end-user interface.
                'body': function that represents the main logic of the task solution.
                'test': stores pytest/unittest class.

        Returns:
            None

        Raises:
            TypeError: invalid construction arguments.
        """

        # Call ABCMeta constructor.
        super(Task, self).__init__()
        # Validate construction arguments.
        self._validate_construction_args(**kwargs)
        # Generate jsonschema from function type hints.
        annotations = kwargs["body"].__annotations__
        self.args_schema = {
            key: annotations[key].__name__ for key in annotations if key != "return"
        }
        # Postprocess to cast python type names to JS type names.
        for key in self.args_schema:
            if self.args_schema[key] in ["int", "float"]:
                self.args_schema[key] = "number"
            if self.args_schema[key] == "str":
                self.args_schema[key] = "string"
        # Save task name.
        self.name = kwargs["name"]
        # Save the description.
        self.description = kwargs["description"]
        # Save function body.
        self.body = kwargs["body"]
        # Return type is extracted from body type hints.
        self.return_type = kwargs["body"].__annotations__["return"]
        self.test = kwargs["test"]

        # Add the task to AlgoHandler.
        handler = AlgoHandler()
        handler.add_task(self)

    def run_body(self, *args, **kwargs) -> return_type:
        """
        Public method used to invoke main task logic.

        Arguments:
            *args, **kwargs: arguments for self.body invocation.

        Returns:
            self.return_type

        Raises:
            ValidationError: invalid arguments.
        """

        # Validate the arguments.
        validate(kwargs, self.args_schema)

        # Invoke the body function with appropriate arguments and return its result.
        return self.body(*args, **kwargs)

    def run_test(self) -> Union[TestResult, ExitCode]:
        """
        Public method used to invoke the tests for the task.

        Arguments: None

        Returns:
            None
        """

        # Invoke the test
        return pytest.main([self.test])
