"""
Name: robot.py
Version: 0.1
Description: Command shell terminal.
"""

import cmd
import argparse

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
        self.running = False

    # TODO: Fix me.
    def runparser(self):
        parser = argparse.ArgumentParser(description='Image Downloader', prog='Imgdl')
        parser.add_argument('start', nargs=1, metavar='<service>', dest='command', help='Start a service.')
        parser.add_argument('stop', nargs=1, metavar='<service>', dest='command', help='Stop a service')
        parser.add_argument('restart', nargs=1, metavar='<service>', dest='command', help='Restart a service')
        self.running = True
        return parser.parse_args()

    def run(self):
        if not self.running:
            args = self.runparser()
        print('--' + cmd.Cmd.precmd(self, args.command[0]))
