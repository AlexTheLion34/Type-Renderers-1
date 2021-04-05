import sys

PYTHON_3 = (3,)
PYTHON_3_7 = (3, 7)

PYTHON_2_BUILTINS_NAME = '__builtin__'
PYTHON_3_TO_3_7_BUILTINS_NAME = '__builtins__'
PYTHON_GREATER_THAN_3_7_BUILTINS_NAME = 'builtins'


def is_built_in(val):

    version = sys.version_info
    root_module = val.__class__.__module__

    if version < PYTHON_3:
        return root_module == PYTHON_2_BUILTINS_NAME
    elif PYTHON_3 <= version < PYTHON_3_7:
        return root_module == PYTHON_3_TO_3_7_BUILTINS_NAME
    else:
        return root_module == PYTHON_GREATER_THAN_3_7_BUILTINS_NAME


def check_vars(depth):
    return {name: is_built_in(val=value) for name, value in sys._getframe(depth).f_locals.items()}


def print_vars(depth=2):
    for name, is_built in check_vars(depth=depth).items():
        print(name + ': ' + str(is_built))

