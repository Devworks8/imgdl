"""
Name: imgdl.py
Version: 0.1
Description: Image downloader for various services. I.e. Facebook, Pintress, etc.
"""

from threading import Thread

import configuration
import robot


def main(**kwargs):
    config = configuration.Config()
    settings = config.get_settings()
    services = config.get_services()
    if not kwargs:
        print("must process kwargs")
    shell = robot.Shell(**kwargs)
    cmd_loop_thread = Thread(target=shell.run)
    cmd_loop_thread.daemon = True
    cmd_loop_thread.start()

    shell.cmdloop()


if __name__ == "__main__":
    main()
