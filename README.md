# PyCalculator

Author: MichaelKim0407 <jinzheng19930407@sina.com>

## Installation

1. Make sure you have Python2.7 or Python3.4+

2. Install `mklibpy`

    Please refer to https://github.com/MichaelKim0407/mklibpy for installation.

3. Download or clone this package

## Run

Run main.py using a desired version of Python.

There is no need to start the program under the same folder.

## Make it easier to run

1. On Windows

    * Create a desktop entry

        On your desktop, create pycalc.bat;

        Edit with Notepad or any text file editor, and enter the following command:

            python3 path\to\PyCalculator\main.py

        Replace `python3` with the desired version of Python.

        Now you should be able to start the calculator by double-clicking the .bat file.

2. On Linux / Mac

    * Make it accessible in terminal by every user

        Login as `root`;

        Download or clone the package under `/usr/lib` (or anywhere that is owned by `root`);

        Create a file called `pycalc.log`, and give rw privilege to all users by `chmod a+rw pycalc.log`;

        Under `/usr/bin` (or anywhere that is included in the system PATH), create a symlink to `main.py`:

            ln -s /usr/lib/PyCalculator/main.py pycalc

        Now, you should be able to run `pycalc` anywhere with any user.

        If you don't want to use Python3, or your Python3 is not installed at `/usr/bin/python3`, create a bash script called `pycalc` and enter:

            #!/bin/bash
            python3 /usr/lib/PyCalculator/main.py

        And make the script executable by `chmod +x pycalc`.

    * (Ubuntu) Create a desktop entry

        Copy `py-calculator.desktop` to `~/Desktop/`.

        Now you should be able to start the calculator by double-clicking the desktop entry.

## Basic usages

1. Enter any expression and get the result.

        :1 + 2
        3

2. The result will be stored (in `_`) for the next expression.

        :1 + 2
        3
        :+ 6
        9
        :2 ** _
        512

    Note: To use `+`/`-` as positive/negative signs instead of add/subtract, surround the number with parentheses.

        :10
        10
        :-5
        5
        :(-5)
        -5

3. Store a value to a variable using `>>`.

        :1 + 2
        3
        :>> x
        3
        :x
        3
        :+ 5 >> y
        8
        :y
        8

4. Use values and functions from the `math` package of Python.

        :sin(pi / 6)
        0.5

## Basic controls

1. To exit the program, enter `exit`.

2. To reset the calculator, enter `reset`.

3. To list all stored values and functions, enter `show`.

4. To clear the screen, enter `clear`.

## Advanced usages (for Python programmers)

1. An assign statement in Python (`=`, `+=`, etc.) is the same as `>>` and will be stored into `_`.

        :x = 1
        1
        :x += 3
        4

2. Any one-line Python code can be executed.

        :1 >> x
        1
        :print "---{}---".format(x)
        ---1---

3. Define custom functions using one-line code or a lambda expression.

        :def cube(x): return x ** 3
        <function cube at ......>
        :cube(4)
        64
        :sq = lambda x: x ** 2
        <function <lambda> at ......>
        :sq(5)
        25

4. Execution log can be found in `pycalc.log` under the program folder.
