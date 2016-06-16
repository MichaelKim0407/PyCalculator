import os
import types

__author__ = 'Michael'


def clear_screen():
    os.system("cls")


def split_var_func(d):
    var_dict = dict()
    func_dict = dict()
    for key in d:
        val = d[key]
        if isinstance(val, types.FunctionType) \
                or isinstance(val, types.BuiltinFunctionType) \
                or isinstance(val, types.BuiltinMethodType):
            func_dict[key] = val
        else:
            var_dict[key] = val
    return var_dict, func_dict


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


def valid_var_name(name):
    if not (name[0].isalpha() or name[0] == "_"):
        return False
    for i in name[1:]:
        if not (i.isalnum() or i == "_"):
            return False
    return True
