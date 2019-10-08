
from baseTask import BaseTask

class CopyTask(BaseTask):
    pass

    def getTestString(self, name):
        return 'Copy still not implemented' + name

# def copyTask(params, vars pretend):
#     # iocage exec sonarr mkdir /usr/local/etc/rc.d
#     # cp ./sonarr.rc  /mnt/iocage/jails/sonarr
#     # iocage exec sonarr chmod 555 /usr/local/etc/rc.d/sonarr
#     # try:
#     #     subprocess.check_output(['iocage', 'exec', jailName, 'mkdir','/usr/local/etc/rc.d' ])
#     #     subprocess.check_output(['cp', params.src, '/root' + params.dest ])
#     #     subprocess.check_output(['iocage', 'exec', 'sonarr', 'chmod', '555', '/usr/local/etc/rc.d/sonarr' ])
#     # except subprocess.CalledProcessError as e:
#     #     print e.output

#     print('Copy not implemented:', params)