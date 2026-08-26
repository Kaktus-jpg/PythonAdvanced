from unittest import TestCase

from Module_4.Lesson_4.Homework.flask_wtforms_home import app


class TestHomework(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        app.config["DEBUG"] = False
        app.config["TESTING"] = True
        app.config["WTF_CSRF_ENABLED"] = False
        cls.app = app.test_client()
        cls.base_url = "/registration"

    def test_unfilled_email_form(self):
        data = {
            "phone": 9991234567,
            "name": "Иванов И. И.",
            "address": "На деревню, дедушке",
            "index": 187110,
            "comment": "вход со двора",
        }

        post_request = self.app.post(self.base_url, json=data)
        self.assertEqual(post_request.status_code, 400)

    def test_unfilled_phone_form(self):
        data = {
            "email": "test@example.com",
            "name": "Иванов И. И.",
            "address": "На деревню, дедушке",
            "index": 187110,
            "comment": "вход со двора",
        }

        post_request = self.app.post(self.base_url, json=data)
        self.assertEqual(post_request.status_code, 400)

    def test_unfilled_address_form(self):
        data = {
            "email": "test@example.com",
            "phone": 9991234567,
            "name": "Иванов И. И.",
            "index": 187110,
            "comment": "вход со двора",
        }

        post_request = self.app.post(self.base_url, json=data)
        self.assertEqual(post_request.status_code, 400)

    def test_unfilled_name_form(self):
        data = {
            "email": "test@example.com",
            "phone": 9991234567,
            "address": "На деревню, дедушке",
            "index": 187110,
            "comment": "вход со двора",
        }

        post_request = self.app.post(self.base_url, json=data)
        self.assertEqual(post_request.status_code, 400)

    def test_wrong_phone_form(self):
        data = {
            "email": "test@example.com",
            "phone": 999,
            "name": "Иванов И. И.",
            "address": "На деревню, дедушке",
            "index": 187110,
            "comment": "вход со двора",
        }

        post_request = self.app.post(self.base_url, json=data)
        self.assertEqual(post_request.status_code, 400)

    def test_wrong_name_form(self):
        data = {
            "email": "test@example.com",
            "phone": 9991234567,
            "name": "Иванов Иван",
            "address": "На деревню, дедушке",
            "index": 187110,
            "comment": "вход со двора",
        }

        post_request = self.app.post(self.base_url, json=data)
        self.assertEqual(post_request.status_code, 400)
