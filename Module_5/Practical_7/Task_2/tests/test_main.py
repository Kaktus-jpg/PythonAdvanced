import unittest
from unittest import TestCase

from Module_5.Practical_7.Task_2.main import app


class TestMain(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        app.config["WTF_CSRF_ENABLED"] = False
        app.config["DEBUG"] = False
        app.config["TESTING"] = True
        cls.app = app.test_client()
        cls.base_url = "/run-program/"

    def setUp(self) -> None:
        self.data = {
            "code": 'print("hello")',
            "timeout": 1,
        }

    def test_timeout_lower_than_execute_time(self):
        self.data["code"] = "import time\ntime.sleep(2)"
        post_request = self.app.post(self.base_url, json=self.data)
        self.assertEqual(post_request.status_code, 400)

    def test_wrong_data_in_form(self):
        self.data["timeout"] = "one"
        post_request = self.app.post(self.base_url, json=self.data)
        self.assertEqual(post_request.status_code, 400)

    def test_insecure_code(self):
        self.data["code"] = """
        from subprocess import run
        run(['./kill_the_system.sh'])
        """
        post_request = self.app.post(self.base_url, json=self.data)
        self.assertEqual(post_request.status_code, 400)


if __name__ == "__main__":
    unittest.main()
