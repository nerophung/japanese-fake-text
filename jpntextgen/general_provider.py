# -*- coding: utf-8 -*- 
import random
import os 

from .utils import constants 

class GeneralProvider(object):

    first_phone_num = [0,0,0,0,0,0,0,1,2,3,4,5,6,7,8,9]

    phone_format = {
        0: '{}{}{}{}{}{}{}{}{}{}'.format(random.choice(first_phone_num), random.randint(0, 9), random.randint(0, 9),random.randint(0, 9),random.randint(0, 9),random.randint(0, 9),random.randint(0, 9),random.randint(0, 9),random.randint(0, 9),random.randint(0, 9)),
        1: '{}{}{}-{}{}{}-{}{}{}{}'.format(random.choice(first_phone_num), random.randint(0, 9), random.randint(0, 9),random.randint(0, 9),random.randint(0, 9),random.randint(0, 9),random.randint(0, 9),random.randint(0, 9),random.randint(0, 9),random.randint(0, 9)), 
        2: '{}{}{}-{}{}{}{}-{}{}{}'.format(random.choice(first_phone_num), random.randint(0, 9), random.randint(0, 9),random.randint(0, 9),random.randint(0, 9),random.randint(0, 9),random.randint(0, 9),random.randint(0, 9),random.randint(0, 9),random.randint(0, 9)),
        3: '{}{}({}{}{}{}){}{}{}{}'.format(random.choice(first_phone_num), random.randint(0, 9), random.randint(0, 9),random.randint(0, 9),random.randint(0, 9),random.randint(0, 9),random.randint(0, 9),random.randint(0, 9),random.randint(0, 9),random.randint(0, 9)),
        4: '{}{}{}({}{}{}){}{}{}{}'.format(random.choice(first_phone_num), random.randint(0, 9), random.randint(0, 9),random.randint(0, 9),random.randint(0, 9),random.randint(0, 9),random.randint(0, 9),random.randint(0, 9),random.randint(0, 9),random.randint(0, 9))
    }

    currency_list = ['$', '￥']

    price_format = {
        0: '{:,}'.format(random.randint(0, 1500000000)),
        1: '{:,}.{}'.format(random.randint(0, 1000000000), random.randint(0, 99)), 
        2: '{}'.format(random.randint(0, 1000000000)),
        3: '{:,}'.format(random.randint(0, 1000000000))
    }

    product_code_format = {
        0: '{}{}{}-{}{}{}{}{}{}{}{}{}'.format(random.choice(constants.ALPHA_CHARS), random.randint(0, 9), random.randint(0, 9),random.randint(0, 9),random.randint(0, 9),random.randint(0, 9),random.randint(0, 9),random.randint(0, 9),random.randint(0, 9),random.randint(0, 9),random.randint(0, 9),random.randint(0, 9),random.randint(0, 9) ), 
        1: '{}{}'.format(random.choice(constants.ALPHA_CHARS), ''.join(random.choices(constants.NUMBERS, k=random.randint(8, 13))))
    }

    def __init__(self, data_path='data'):
        with open(os.path.join(os.path.dirname(__file__), data_path, 'romaji_name.txt')) as romaji_name:
            self.__romaji_name = romaji_name.readlines()

        with open(os.path.join(os.path.dirname(__file__), data_path, 'domain_name.txt')) as domain_name:
            self.__domain_name = domain_name.readlines()

    def get_additional_info(self):
        additional_info = ''
        for i in range(random.randint(2, 7)):
            additional_info += random.choice(constants.ADDITIONAL_CHAR)

        if random.randint(0, 1):
            additional_info += '(有)'
        elif random.randint(0, 1):
            additional_info = '(有)'+ additional_info

        return additional_info
    
    def get_domain(self):
        domain_name = random.choice(self.__domain_name)
        return domain_name.strip()

    def get_romaji_name(self):
        romaji_name = random.choice(self.__romaji_name)
        return romaji_name.strip()

    def get_email(self):
        domain_name = self.get_domain()
        romaji_name = self.get_romaji_name()
        return romaji_name + '@' + domain_name
    
    def get_url(self):
        host_name = random.choice(['https://www.', 'www.', 'http://www.'])
        return host_name + self.get_domain()

    def get_eng_katakana(self):
        katakana_eng = random.choice(constants.KATAKANA_LIST)
        for i in range(random.randint(1, 11)):
            katakana_eng += random.choice(constants.KATAKANA_LIST)
        return katakana_eng

    def get_phone_number(self):
        return self.phone_format[random.randint(0, 4)]

    def get_post_code(self):
        post_code = ''
        post_code += str(random.choice(['〒', '']))
        post_code += '{}{}{}-{}{}{}{}'.format(random.randint(0, 9), random.randint(0, 9),random.randint(0, 9),random.randint(0, 9),random.randint(0, 9),random.randint(0, 9),random.randint(0, 9))
        return post_code
    
    def get_price(self):
        money_type = random.choice(self.currency_list)
        price = random.choice(self.price_format)
        return random.choice([money_type + price, price + money_type])

    def get_product_code(self):
        return self.product_code_format[random.randint(0, 1)]

    def get_status(self):
        return random.choice(constants.STATUS_LIST)

    def get_general_text(self):
        return random.choice([
            self.get_additional_info(), 
            self.get_email(), 
            self.get_url(), 
            self.get_eng_katakana(), 
            self.get_phone_number(), 
            self.get_post_code(), 
            self.get_price(), 
            self.get_product_code()
        ])