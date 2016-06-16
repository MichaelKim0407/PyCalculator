import math
import os

__author__ = 'Michael'

FILE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(FILE_DIR, "pycalc.log")
LOG_FORMAT = "[%(asctime)s %(levelname)s %(name)s] %(message)s"

MATH_VARS = dict(math.__dict__)
for key in MATH_VARS.keys():
    if key.startswith("__"):
        MATH_VARS.pop(key)

INTRO_STR = """Welcome to Michael Kim's Py-Calculator!
Enter 'help' for usage guide.
"""

with open(os.path.join(FILE_DIR, "README.txt")) as f:
    HELP_STR = f.read()
