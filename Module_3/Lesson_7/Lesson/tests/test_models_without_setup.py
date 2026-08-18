from unittest import TestCase

from Module_3.Lesson_7.Lesson.models import Student


class StudentTestCase(TestCase):
    def test_default_name_is_none(self):
        student = Student()
        self.assertIsNone(student.name)

    def test_set_invalid_age(self):
        student = Student()
        with self.assertRaises(ValueError):
            student.set_age(-100)
