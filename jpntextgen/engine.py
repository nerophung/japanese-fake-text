# -*- coding: utf-8 -*- 
from .address_provider import AddressProvider
from .name_provider import NameProvider
from .date_provider import DateProvider

class Engine(object):

    def __init__(self):
        self.__address_provider = AddressProvider()
        self.__name_provider = NameProvider()
        self.__date_provider = DateProvider()

    def get_address(self):
        return self.__address_provider.get_address()

    def get_full_name(self):
        return self.__name_provider.get_full_name()

    def get_date(self):
        return self.__date_provider.get_date()
