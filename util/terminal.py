import os

__author__ = 'Michael'


def clear_screen():
    os.system("cls")


def print_vars(d):
    for key in sorted(d.keys()):
        print "{: >16} = {: >16}".format(key, d[key])


def print_func_names(d):
    if not d:
        return
    result = ""
    x = 0
    width = 16
    columns = 6
    for item in sorted(d.keys()):
        s = str(item)
        d = (len(s) + 1) / width + 1
        if x + d > columns and x != 0:
            result += "\n"
            x = 0
        spec = "{{: <{}}}".format(width * d)
        s_right = spec.format(s)
        result += s_right
        x += d
    print result


def print_result(text):
    print "\033[36;1m{}\033[0m".format(text)


def print_err(text):
    print "\033[31;1m{}\033[0m".format(text)
