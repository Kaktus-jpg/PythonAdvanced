import unittest

from Module_3.Lesson_7.Lesson.hello_world_with_day import app


class TestHelloWorldWithDayApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        app.config["TESTING"] = True
        app.config["DEBUG"] = False
        cls.app = app.test_client()
        cls.base_url: str = "/hello-world/"

    def test_can_get_correct_username_with_weekdate(self):
        username: str = "username"
        response = self.app.get(self.base_url + username)
        response_text: str = response.data.decode()
        self.assertIn(username, response_text)
