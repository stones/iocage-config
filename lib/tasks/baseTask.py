
class BaseTask:

    def __init__(self, name, config):
        self.name = name
        self.config = config

    def getTestString(self, name):
        return 'Copy not implemented' + name

    def run(self, params):
        print( self.getTestString(self.name))