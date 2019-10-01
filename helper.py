#!/usr/bin/python3.6
import sys
sys.path.insert(1, './lib')

from parseCliArgs import cliArgs
from loadConfig import load

config = load(cliArgs.file)

print(config['version'])