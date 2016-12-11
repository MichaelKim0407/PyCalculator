#!/usr/bin/python3

import logging

from mklibpy.terminal.interact import user_input

import calculator
import constant

__author__ = 'Michael'

if __name__ == '__main__':
    logging.basicConfig(
        format=constant.LOG_FORMAT,
        filename=constant.LOG_FILE,
        level=logging.INFO
    )
    calc = calculator.new_calculator()
    while True:
        line = user_input(":")
        try:
            calc.line(line)
        except calculator.ExitCommand:
            break
        except calculator.ResetCommand:
            calc = calculator.new_calculator()
