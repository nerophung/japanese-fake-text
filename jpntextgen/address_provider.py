# -*- coding: utf-8 -*- 
import os
import pickle
import random

from .utils import constants 

class AddressProvider(object):

    def __init__(self, data_path='data'):
        self.__handle = open(os.path.join(os.path.abspath(os.path.dirname(__file__)), data_path , 'address.pkl'), 'rb')
        self.__address_provider = pickle.load(self.__handle)
        self.__handle.close()

    def __get_katakana_name(self, num_chars=5, set_random=True, probability=0.6):
        assert probability < 1, "Probability must be lower than 1!"
        katakana_name = ''
        have_kata_name = random.choices([True, False], weights=[probability, 1 - probability], k=1)[0]
        if have_kata_name:
            katakana_name = ''.join(random.choices(constants.KATAKANA_LIST, k=num_chars))
        return katakana_name

    def __get_split_area(self, state, probability=0.6):
        assert probability < 1, "Probability must be lower than 1!"
        split_area = ' '
        have_area = random.choices([True, False], weights=[probability, 1 - probability], k=1)[0]
        use_symbol = random.choices([True, False], weights=[0.5, 0.5], k=1)[0]
        if not use_symbol and have_area:
            if state[-1].isdigit():
                split_area = "-{}{} ".format(random.randint(1, 10), random.randint(1, 15), self.__get_apartment_number())
            else:
                split_area = "-{}-{}{} ".format(random.randint(1, 10), random.randint(1, 15), self.__get_apartment_number())
        elif have_area:
            split_area = "{}番地{}号{} ".format(random.randint(1, 10), random.randint(1, 15), self.__get_apartment_number()[1:])
        return split_area

    def __get_apartment_number(self, probability=0.4):
        assert probability < 1, "Probability must be lower than 1!"

        apart_num = ''
        have_apart = random.choices([True, False], weights=[probability, 1 - probability], k=1)[0]
        if have_apart:
            apart_num = "-{}".format(random.randint(1, 999))
        return apart_num
    
    def __get_floor(self, katakana_name, probability=0.4):
        assert probability < 1, "Probability must be lower than 1!"
        floor = ''
        have_floor = random.choices([True, False], weights=[probability, 1 - probability], k=1)[0]
        if have_floor and len(katakana_name) > 1:
            floor = " {}{}".format(random.randint(1, 100), random.choice(["F", "階"]))
        return floor

    def get_address(self):
        city_index = random.choice(list(self.__address_provider.keys()))
        city = self.__address_provider[city_index]
        district_index = random.choice(list(city.keys()))
        district = city[district_index]
        state = random.choice(district)
        split_area = self.__get_split_area(state)
        katakana_name = self.__get_katakana_name(set_random=True)
        floor = self.__get_floor(katakana_name)
        return city_index +  district_index + state + split_area + katakana_name + floor
