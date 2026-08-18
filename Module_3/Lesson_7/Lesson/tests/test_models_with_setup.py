from unittest import TestCase

from Module_3.Lesson_7.Lesson.models import Student


class StudentTestCase(TestCase):
    def setUp(self) -> None:
        self.student = Student()

    def test_default_name_is_none(self):
        self.assertIsNone(self.student.name)

    def test_set_invalid_age(self):
        with self.assertRaises(ValueError):
            self.student.set_age(-100)
