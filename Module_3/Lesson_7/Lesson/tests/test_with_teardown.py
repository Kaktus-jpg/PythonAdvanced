import time
from unittest import TestCase


class PerformanceTest(TestCase):
    def setUp(self) -> None:
        self.start = time.perf_counter()

    def tearDown(self) -> None:
        self.end = time.perf_counter()
        print(self.id(), self.end - self.start)

    def test_million_appends(self):
        N = 1_000_000
        lst = []
        for i in range(N):
            lst.append(i)
        self.assertListEqual(lst, list(range(N)))
