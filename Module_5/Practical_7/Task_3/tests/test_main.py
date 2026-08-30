import unittest
from unittest import TestCase

from Module_5.Practical_7.Task_3.main import BlockErrors


class TestBlockErrors(TestCase):
    def test_1(self):
        err_types = {ZeroDivisionError, TypeError}
        with BlockErrors(err_types):
            a = 1 / 0

    def test_2(self):
        with self.assertRaises(TypeError):
            err_types = {ZeroDivisionError}
            with BlockErrors(err_types):
                a = 1 / "0"

    def test_3(self):
        outer_err_types = {TypeError}
        with BlockErrors(outer_err_types):
            inner_err_types = {ZeroDivisionError}
            with BlockErrors(inner_err_types):
                a = 1 / "0"

    def test_4(self):
        err_types = {Exception}
        with BlockErrors(err_types):
            a = 1 / "0"

    def test_5(self):
        with self.assertRaises(ZeroDivisionError), BlockErrors({TypeError}):
            a = 1 / 0

    def test_6(self):
        try:
            with BlockErrors({ZeroDivisionError}):
                a = 1 / 0
        except Exception as exc:
            self.fail(exc)


if __name__ == "__main__":
    unittest.main()
