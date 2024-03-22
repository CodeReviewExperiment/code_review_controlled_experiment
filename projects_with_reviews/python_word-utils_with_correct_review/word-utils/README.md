# Instructions
**IMPORTANT: PLEASE, AS SOON AS YOU FINISH REVIEWING A PROJECT, COME BACK TO THIS FILE AND RATE THE CONFIDENCE OF YOUR REVIEW. SIMPLY WRITE A NUMBER FROM 1 TO 5 AT THE END OF THIS FILE.**

To review this project, you can open the root folder (i.e., `~/`) or the project folder (i.e., `~/cr-study-2024/<language>/<project>`). Make sure to review each source file except for the main file (`main.py` or `Main.java`), which does not need to be reviewed. However, **the main file includes a description of the project to review, which we recommend you to read**.

In some cases, you may see review comments already added to the files that you need to review. **Please, consider these comments to write your own review**. You can also delete or modify these comments if you feel they are not relevant/correct.

## Adding a new code review comment
To add a comment, simply select some text (it can be multiple lines), right click, then select `Code Review: Add Note`. A new window will open, where you can include a comment in the `Description` field. Feel free to ignore the other fields, i.e., `Title`, `Category`, `Additional Info`, `Priority` and `Private`. After you've finished, click on `Save`.

## Modifying or deleting an existing comment
If some source code has a comment added, you will see a `Code Review:` message on top of the first line commented. Click on the message and a new "Code Review" window will open, allowing you to modify (`Update`), delete (`Delete`) or keep the original comment (`Cancel`).

## Seeing all comments
To see all added comments, simply click on the "Code Review" extension that should be visible on the left bar of Visual Studio Code.


# Java projects
## Running the application
To run a Java application, you have two options:
1. Click on the "Run" code lens that pops up on top of the `main()` method of the `Main` Java class. This code lens might take a few seconds to appear.
2. Click on the run button (play-like triangle icon on the top right corner of Visual Studio Code) when on the `Main` Java class.

## Running the tests
To run the tests for a Java application, simply proceed as follows:
1. Open any Java file (source or test). Wait a few seconds so that the Java plugin of Visual Studio Code automatically loads the tests.
2. The "Testing" extension of Visual Studio Code should be now visible on the left bar. Click on it and select any test that you want to run.

## Troubleshooting
If you opened a Java project from the root folder of your own user, it is possible that, when running it, you get the following error:

```
Error: Could not find or load main class org.crprojects.Main
Caused by: java.lang.ClassNotFoundException: org.crprojects.Main
```

If so, try opening the Command Palette (Ctrl + Shift + P) and select the option "Java: Rebuild Projects".


# Python projects
## Running the application
To run a Python application, you have two options:
1. Click on the run button (play-like triangle icon on the top right corner of Visual Studio Code) when on the `main.py` Python file.
2. Run `main.py` from the terminal. From the root folder of the project (`~/cr-study-2024/python/<project>`), type the following command:
    ```
    python main.py
    ```

## Running the tests
If you opened a Python project from the root folder of your own user, it is possible that tests do not show up automatically on the "Testing" tab extension of Visual Studio Code. If this is the case, you can always run the tests of a given Python project from the command line as follows:
```
cd ~/cr-study-2024/python/<project>
python -m unittest
```


# Rate the confidence of your code review
At the end of the session, please rate how confident you are about your review, from 1 to 5, where 1 is "Not confident at all" and 5 is "Absolutely confident".

Confidence: 