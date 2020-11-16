import os
import sys
import __main__


print(__main__.__file__)


print('\n\n\n\n\n')
os.execv('test.py', sys.argv)