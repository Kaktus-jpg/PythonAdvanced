import unittest

from Module_3.Lesson_3.Lesson.social_age import get_social_status


class TestSocialAge(unittest.TestCase):
    def test_can_get_child_age(self):
        age = 8
        expected_res = "ребёнок"
        function_res = get_social_status(age)
        self.assertEqual(expected_res, function_res)

    def test_cannot_pass_str_as_age(self):
        age = "old"
        with self.assertRaises(TypeError):
            get_social_status(age)
