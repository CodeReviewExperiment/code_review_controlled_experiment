package org.crprojects;

/**
 * This file should NOT be reviewed. Its only purpose is to showcase the
 * functionality of the stopwatch program. In what follows, a brief
 * specification of the program is provided:
 *
 * A stopwatch is useful for timing the duration of a task. This program
 * provides methods for starting, stopping, suspending, resuming, splitting,
 * unsplitting and resetting a stopwatch. More specifically, these methods do
 * the following:
 *
 *     - Start: The stopwatch starts measuring time.
 *     - Stop: The stopwatch stops measuring time and the timing session ends.
 *     - Split: The time since the stopwatch started is recorded while the
 *       stopwatch continues measuring time.
 *     - Unsplit: This method removes the effect of the split.
 *     - Suspend: This method pauses the stopwatch.
 *     - Resume: This method makes the stopwatch to continue measuring time.
 *     - Reset: This method resets the stopwatch to its initial state.
 *
 * The following scenarios are not allowed (an exception is thrown):
 *
 *     - Stop is called before start.
 *     - Resume is called before suspend.
 *     - Unsplit is called before split.
 *     - Start is called twice without calling reset.
 *     - Split, suspend or stop are called twice.
 */
public class Main {

    /**
     * Main method showcasing basic usage patterns of the StopWatch class.
     */
    public static void main(String[] args) throws InterruptedException {
        // Create a new StopWatch instance
        StopWatch stopWatch = new StopWatch("My StopWatch");
        // Print the name of the StopWatch and whether it is running (should be false)
        System.out.println("StopWatch name: " + stopWatch.getMessage() + ", is running: " + stopWatch.isStarted());
        // Start the StopWatch
        stopWatch.start();
        // Print the name of the StopWatch and whether it is running (should be true)
        System.out.println("StopWatch name: " + stopWatch.getMessage() + ", is running: " + stopWatch.isStarted());
        // Wait for 1 second
        Thread.sleep(1000);
        // Split the StopWatch
        stopWatch.split();
        // Wait for 1 second
        Thread.sleep(1000);
        // Prints the total time and the split time
        System.out.println("Total time: " + stopWatch.getTime() + ", split time: " + stopWatch.getSplitTime());
        // Stop the StopWatch
        stopWatch.stop();
        // Print the elapsed time
        System.out.println("Elapsed time: " + stopWatch.getTime());
    }
}
