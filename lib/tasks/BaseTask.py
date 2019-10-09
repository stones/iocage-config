
import subprocess;

class BaseTask:

    task = 'Base'

    requiredParams = {}

    defaultParams = {}

    def __init__(self, name, config):
        self.name = name
        self.config = config

    def getTestString(self):
        return self.task +' not implemented'

    def verifyRequired(self, required, provided):
        print('Verifying requirements')

    def combineParams(self, defaults, provided):
        print('Combining params')

    def execute(self, commands, pretend):
        if pretend:
            for command in commands:
                print('PRETEND:', ' '.join(command))
        else:
            for command in commands:
                try:
                    subprocess.check_output(command)
                except subprocess.CalledProcessError as e:
                    print(e.output)


    def run(self, params, pretend):
        print('Please implement a `run` function for', self.task)