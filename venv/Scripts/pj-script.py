#!D:\python\flowmeter\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'javascripthon==0.11','console_scripts','pj'
__requires__ = 'javascripthon==0.11'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('javascripthon==0.11', 'console_scripts', 'pj')()
    )
