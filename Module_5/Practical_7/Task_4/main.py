import sys
import traceback


class Redirect:
    def __init__(self, stdout=None, stderr=None):
        self.cur_stdout = sys.stdout
        self.cur_stderr = sys.stderr
        self.new_stdout = stdout
        self.new_stderr = stderr

    def __enter__(self):
        if self.new_stdout is not None:
            sys.stdout = self.new_stdout
        if self.new_stderr is not None:
            sys.stderr = self.new_stderr

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            sys.stderr.write(traceback.format_exc())

        sys.stdout = self.cur_stdout
        sys.stderr = self.cur_stderr

        return True
