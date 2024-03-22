package org.crprojects;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.Date;
import java.util.Scanner;

/**
 * A simple to-do list application that allows users to add, mark as done/undone, delete, and list tasks with various sorting options.
 */
public class TodoListApp {

    // List to store tasks
    final ArrayList<Task> tasks;
    private final Scanner scanner = new Scanner(System.in);

    /**
     * Constructor to initialize the to-do list.
     */
    public TodoListApp() {
        this.tasks = new ArrayList<>();
    }

    /**
     * Adds a new task to the to-do list.
     *
     * @param message  The message or description of the task.
     * @param priority The priority level of the task.
     */
    public void addTask(String message, int priority) {
        Task task = new Task(message, priority);
        tasks.add(task);
        System.out.println("Task added successfully.");
    }

    /**
     * Toggles the completion status of a task at a given index.
     *
     * @param index The index of the task in the list.
     */
    public void reverseTaskStatus(int index) {
        if (index < tasks.size()) {
            Task task = tasks.get(index);
            if (task.done) {
                task.done = false;
                System.out.println("Task marked as undone.");
            } else {
                task.done = true;
                System.out.println("Task marked as done.");
            }
        } else {
            System.out.println("Invalid task index.");
        }
    }

    /**
     * Deletes a task from the to-do list based on the given index.
     *
     * @param index The index of the task to be deleted.
     */
    public void deleteTask(int index) {
        if (index < tasks.size()) {
            tasks.remove(index);
            System.out.println("Task deleted successfully.");
        } else {
            System.out.println("Invalid task index.");
        }
    }

    /**
     * Lists all tasks in the to-do list with sorting options.
     *
     * @param sortBy The parameter to sort the tasks by (date, priority, alphabetically).
     */
    public void listTasks(String sortBy) {
        if (tasks.isEmpty()) {
            System.out.println("No tasks available.");
            return;
        }

        switch (sortBy.toLowerCase()) {
            case "", "date":
                tasks.sort(Comparator.comparing(task -> task.creationDate));
                break;
            case "priority":
                tasks.sort(Comparator.comparingInt(task -> task.priority));
                break;
            case "alphabetically":
                tasks.sort(Comparator.comparing(task -> task.message));
                break;
            default:
                System.out.println("Invalid sorting option.");
                return;
        }

        System.out.println("Tasks:");
        for (int i = 0; i < tasks.size(); i++) {
            Task task = tasks.get(i);
            System.out.printf("%d. [%s] %s (Priority: %d, Created on: %s)%n",
                    i + 1, task.done ? "X" : " ", task.message, task.priority, task.creationDate);
        }
    }

    /**
     * Handles user input for integers and returns the parsed integer.
     *
     * @param scanner        The Scanner object to read user input.
     * @param requestMessage The prompt message for the user.
     * @return The parsed integer.
     */
    private int processInputInt(Scanner scanner, String requestMessage) {
        Integer input = null;
        while (input == null) {
            try {
                input = Integer.parseInt(scanner.nextLine());
            } catch (NumberFormatException e) {
                System.out.println("Invalid number. Please try again.");
                System.out.print(requestMessage);
            }
        }
        return input;
    }

    /**
     * Manages the interaction with the to-do list application.
     */
    private void interactWithApp() {
        printMenu();

        int choice = processInputInt(scanner, "Enter your choice: ");

        switch (choice) {
            case 1:
                System.out.print("Enter task message: ");
                String message = scanner.nextLine();
                System.out.print("Enter task priority: ");
                int priority = processInputInt(scanner,  "Enter task priority: ");
                this.addTask(message, priority);
                break;
            case 2:
                System.out.println("These are your current tasks:");
                this.listTasks("");
                System.out.print("Enter the index of the task to mark as done/undone: ");
                int doneIndex = processInputInt(scanner, "Enter the index of the task to mark as done/undone: ");
                this.reverseTaskStatus(doneIndex - 1);
                break;
            case 3:
                System.out.println("These are your current tasks:");
                this.listTasks("");
                System.out.print("Enter the index of the task to delete: ");
                int deleteIndex = processInputInt(scanner, "Enter the index of the task to delete: ");
                this.deleteTask(deleteIndex - 1);
                break;
            case 4:
                System.out.print("Enter sorting option (date/priority/alphabetically). Default is date: ");
                String sortBy = scanner.nextLine();
                this.listTasks(sortBy);
                break;
            case 5:
                System.out.println("Exiting the application. Goodbye!");
                System.exit(0);
                break;
            default:
                System.out.println("Invalid choice. Please try again.");
        }
    }

    /**
     * Prints the menu options for the application.
     */
    private static void printMenu() {
        System.out.println("\n--- Todo List Application ---");
        System.out.println("1. Add Task");
        System.out.println("2. Mark Task as Done/Undone");
        System.out.println("3. Delete Task");
        System.out.println("4. List Tasks");
        System.out.println("5. Exit");
        System.out.print("Enter your choice: ");
    }

    /**
     * Starts the to-do list application.
     */
    public void run() {
        while (true) {
            interactWithApp();
        }
    }

    /**
     * Inner class representing a task in the todo list.
     */
    static class Task {
        final String message;
        final int priority;
        final Date creationDate;
        boolean done;

        public Task(String message, int priority) {
            this.message = message;
            this.priority = priority;
            this.creationDate = new Date();
            this.done = false;
        }
    }
}
