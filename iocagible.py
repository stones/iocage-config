#!/usr/bin/python3.6
import sys
import subprocess
sys.path.insert(1, './lib')

from parseCliArgs import cliArgs
from iocagibleParser import IocagibleParser
from loadConfig import load

config = load(cliArgs.file)

parser =  IocagibleParser(config['name'], config['vars'])

parser.runTasks(config['tasks'])