import sys
sys.path.insert(1, './')

from iocagibleTasks import IocagibleTasks

class IocagibleParser:

    def __init__(self, name, vars, pretend):
        self.name = name
        self.vars = vars
        self.pretend = pretend

    def runTasks(self, tasks):
        taskRunner = IocagibleTasks(self.name, self.vars, self.pretend) 
        taskRunner.run(tasks)