class BlockErrors:
    def __init__(self, exceptions: set):
        self.exceptions = exceptions

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type in self.exceptions:
            return True
        else:
            for exc in self.exceptions:
                if issubclass(exc_type, exc):
                    return True
        raise exc_type(exc_val)
