package org.crprojects;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

/**
 * This file should NOT be reviewed, nor should your code review comments
 * revolve around including more tests. However, feel free to run the
 * tests or to include more, e.g., to understand how the program works
 * or to verify certain program functionality.
 */
public class TodoListAppTest {

    private TodoListApp app;

    @BeforeEach
    public void setUp() {
        app = new TodoListApp();
    }

    @Test
    public void addTaskTest() {
        assertEquals(0, app.tasks.size());
        app.addTask("Test task", 1);
        assertEquals(1, app.tasks.size());
        assertEquals("Test task", app.tasks.get(0).message);
        assertEquals(1, app.tasks.get(0).priority);
    }

    @Test
    public void reverseTaskStatusTest() {
        app.addTask("Test task", 1);
        assertFalse(app.tasks.get(0).done);
        app.reverseTaskStatus(0);
        assertTrue(app.tasks.get(0).done);
        app.reverseTaskStatus(0);
        assertFalse(app.tasks.get(0).done);
    }

    @Test
    public void deleteTaskTest() {
        app.addTask("Test task", 1);
        assertEquals(1, app.tasks.size());
        app.deleteTask(0);
        assertEquals(0, app.tasks.size());
    }
}