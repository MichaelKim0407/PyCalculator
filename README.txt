Py-Calculator is a Python-based, easy-to-use calculator.
Arthur: MichaelKim0407 <jinzheng19930407@sina.com>

--- SETUP & RUN ---

1. Please make sure you have Python 2.7 installed on your computer.

2. Unpack the source code anywhere you like.

3. Run main.py using Python 2.7.

--- BASIC USAGES ---

1. Enter any expression and get the result.

:1 + 2
3

2. The result will be stored (__last__) for the next expression.

:1 + 2
3
:+ 6
9
:2 ** __last__
512

Note: To use +/- as positive/negative signs instead of add/subtract, surround the number with parentheses.

:10
10
:-5
5
:(-5)
-5

3. Store a value to a variable using '>>'.

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

4. Use values and functions from the 'math' package of Python.

:sin(pi / 6)
0.5

--- BASIC CONTROLS ---

1. To exit the program, enter 'exit'.
2. To reset the calculator, enter 'reset'.
3. To list all stored values and functions, enter 'show'.
4. To clear the screen, enter 'clear'.

--- ADVANCED USAGES (for Python programmers) ---

1. An assign statement in Python ('=', '+=', etc.) is the same as ">>" and will be stored into __last__.

:x = 1
1
:x += 3
4

2. Any one-line Python code can be executed.

:1 >> x
1
:print "---{}---".format(x)
---1---

3. Define custom functions using a one-line code or a lambda expression.

:def cube(x): return x ** 3
<function cube at ......>
:cube(4)
64
:sq = lambda x: x ** 2
<function <lambda> at ......>
:sq(5)
25

4. Execution log can be found at 'pycalc.log' under the program folder. There is no need to start the program under that folder.
