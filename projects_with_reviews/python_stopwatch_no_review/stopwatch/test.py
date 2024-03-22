from time import sleep
from unittest import TestCase
from StopWatch import StopWatch


class TestStopWatch(TestCase):
    """
    This file should NOT be reviewed, nor should your code review comments
    revolve around including more tests. However, feel free to run the
    tests or to include more, e.g., to understand how the program works
    or to verify certain program functionality.
    """

    def test_get_message(self):
        self.assertIsNone(StopWatch().get_message())
        message = "test"
        self.assertEqual(message, StopWatch(message).get_message())

    def test_get_nano_time(self):
        watch = StopWatch()
        watch.start()
        self.assertGreater(watch.get_nano_time(), 0)

    def test_get_split_nano_time(self):
        watch = StopWatch()
        watch.start()
        sleep(1)
        watch.split()
        self.assertGreater(watch.get_split_nano_time(), 0)

    def test_get_start_time(self):
        watch = StopWatch()
        watch.start()
        self.assertGreater(watch.get_start_time(), 0)

    def test_get_stop_time(self):
        watch = StopWatch()
        watch.start()
        sleep(1)
        watch.suspend()
        self.assertGreater(watch.get_stop_time(), 0)
