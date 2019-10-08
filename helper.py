#!/usr/bin/python3.6
import sys
sys.path.insert(1, './lib')

from parseCliArgs import cliArgs
from loadConfig import load

config = load(cliArgs.file)

def handleUnknownAction( name, config):
    print('I dont know how to handle:', name)

def handleNameAction(description):
    print('TASK:', description)

def handleTask(taskName, config):
    if(taskName == 'name'):
        handleNameAction(config)
    else:
        handleUnknownAction(taskName, config)

def handleTaskGroup( taskGroup):
    for task in taskGroup :
        handleTask(task, taskGroup[task])

for taskGroup in config['tasks']:
    handleTaskGroup( taskGroup ) 
    print('')