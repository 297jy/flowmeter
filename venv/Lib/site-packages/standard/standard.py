from __future__ import print_function

import inspect
import re
import sys

from distutils.sysconfig import get_python_lib
from os.path import abspath, join
from termcolor import colored
from traceback import extract_tb, format_list, format_exception_only, format_exception


class flushfile():
    def __init__(self, f):
        self.f = f

    def __getattr__(self, name):
        return object.__getattribute__(self.f, name)

    def write(self, x):
        self.f.write(x)
        self.f.flush()

sys.stderr = flushfile(sys.stderr)
sys.stdout = flushfile(sys.stdout)


def eprint(*args, **kwargs):
    end = kwargs.get("end", "\n")
    sep = kwargs.get("sep", " ")
    (filename, lineno) = inspect.stack()[1][1:3]
    print("{}:{}: ".format(filename, lineno), end="")
    print(*args, end=end, file=sys.stderr, sep=sep)


def formatException(type, value, tb):
    # Absolute paths to site-packages
    packages = tuple(join(abspath(p), "") for p in sys.path[1:])

    # Highlight lines not referring to files in site-packages
    lines = []
    for line in format_exception(type, value, tb):
        matches = re.search(r"^  File \"([^\"]+)\", line \d+, in .+", line)
        if matches and matches.group(1).startswith(packages):
            lines += line
        else:
            matches = re.search(r"^(\s*)(.*?)(\s*)$", line, re.DOTALL)
            lines.append(matches.group(1) + colored(matches.group(2), "yellow") + matches.group(3))
    return "".join(lines).rstrip()


sys.excepthook = lambda type, value, tb: print(formatException(type, value, tb), file=sys.stderr)


def getc(prompt=None):
    while True:
        s = gets(prompt)
        if s is None:
            return None
        if len(s) == 1:
            return s[0]

        # Temporarily here for backwards compatibility
        if prompt is None:
            print("Retry: ", end="")


def getf(prompt=None):
    while True:
        s = gets(prompt)
        if s is None:
            return None
        if len(s) > 0 and re.search(r"^[+-]?\d*(?:\.\d*)?$", s):
            try:
                return float(s)
            except ValueError:
                pass

        # Temporarily here for backwards compatibility
        if prompt is None:
            print("Retry: ", end="")


def geti(prompt=None):
    while True:
        s = gets(prompt)
        if s is None:
            return None
        if re.search(r"^[+-]?\d+$", s):
            try:
                i = int(s, 10)
                if type(i) is int:  # Could become long in Python 2
                    return i
            except ValueError:
                pass

        # Temporarily here for backwards compatibility
        if prompt is None:
            print("Retry: ", end="")


if sys.version_info.major != 3:
    def getlong(prompt=None):
        while True:
            s = gets(prompt)
            if s is None:
                return None
            if re.search(r"^[+-]?\d+$", s):
                try:
                    return long(s, 10)
                except ValueError:
                    pass

            # Temporarily here for backwards compatibility
            if prompt is None:
                print("Retry: ", end="")


def gets(prompt=None):
    try:
        if prompt is not None:
            print(prompt, end="")
        s = sys.stdin.readline()
        if not s:
            return None
        return re.sub(r"(?:\r|\r\n|\n)$", "", s)
    except KeyboardInterrupt:
        sys.exit("")
    except ValueError:
        return None
