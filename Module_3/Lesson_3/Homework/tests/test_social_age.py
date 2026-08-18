import unittest

from social_age import get_social_status


class TestSocialAge(unittest.TestCase):
    def test_can_get_child_age(self):
        age = 8
        expected_res = "ребёнок"
        function_res = get_social_status(age)
        self.assertEqual(expected_res, function_res)

    def test_can_get_teen_age(self):
        age = 14
        expected_res = "подросток"
        function_res = get_social_status(age)
        self.assertEqual(expected_res, function_res)

    def test_can_get_adult_age(self):
        age = 34
        expected_res = "взрослый"
        function_res = get_social_status(age)
        self.assertEqual(expected_res, function_res)

    def test_can_get_elderly_age(self):
        age = 52
        expected_res = "пожилой"
        function_res = get_social_status(age)
        self.assertEqual(expected_res, function_res)

    def test_can_get_pensioner_age(self):
        age = 67
        expected_res = "пенсионер"
        function_res = get_social_status(age)
        self.assertEqual(expected_res, function_res)

    def test_cannot_pass_str_as_age(self):
        age = "old"
        with self.assertRaises(TypeError):
            get_social_status(age)

    def test_cannot_pass_negative_age(self):
        age = -3
        with self.assertRaises(ValueError):
            get_social_status(age)
