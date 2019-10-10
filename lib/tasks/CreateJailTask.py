
from BaseTask import BaseTask
from jinja2 import Template

class CreateJailTask(BaseTask):
    task = 'CreateJail'

    requiredParams = {
        'ip': 'The ip parameter is missing'
    }

    defaultParams = {
       'ip': '192.168.1.51',
       'release': '11.2-RELEASE',
       'gateway': '192.168.1.1',
       'vnet': 'on',
       'raw_sockets': 1,
       'boot': 'on',
       'interface': 'vnet0'
    }

    def combineConfigs(self, params):
        return { **{'name': self.name}, **self.defaultParams, **self.config,  **params }

    def run(self, params, pretend):
        config = self.combineConfigs(params)

        command = [ 
            'iocage',
            'create' ,
            '-n',
            '{{ name }}',  
            '-r',
            '{{ release }}', 
            'ip4_addr="{{ interface }}|{{ip}}/24"', 
            'defaultrouter="{{gateway}}"', 
            'vnet="{{vnet}}"', 
            'allow_raw_sockets="{{ raw_sockets}}"',
            'boot="{{ boot }}"'
        ]

        conv = map(lambda x: Template(x).render(config), command )

        self.execute([conv], pretend )
