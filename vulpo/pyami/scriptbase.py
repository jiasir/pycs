import os
import sys
from vulpo.utils import ShellCommand, get_ts
import vulpo
import vulpo.utils

class ScriptBase(object):

    def __init__(self, config_file=None):
        self.instance_id = vulpo.config.get('Instance', 'instance-id', 'default')
        self.name = self.__class__.__name__
        self.ts = get_ts()
        if config_file:
            vulpo.config.read(config_file)

    def notify(self, subject, body=''):
        vulpo.utils.notify(subject, body)

    def mkdir(self, path):
        if not os.path.isdir(path):
            try:
                os.mkdir(path)
            except:
                vulpo.log.error('Error creating directory: %s' % path)

    def umount(self, path):
        if os.path.ismount(path):
            self.run('umount %s' % path)

    def run(self, command, notify=True, exit_on_error=False, cwd=None):
        self.last_command = ShellCommand(command, cwd=cwd)
        if self.last_command.status != 0:
            vulpo.log.error('Error running command: "%s". Output: "%s"' % (command, self.last_command.output))
            if notify:
                self.notify('Error encountered', \
                        'Error running the following command:\n\t%s\n\nCommand output:\n\t%s' % \
                        (command, self.last_command.output))
            if exit_on_error:
                sys.exit(-1)
        return self.last_command.status

    def main(self):
        pass

