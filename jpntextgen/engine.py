# -*- coding: utf-8 -*- 
from .address_provider import AddressProvider
from .name_provider import NameProvider
from .date_provider import DateProvider
from .general_provider import GeneralProvider

class Engine(object):

    def __init__(self, data_path='data'):
        self.__address_provider = AddressProvider(data_path=data_path)
        self.__name_provider = NameProvider(data_path=data_path)
        self.__date_provider = DateProvider()
        self.__general_provider = GeneralProvider(data_path=data_path)

    def get_general_provider(self):
        return self.__general_provider

    def get_name_provider(self):
        return self.__name_provider

    def get_date_provider(self):
        return self.__date_provider

    def get_address_provider(self):
        return self.__address_provider

    def get_address(self):
        return self.__address_provider.get_address()

    def get_full_name(self):
        return self.__name_provider.get_full_name()

    def get_date(self):
        return self.__date_provider.get_date()

    def get_general_text(self):
        return self.__general_provider.get_general_text()

    def get_additional_info(self):
        return self.__general_provider.get_additional_info()

    def get_email(self):
        return self.__general_provider.get_email()

    def get_url(self):
        return self.__general_provider.get_url()

    def get_eng_katakana(self):
        return self.__general_provider.get_eng_katakana()

    def get_phone_number(self):
        return self.__general_provider.get_phone_number()

    def get_post_code(self):
        return self.__general_provider.get_post_code()

    def get_price(self):
        return self.__general_provider.get_price()

    def get_product_code(self):
        return self.__general_provider.get_product_code()

    def get_status(self):
        return self.__general_provider.get_status()