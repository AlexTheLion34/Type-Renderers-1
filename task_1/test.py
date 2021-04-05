import unittest
from task_1 import check_vars
from task_1 import print_vars
import sys
import os

# For testing purpose
import pandas as pd


# For testing purpose
class MyClass:
    pass


class Test(unittest.TestCase):

    def test_builtins(self):
        """
        Test that function works on common built-in types
        """
        a = 1
        b = 2.0
        c = complex(1, 2)
        d = False
        e = None
        f = ''
        g = []
        h = {}
        i = set()

        is_built_actual = list(check_vars(depth=1).values())

        # Additional False value because of self parameter passes to the method
        is_built_expected = [False] + [True for _ in range(9)]

        self.assertEqual(is_built_expected, is_built_actual)

    def test_non_built_ins(self):
        """
        Test that function works on not built-in types
        """
        a = MyClass()
        b = pd.DataFrame()

        is_built_actual = list(check_vars(depth=1).values())

        # Additional False value because of self parameter passes to the method
        is_built_expected = [False for _ in range(3)]

        self.assertEqual(is_built_expected, is_built_actual)

    def test_classes(self):
        """
        Test that function works on classes properly
        Should return True because any class is instance of type which is built-in
        """

        a = MyClass
        b = pd.DataFrame

        is_built_actual = list(check_vars(depth=1).values())

        # Additional False value because of self parameter passes to the method
        is_built_expected = [False] + [True for _ in range(2)]

        self.assertEqual(is_built_expected, is_built_actual)

    def test_printing(self):
        """
        Test that function prints result in an appropriate format
        """

        a = 1
        b = MyClass()
        c = [1, 2, 3]
        d = pd.DataFrame()

        console_stdout = sys.stdout

        with open('test.txt', 'w') as f:
            sys.stdout = f
            print_vars()
            sys.stdout = console_stdout

        with open('test.txt', 'r') as f:
            actual_lines = (list(map(lambda line: line.replace('\n', ''), f.readlines())))

        expected_lines = [
            'self: False',
            'a: True',
            'b: False',
            'c: True',
            'd: False',
            'console_stdout: False',
            'f: False'
        ]

        os.remove('test.txt')

        self.assertEqual(expected_lines, actual_lines)


if __name__ == '__main__':
    unittest.main()
