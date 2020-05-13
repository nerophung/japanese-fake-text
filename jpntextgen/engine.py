from .address_provider import AddressProvider
from .name_provider import NameProvider

class Engine(object):

    def __init__(self):
        self.__address_provider = AddressProvider()
        self.__name_provider = NameProvider()

    def get_address(self):
        return self.__address_provider.get_address()

    def get_full_name(self):
        return self.__name_provider.get_full_name()
