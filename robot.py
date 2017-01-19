"""
Name: robot.py
Version: 0.1
Description: Command shell terminal.
"""

import cmd

__version__ = '0.1'


class Shell(cmd.Cmd):
    def __init__(self,
                 context=None,
                 prompt_name='imgdl'):
        super().__init__()
        self.stdout.write('Imgdl {}\n'.format(__version__))
        self.stdout.write("Type \"help\" for command line help\n\n")
        self.prompt = prompt_name + ': '
        self.misc_header = "Commands"

    def do_start(self, args):
        print('start service')

    def do_stop(self, args):
        print('stop service')

    def do_restart(self, args):
        print('restart service')

    def do_quit(self, args):
        print('Quitting.')
        raise SystemExit

    def emptyline(self):
        pass

    def run(self):
        pass
