#!/usr/bin/python3.6
import sys
import subprocess
sys.path.insert(1, './lib')

from parseCliArgs import cliArgs
from loadConfig import load

config = load(cliArgs.file)

jailName = 'sonarr'

def handleCopy(params):
    # iocage exec sonarr mkdir /usr/local/etc/rc.d
    # cp ./sonarr.rc  /mnt/iocage/jails/sonarr
    # iocage exec sonarr chmod 555 /usr/local/etc/rc.d/sonarr
    try:
        subprocess.check_output(['iocage', 'exec', jailName, 'mkdir','/usr/local/etc/rc.d' ])
        subprocess.check_output(['cp', params.src, '/root' + params.dest ])
        subprocess.check_output(['iocage', 'exec', 'sonarr', 'chmod', '555', '/usr/local/etc/rc.d/sonarr' ])
    except subprocess.CalledProcessError as e:
        print e.output

    print('Copy not implemented:', params)

def handleExec(params):
    # iocage exec sonarr ln -s /usr/local/bin/mono /usr/bin/mono
    print('Exec not implements:', params)

def handleFetch(params):
    # iocage exec sonarr "fetch http://download.sonarr.tv/v2/master/mono/NzbDrone.master.tar.gz -o /usr/local/share"
    # iocage exec sonarr "tar -xzvf /usr/local/share/NzbDrone.master.tar.gz -C /usr/local/share"
    # iocage exec sonarr rm /usr/local/share/NzbDrone.master.tar.gz
    print('Fetch not implements:', params)

def handleMediaUser(params):
    # Add media user
    # iocage exec sonarr "pw user add media -c media -u 8675309 -d /nonexistent -s /usr/bin/nologin"
    # iocage exec sonarr "pw groupadd -n media -g 8675309"
    # iocage exec sonarr "pw groupmod media -m sonarr"
    print('Add media user not implemented:', params)

def handleMount(params):
    # iocage fstab -a sonarr /mnt/Tank/configs/sonarr /mnt/config nullfs rw 0 0
    print('Mount not implmented:', params)

def handleName(description):
    print('TASK:', description)

def handleService(params):
    # iocage exec sonarr service sonarr start
    print('service not implemented:', params)

def handleSysrc(params):
    # iocage exec sonarr sysrc "sonarr_enable=YES"
    print('sysrc not implemented:', params)

def handleUnknown( name, config):
    print('I dont know how to handle:', name)

def handleTask(taskName, config):
    if(taskName == 'copy'):
        handleCopy(config)
    elif(taskName == 'exec'):
        handleExec(config)
    elif(taskName == 'fetch'):
        handleFetch(config)
    elif(taskName == 'mediaUser'):
        handleMediaUser(config)
    elif(taskName == 'mount'):
        handleMount(config)
    elif(taskName == 'name'):
        handleName(config)
    elif(taskName == 'service'):
        handleService(config)
    elif(taskName == 'sysrc'):
        handleSysrc(config)
    else:
        handleUnknown(taskName, config)

def handleTaskGroup( taskGroup):
    for task in taskGroup :
        handleTask(task, taskGroup[task])

for taskGroup in config['tasks']:
    handleTaskGroup( taskGroup ) 
    print('')