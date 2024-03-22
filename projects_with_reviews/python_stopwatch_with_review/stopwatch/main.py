"""
This file should NOT be reviewed. Its only purpose is to showcase the
functionality of the stopwatch program. In what follows, a brief
specification of the program is provided:

A stopwatch is useful for timing the duration of a task. This program
provides methods for starting, stopping, suspending, resuming, splitting,
unsplitting and resetting a stopwatch. More specifically, these methods do
the following:

    - Start: The stopwatch starts measuring time.
    - Stop: The stopwatch stops measuring time and the timing session ends.
    - Split: The time since the stopwatch started is recorded while the
      stopwatch continues measuring time.
    - Unsplit: This method removes the effect of the split.
    - Suspend: This method pauses the stopwatch.
    - Resume: This method makes the stopwatch to continue measuring time.
    - Reset: This method resets the stopwatch to its initial state.

The following scenarios are not allowed (an exception is thrown):

    - Stop is called before start.
    - Resume is called before suspend.
    - Unsplit is called before split.
    - Start is called twice without calling reset.
    - Split, suspend or stop are called twice.
"""


from StopWatch import StopWatch
import time


def main():
    # Create a new StopWatch instance
    stop_watch = StopWatch("My StopWatch")
    # Print the name of the StopWatch and whether it is running (should be false)
    print("StopWatch name: " + stop_watch.get_message() + ", is running: " + str(stop_watch.is_started()))
    # Start the StopWatch
    stop_watch.start()
    # Print the name of the StopWatch and whether it is running (should be true)
    print("StopWatch name: " + stop_watch.get_message() + ", is running: " + str(stop_watch.is_started()))
    # Wait for 1 second
    time.sleep(1)
    # Split the StopWatch
    stop_watch.split()
    # Wait for 1 second
    time.sleep(1)
    # Prints the total time and the split time
    print("Total time: " + str(stop_watch.get_time()) + ", split time: " + str(stop_watch.get_split_time()))
    # Stop the StopWatch
    stop_watch.stop()
    # Print the elapsed time
    print("Elapsed time: " + str(stop_watch.get_time()))


if __name__ == "__main__":
    main()
