#!/usr/bin/python3.6
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, './lib')

from parseCliArgs import cliArgs

print(cliArgs.file)