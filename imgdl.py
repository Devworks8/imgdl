"""
Name: imgdl.py
Version: 0.1
Description: Image downloader for various services. I.e. Facebook, Pintress, etc.
"""

import configuration


def main():
    config = configuration.Config()
    settings = config.get_settings()
    services = config.get_services()
    print(settings)
    print(services)


if __name__ == "__main__":
    main()
