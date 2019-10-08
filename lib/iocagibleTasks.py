

from copyTask import CopyTask

class IocagibleTasks:

    def __init__(self, name, vars, pretend):
        self.name = name
        self.vars = vars
        self.pretend = pretend

    def handleCopy(self, params):
        # iocage exec sonarr mkdir /usr/local/etc/rc.d
        # cp ./sonarr.rc  /mnt/iocage/jails/sonarr
        # iocage exec sonarr chmod 555 /usr/local/etc/rc.d/sonarr
        # try:
        #     subprocess.check_output(['iocage', 'exec', jailName, 'mkdir','/usr/local/etc/rc.d' ])
        #     subprocess.check_output(['cp', params.src, '/root' + params.dest ])
        #     subprocess.check_output(['iocage', 'exec', 'sonarr', 'chmod', '555', '/usr/local/etc/rc.d/sonarr' ])
        # except subprocess.CalledProcessError as e:
        #     print e.output

        # task = CopyTask()
        # task.run()

        temp  = CopyTask(self.name, self.vars)

        temp.run(params)
        print('Copy not implemented:', params)

    def handleExec(self, params):
        # iocage exec sonarr ln -s /usr/local/bin/mono /usr/bin/mono
        print('Exec not implements:', params)

    def handleFetch(self, params):
        # iocage exec sonarr "fetch http://download.sonarr.tv/v2/master/mono/NzbDrone.master.tar.gz -o /usr/local/share"
        # iocage exec sonarr "tar -xzvf /usr/local/share/NzbDrone.master.tar.gz -C /usr/local/share"
        # iocage exec sonarr rm /usr/local/share/NzbDrone.master.tar.gz
        print('Fetch not implements:', params)

    def handleMediaUser(self, params):
        # Add media user
        # iocage exec sonarr "pw user add media -c media -u 8675309 -d /nonexistent -s /usr/bin/nologin"
        # iocage exec sonarr "pw groupadd -n media -g 8675309"
        # iocage exec sonarr "pw groupmod media -m sonarr"
        print('Add media user not implemented:', params)

    def handleMount(self, params):
        # iocage fstab -a sonarr /mnt/Tank/configs/sonarr /mnt/config nullfs rw 0 0
        print('Mount not implmented:', params)

    def handleName(self, description):
        print('TASK:', description)

    def handleService(self, params):
        # iocage exec sonarr service sonarr start
        print('service not implemented:', params)

    def handleSysrc(self, params):
        # iocage exec sonarr sysrc "sonarr_enable=YES"
        print('sysrc not implemented:', params)

    def handleUnknown( self, name, config):
        print('I dont know how to handle:', name)

    def handleTask(self, taskName, config):
        if(taskName == 'copy'):
            self.handleCopy(config)
        elif(taskName == 'exec'):
            self.handleExec(config)
        elif(taskName == 'fetch'):
            self.handleFetch(config)
        elif(taskName == 'mediaUser'):
            self.handleMediaUser(config)
        elif(taskName == 'mount'):
            self.handleMount(config)
        elif(taskName == 'name'):
            self.handleName(config)
        elif(taskName == 'service'):
            self.handleService(config)
        elif(taskName == 'sysrc'):
            self.handleSysrc(config)
        else:
            self.handleUnknown(taskName, config)

    def handleTaskGroup(self, taskGroup):
        for task in taskGroup :
           self.handleTask(task, taskGroup[task])

    def run(self, tasks):
        for taskGroup in tasks:
            self.handleTaskGroup(taskGroup) 