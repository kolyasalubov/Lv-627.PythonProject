class Task:
    def __init__(self):
        self.arg = 1
        self.description = "This is a base class for all tasks. You shouldn't see this."
        self.require_input = True


    def change_arguments(self, arg):
        self.arg = arg

    def validate(self):
        if isinstance(self.arg, int) and self.arg >= 0:
            return True
        else:
            return False

    def solve(self):
        pass
