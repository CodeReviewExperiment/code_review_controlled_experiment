import time


class StopWatch:
    """
    A simple stopwatch utility class that provides methods to measure elapsed time.

    Attributes:
        MILLIS_2_NANO (int): Constant to convert nanoseconds to milliseconds.
    """

    MILLIS_2_NANO = 1000000

    class State:
        """Enumeration for stopwatch states."""
        UNSTARTED = 0
        RUNNING = 1
        STOPPED = 2
        SUSPENDED = 3

    class SplitState:
        """Enumeration for split states of the stopwatch."""
        SPLIT = 0
        UNSPLIT = 1

    def __init__(self, message=None):
        """
        Initialize a new instance of the StopWatch class.

        :param message: A message or name for the stopwatch.
        :type message: str, optional
        """
        self.message = message
        self.running_state = self.State.UNSTARTED
        self.split_state = self.SplitState.UNSPLIT
        self.start_time_nanos = 0
        self.start_time_millis = 0
        self.stop_time_nanos = 0
        self.stop_time_millis = 0

    @staticmethod
    def create():
        """
        Initialize a new instance of the StopWatch class.

        :param message: A message or name for the stopwatch.
        :type message: str, optional
        """
        return StopWatch()

    @staticmethod
    def create_started():
        """
        Create and start a new StopWatch instance.

        :return: A started StopWatch instance.
        :rtype: StopWatch
        """
        sw = StopWatch()
        sw.start()
        return sw

    def get_message(self):
        """
        Return the message associated with the StopWatch.

        :return: The message of the stopwatch.
        :rtype: str
        """
        return self.message

    def get_nano_time(self):
        """
        Return the elapsed time in nanoseconds.

        :return: Elapsed time in nanoseconds.
        :rtype: int
        :raises ValueError: If the stopwatch is in an illegal state.
        """
        if self.running_state in [self.State.STOPPED, self.State.SUSPENDED]:
            return self.stop_time_nanos - self.start_time_nanos
        if self.running_state == self.State.UNSTARTED:
            return 0
        if self.running_state == self.State.RUNNING:
            return time.time_ns() - self.start_time_nanos
        raise ValueError("Illegal running state has occurred.")

    def get_split_nano_time(self):
        """
        Returns the split time in nanoseconds.

        :return: Split time in nanoseconds.
        :rtype: int
        :raises ValueError: If the stopwatch has not been split.
        """
        if self.split_state != self.SplitState.SPLIT:
            raise ValueError("Stopwatch must be split to get the split time.")
        return self.stop_time_nanos - self.start_time_nanos

    def get_split_time(self):
        """
        Returns the split time in milliseconds.

        :return: Split time in milliseconds.
        :rtype: str
        """
        return self.nanos_to_millis(self.get_split_nano_time())

    def get_start_time(self):
        """
        Returns the start time of the stopwatch in milliseconds.

        :return: Start time in milliseconds.
        :rtype: int
        :raises ValueError: If the stopwatch has not been started.
        """
        if self.running_state == self.State.UNSTARTED:
            raise ValueError("Stopwatch has not been started")
        return self.start_time_millis

    def get_stop_time(self):
        """
        Returns the stop time of the stopwatch in milliseconds.

        :return: Stop time in milliseconds.
        :rtype: int
        :raises ValueError: If the stopwatch has not been started.
        """
        if self.running_state == self.State.UNSTARTED:
            raise ValueError("Stopwatch has not been started")
        return self.stop_time_millis

    def get_time(self):
        """
        Returns the total elapsed time of the stopwatch in milliseconds.

        :return: Elapsed time in milliseconds.
        :rtype: int
        """
        return self.nanos_to_millis(self.get_nano_time())

    def is_started(self):
        """
        Checks if the stopwatch is started.

        :return: True if the stopwatch is running, False otherwise.
        :rtype: bool
        """
        return self.running_state == self.State.RUNNING

    def is_stopped(self):
        """
        Checks if the stopwatch is stopped.

        :return: True if the stopwatch is stopped, False otherwise.
        :rtype: bool
        """
        return self.running_state == self.State.STOPPED

    def is_suspended(self):
        """
        Checks if the stopwatch is suspended.

        :return: True if the stopwatch is suspended, False otherwise.
        :rtype: bool
        """
        return self.running_state == self.State.SUSPENDED

    @staticmethod
    def nanos_to_millis(nanos):
        """
        Converts nanoseconds to milliseconds.

        :param nanos: Time in nanoseconds to convert.
        :type nanos: int
        :return: Time in milliseconds.
        :rtype: int
        """
        return nanos // StopWatch.MILLIS_2_NANO

    def reset(self):
        """
        Resets the stopwatch. This method stops the stopwatch and resets all times to zero.
        """
        self.running_state = self.State.UNSTARTED
        self.split_state = self.SplitState.UNSPLIT

    def resume(self):
        """
        Resumes the stopwatch from a suspended state.

        :raises ValueError: If the stopwatch is not suspended.
        """
        if self.running_state != self.State.SUSPENDED:
            raise ValueError("Stopwatch must be suspended to resume.")
        self.start_time_nanos += time.time_ns() - self.stop_time_nanos
        self.running_state = self.State.RUNNING

    def split(self):
        """
        Splits the time. This method sets the stop time of the watch to allow a time to be extracted.

        :raises ValueError: If the stopwatch is not running.
        """
        if self.running_state != self.State.RUNNING:
            raise ValueError("Stopwatch is not running.")
        self.stop_time_nanos = time.time_ns()
        self.split_state = self.SplitState.SPLIT

    def start(self):
        """
        Starts the stopwatch.

        :raises ValueError: If the stopwatch is already running or has been stopped without being reset.
        """
        if self.running_state == self.State.RUNNING:
            raise ValueError("Stopwatch must be reset before being restarted.")
        if self.running_state == self.State.STOPPED:
            raise ValueError("Stopwatch must be reset before being restarted.")
        self.start_time_nanos = time.time_ns()
        self.start_time_millis = int(time.time() * 1000)
        self.running_state = self.State.RUNNING

    def stop(self):
        """
        Stops the stopwatch.

        :raises ValueError: If the stopwatch is not running or suspended.
        """
        if self.running_state  != self.State.RUNNING:
            if self.running_state  != self.State.SUSPENDED:
                raise ValueError("Stopwatch is not running.")
        if self.running_state == self.State.RUNNING:
            self.stop_time_nanos = time.time_ns()
            self.stop_time_millis = int(time.time() * 1000)
        self.running_state = self.State.STOPPED

    def suspend(self):
        """
        Suspends the stopwatch for later resumption.

        :raises ValueError: If the stopwatch is not currently running.
        """
        if self.running_state != self.State.RUNNING:
            raise ValueError("Stopwatch must be running to suspend.")
        self.stop_time_nanos = time.time_ns()
        self.stop_time_millis = int(time.time() * 1000)
        self.running_state = self.State.SUSPENDED

    def unsplit(self):
        """
        Removes a split. This method clears the stop time.

        :raises ValueError: If the stopwatch has not been split.
        """
        if self.split_state != self.SplitState.SPLIT:
            raise ValueError("Stopwatch has not been split.")
        self.split_state = self.SplitState.UNSPLIT
