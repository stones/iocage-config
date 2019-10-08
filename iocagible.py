#!/usr/bin/env python3.6
import sys
import subprocess

sys.path.insert(1, './lib')
sys.path.insert(0, './lib/tasks')

from parseCliArgs import cliArgs
from iocagibleParser import IocagibleParser
from loadConfig import load

config = load(cliArgs.file)

parser = IocagibleParser()

parser.create(config, cliArgs.pretend)