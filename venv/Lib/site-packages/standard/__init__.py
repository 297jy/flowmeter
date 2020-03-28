import os
import sys

try:
    path = sys.path[:]
    sys.path = [p for p in sys.path if p not in ("", os.getcwd())]

    from .standard import eprint, getc, getf, geti, gets
    try:
        from .standard import getlong
    except Exception:
        pass

finally:
    sys.path = path
