import unittest

from Module_5.Practical_7.Task_4.main import Redirect


class TestRedirect(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.test_str_stdout = "test stdout"
        cls.test_str_stderr = "test stderr"
        cls.test_stdout_file_path = "test_stdout.txt"
        cls.test_stderr_file_path = "test_stderr.txt"

    def test_redirect(self):

        with (
            open(self.test_stdout_file_path, "w") as test_stdout_file,
            open(self.test_stderr_file_path, "w") as test_stderr_file,
            Redirect(stdout=test_stdout_file, stderr=test_stderr_file),
        ):
            print(self.test_str_stdout)
            raise Exception(self.test_str_stderr)
        with open(self.test_stdout_file_path, "r") as test_stdout_file:
            line = test_stdout_file.readline()
            self.assertEqual(self.test_str_stdout, line.strip())

        with open(self.test_stderr_file_path, "r") as test_stderr_file:
            last_line = test_stderr_file.readlines()[-1]
            self.assertEqual(
                f"{Exception.__name__}: {self.test_str_stderr}", last_line.strip()
            )

    def test_redirect_only_stdout(self):
        with (
            open(self.test_stdout_file_path, "w") as test_stdout_file,
            Redirect(stdout=test_stdout_file),
        ):
            print(self.test_str_stdout)
        with open(self.test_stdout_file_path, "r") as test_stdout_file:
            line = test_stdout_file.readline()
            self.assertEqual(self.test_str_stdout, line.strip())

    def test_redirect_only_stderr(self):
        with (
            open(self.test_stderr_file_path, "w") as test_stderr_file,
            Redirect(stderr=test_stderr_file),
        ):
            raise Exception(self.test_str_stderr)
        with open(self.test_stderr_file_path, "r") as test_stderr_file:
            last_line = test_stderr_file.readlines()[-1]
            self.assertEqual(
                f"{Exception.__name__}: {self.test_str_stderr}", last_line.strip()
            )

    def test_non_redirect(self):
        try:
            with Redirect():
                print(self.test_str_stdout, flush=True)
                raise Exception(self.test_str_stderr)
        except Exception as exc:
            self.fail(exc)


if __name__ == "__main__":
    with open("test_results.txt", "a") as test_file_stream:
        runner = unittest.TextTestRunner(stream=test_file_stream)
        unittest.main(testRunner=runner)
