class Singleton(type):
    """
    Standard singleton metaclass.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        # Check if class instance already exists and if it doesnt,
        # create one and record in in _instances set.
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
