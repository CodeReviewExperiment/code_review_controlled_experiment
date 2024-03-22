package org.crprojects;


import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.concurrent.TimeUnit;

import static org.junit.jupiter.api.Assertions.*;

/**
 * This file should NOT be reviewed, nor should your code review comments
 * revolve around including more tests. However, feel free to run the
 * tests or to include more, e.g., to understand how the program works
 * or to verify certain program functionality.
 */
public class StopWatchTest {

    private StopWatch stopWatch;
    private static final String MESSAGE = "Default StopWatch";

    @BeforeEach
    public void setUp() {
        stopWatch = new StopWatch(MESSAGE);
    }

    @Test
    public void createTest() {
        assertFalse(StopWatch.create().isStarted());
    }

    @Test
    public void createStartedTest() {
        assertTrue(StopWatch.createStarted().isStarted());
    }

    @Test
    public void getMessageTest() {
        assertEquals(MESSAGE, stopWatch.getMessage());
    }

    @Test
    public void getNanoTimeTest() {
        assertEquals(0, stopWatch.getNanoTime());
    }

    @Test
    public void getSplitNanoTimeTest() {
        assertThrows(RuntimeException.class, () -> stopWatch.getSplitNanoTime());
        stopWatch.start();
        stopWatch.split();
        assertTrue(stopWatch.getSplitNanoTime() > 0);
    }

    @Test
    public void getSplitTimeTest() {
        assertThrows(RuntimeException.class, () -> stopWatch.getSplitTime());
        stopWatch.start();
        stopWatch.split();
        assertTrue(stopWatch.getSplitTime() >= 0);
    }

    @Test
    public void getStartTimeTest() {
        assertThrows(RuntimeException.class, () -> stopWatch.getStartTime());
        stopWatch.start();
        assertTrue(stopWatch.getStartTime() > 0);
    }

    @Test
    public void getStopTimeTest() {
        assertThrows(RuntimeException.class, () -> stopWatch.getStopTime());
        stopWatch.start();
        stopWatch.stop();
        assertTrue(stopWatch.getStopTime() > 0);
    }

    @Test
    public void getTimeTest() {
        assertEquals(0, stopWatch.getTime());
    }

    @Test
    public void getTimeInTimeUnitsTest() {
        assertEquals(0, stopWatch.getTime(TimeUnit.NANOSECONDS));
    }

    @Test
    public void isStartedTest() {
        assertFalse(stopWatch.isStarted());
        stopWatch.start();
        assertTrue(stopWatch.isStarted());
    }

    @Test
    public void isStoppedTest() {
        assertTrue(stopWatch.isStopped());
        stopWatch.start();
        assertFalse(stopWatch.isStopped());
    }

    @Test
    public void isSuspendedTest() {
        assertFalse(stopWatch.isSuspended());
        stopWatch.start();
        stopWatch.suspend();
        assertTrue(stopWatch.isSuspended());
    }

    @Test
    public void resetTest() {
        stopWatch.start();
        stopWatch.split();
        assertTrue(stopWatch.isStarted());
        assertTrue(stopWatch.getSplitNanoTime() > 0);
        stopWatch.reset();
        assertFalse(stopWatch.isStarted());
        assertThrows(RuntimeException.class, () -> stopWatch.getSplitNanoTime());
    }

    @Test
    public void resumeTest() {
        stopWatch.start();
        stopWatch.suspend();
        assertTrue(stopWatch.isSuspended());
        stopWatch.resume();
        assertFalse(stopWatch.isSuspended());
    }

    @Test
    public void splitTest() {
        assertThrows(RuntimeException.class, () -> stopWatch.getSplitNanoTime());
        stopWatch.start();
        stopWatch.split();
        assertTrue(stopWatch.getSplitNanoTime() > 0);
    }

    @Test
    public void startTest() {
        assertFalse(stopWatch.isStarted());
        stopWatch.start();
        assertTrue(stopWatch.isStarted());
    }

    @Test
    public void stopTest() {
        stopWatch.start();
        assertFalse(stopWatch.isStopped());
        stopWatch.stop();
        assertTrue(stopWatch.isStopped());
    }

    @Test
    public void suspendTest() {
        stopWatch.start();
        assertFalse(stopWatch.isSuspended());
        stopWatch.suspend();
        assertTrue(stopWatch.isSuspended());
    }

    @Test
    public void unsplitTest() {
        stopWatch.start();
        stopWatch.split();
        assertTrue(stopWatch.getSplitNanoTime() > 0);
        stopWatch.unsplit();
        assertThrows(RuntimeException.class, () -> stopWatch.getSplitNanoTime());
    }
}