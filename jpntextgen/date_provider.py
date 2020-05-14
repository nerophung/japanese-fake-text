# -*- coding: utf-8 -*- 
import random
from .utils import constants 

class DateProvider(object):

    date_format = {
        0: '{}{}/{:02d}/{:02d}'.format(random.choice(constants.YEAR_LIST), random.randint(0, 70), random.randint(1, 31), random.randint(1, 12)),
        1: '{}{}/{:02d}'.format(random.choice(constants.YEAR_LIST),random.randint(0, 70), random.randint(1, 12)),
        2: '{}{}.{:02d}'.format(random.choice(constants.YEAR_LIST),random.randint(0, 70), random.randint(1, 12)),
        3: '{}{}.{:02d}.{:02d}'.format(random.choice(constants.YEAR_LIST),random.randint(0, 70), random.randint(1, 31), random.randint(1, 12)),
        4: '{}{}年{:02d}月{:02d}日'.format(random.choice(constants.YEAR_LIST),random.randint(0, 70), random.randint(0, 31), random.randint(0, 12)),
        5: 'R{}年{:02d}月{:02d}日'.format(random.randint(0, 70), random.randint(1, 12), random.randint(1, 31)),
        6: 'R{}年{:02d}月'.format(random.randint(0, 70), random.randint(1, 12)),
        7: 'R{}/{:02d}/{:02d}'.format(random.randint(0, 70), random.randint(1, 12), random.randint(1, 31)),
        8: 'R{}/{:02d}'.format(random.randint(0, 70), random.randint(1, 12)),
        9: '{}年{:02d}月{:02d}日'.format(random.randint(1800, 2100), random.randint(1, 31), random.randint(1, 12)),
        10: '{}{}.{:02d}.{:02d}'.format(random.choice(constants.YEAR_LIST),random.randint(0, 70), random.randint(1, 31), random.randint(1, 12)),
        11: '{}{}/{:02d}'.format(random.choice(constants.YEAR_LIST),random.randint(0, 70), random.randint(1, 12)),
        12: '{}.{:02d}.{:02d}'.format(random.randint(1800, 2100), random.randint(1, 12), random.randint(1, 31)),
        13: '{}/{:02d}/{:02d}'.format(random.randint(1800, 2100), random.randint(1, 12), random.randint(1, 31)),
        14: '{}/{:02d}'.format(random.randint(1800, 2100), random.randint(1, 12)),
        15: '{}.{:02d}'.format(random.randint(1800, 2100), random.randint(1, 12)),
    }

    def __init__(self):
        pass

    def get_date(self):
        return self.date_format[random.randint(0, 15)]
