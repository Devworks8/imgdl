"""
Name: configuration.py
Version: 0.1
Description: Setting/services class
"""

import os.path as path

import yaml


# import logging


class Config:
    def __init__(self):
        self._CWD = path.abspath(path.curdir)
        with open(self._CWD + '/services.yml') as fstream:
            self.services = yaml.load(fstream)
        with open(self._CWD + '/settings.yml') as fstream:
            self.settings = yaml.load(fstream)

    def get_settings(self):
        return self.settings

    def get_services(self):
        return self.services

    def set_settings(self, data):
        """
        Setting setter.
        :param data: New setting data.
        :return:
        """
        self._commit(type='setting', data=data)

    def set_services(self, data):
        """
        Service setter.
        :param data: New service data.
        :return:
        """
        self._commit(type='service', data=data)

    def _commit(self, type, data):
        """
        Private setting/service committer.
        :param type: Commit type: setting/service.
        :param data: Data to be committed to the associated type.
        :return:
        """
        pass
