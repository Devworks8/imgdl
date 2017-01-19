"""
Name: imgdl.py
Version: 0.1
Description: Image downloader for various services. I.e. Facebook, Pintress, etc.
"""

from threading import Thread
import argparse

import configuration
import robot

__version__ = '0.1'


def runparser():
    parser = argparse.ArgumentParser(description='Image Downloader', prog='Imgdl')
    parser.add_argument('--gui', action='store_true', dest='gui', help='Start GUI.')
    parser.add_argument('--debug', action='store_true', dest='debug', help='Enable debugging.')
    parser.add_argument('--version', action='version', version='%(prog)s {}'.format(__version__))
    return parser.parse_args()


def main():
    config = configuration.Config()
    settings = config.get_settings()
    services = config.get_services()

    # Parse command line arguments.
    args = runparser()
    if args.gui:
        print('Run GUI')
    elif args.debug:
        print('Run debugger, and enable logging')
    shell = robot.Shell()
    cmd_loop_thread = Thread(target=shell.run)
    cmd_loop_thread.daemon = True
    cmd_loop_thread.start()

    shell.cmdloop()


if __name__ == "__main__":
    main()
