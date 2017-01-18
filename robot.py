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
                 prompt_name='imgdl',
                 **kwargs):
        super().__init__()
        self.stdout.write('Imgdl {}\n'.format(__version__))
        self.stdout.write("Type \"help\" for command line help or "
                          "\"commands\" for bot commands\n\n")
        self.prompt = prompt_name + ': '
        self.misc_header = "Commands"

    def run(self):
        # self.stdout.write("imgdl: ")
        self.stdout.flush()
