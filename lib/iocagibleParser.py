from iocagibleTasks import IocagibleTasks
from CreateJailTask import CreateJailTask

class IocagibleParser:

    def runTasks(self,name, vars, tasks, pretend):
        taskRunner = IocagibleTasks(name, vars, pretend) 
        taskRunner.run(tasks)

    def create(self, config, pretend):
        name =config['name']
        vars = config['vars']
        tasks = config['tasks']

        createJail = CreateJailTask(name, vars)
        createJail.run({}, pretend)
        # Reinstate when finished testing
        # self.runTasks(name, vars, tasks, pretend)