# -*- coding: utf-8 -*- 
import random
import os

class NameProvider(object):

    def __init__(self,  data_path='data'):
        with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), data_path, 'first_name.txt')) as first_name_file:
            self.__first_name_provider = first_name_file.readlines()
        with open(os.path.join(os.path.dirname(__file__), data_path, 'last_name.txt')) as last_name_file:
            self.__last_name_provider = last_name_file.readlines()

    def get_first_name(self):
        first_name = random.choice(self.__first_name_provider)
        return first_name.strip()

    def get_last_name(self):
        last_name = random.choice(self.__last_name_provider)
        return last_name.strip()

    def get_full_name(self):
        first_name = self.get_first_name()
        last_name = self.get_last_name()
        full_name = '{} {}'.format(first_name, last_name)
        return full_name