# PyCalculator v2

Author: [Michael Kim](http://michaelkim0407.com) <mkim0407@gmail.com>

## Installation

1. Make sure you have Python2.7 or Python3.4+

2. Install using pip

    ```
    pip install mkpycalc
    ```

## Run

A script named `pycalc` should be automatically installed by pip.

1. Run in interactive mode

    ```
    pycalc
    ```

2. Evaluate single expression

    ```
    pycalc EXPRESSION
    ```

    There is no need to quote the expression.

    **However**, if the expression contains `*`, your shell may replace it with file names under current working directory, in which case you do need to quote the expression.

## Basic usages

1. Enter any expression and get the result.

    ```
    :1 + 2
    3
    ```

2. The result will be stored (in `_`) for the next expression.

    ```
    :1 + 2
    3
    :+ 6
    9
    :2 ** _
    512
    ```

    Note: To use `+`/`-` as positive/negative signs instead of add/subtract, surround the number with parentheses.

    ```
    :10
    10
    :-5
    5
    :(-5)
    -5
    ```

3. Store a value to a variable using `>>`.

    ```
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
    ```

4. Use values and functions from the `math` package of Python.

    ```
    :sin(pi / 6)
    0.5
    ```

## Basic controls

1. To exit the program, enter `exit`.

2. To reset the calculator, enter `reset`.

3. To list all stored values and functions, enter `show`.

4. To clear the screen, enter `clear`.

## Advanced usages (for Python programmers)

1. An assign statement in Python (`=`, `+=`, etc.) is the same as `>>` and will be stored into `_`.

    ```
    :x = 1
    1
    :x += 3
    4
    ```

2. Any one-line Python code can be executed.

    ```
    :1 >> x
    1
    :print "---{}---".format(x)
    ---1---
    ```

3. Define custom functions using one-line code or a lambda expression.

    ```
    :def cube(x): return x ** 3
    <function cube at ......>
    :cube(4)
    64
    :sq = lambda x: x ** 2
    <function <lambda> at ......>
    :sq(5)
    25
    ```

## Import as a library

Simply `import mkpycalc` in your Python program and do whatever you want!

## License

MIT
