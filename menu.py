# -*- coding: utf-8 -*-

import random


class Menu:

    def okazu(self):
        item = {'peach': '4',
                'melon': '4',
                'Cherry': '1',
                'orange': '3',
                'Grape': '4',
                'persimmon': '3',
                'strawberry': '3',
                'watermelon': '7',
                'pear': '4',
                'grapefruit': '3',
                'banana': '2',
                'Apple': '5',
                'pineapple': '6'
                }
        print(list(item.items()))
        fruit, val = random.choice(list(item.items()))
        return fruit
