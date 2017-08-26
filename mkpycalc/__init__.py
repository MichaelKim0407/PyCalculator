import logging

from mklibpy.terminal.interact import user_input
from mklibpy.util.collection import format_list

from . import calculator
from . import constant

__author__ = 'Michael'


def expression(line):
    calc = calculator.new_calculator(False)
    calc.line(line)


def start_interactive():
    calc = calculator.new_calculator()
    while True:
        line = user_input(":")
        try:
            calc.line(line)
        except calculator.ExitCommand:
            break
        except calculator.ResetCommand:
            calc = calculator.new_calculator()


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("expression", nargs=argparse.REMAINDER)
    args = parser.parse_args()

    logging.basicConfig(
        format=constant.LOG_FORMAT,
        filename=constant.LOG_FILE,
        level=logging.INFO
    )

    if args.expression:
        expression(format_list(args.expression, "", "", " ", False))
    else:
        start_interactive()
