from iocagibleTasks import IocagibleTasks

class IocagibleParser:

    def runTasks(self,name, vars, tasks, pretend):
        taskRunner = IocagibleTasks(name, vars, pretend) 
        taskRunner.run(tasks)

    def create(self, config, pretend):
        name =config['name']
        vars = config['vars']
        tasks = config['tasks']

        self.runTasks(name, vars, tasks, pretend)