# -*- coding: utf-8 -*-

import random


class Menu:

    def okazu(self):
        item = {'マクドナルド': '4',
                'ケンタッキー': '4',
                '焼肉ライク': '1',
                '野菜を食べるカレーcamp': '3',
                '岡むら屋': '4',
                'すき家': '3',
                '松屋': '3',
                '吉野家': '7',
                }
        print(list(item.items()))
        fruit, val = random.choice(list(item.items()))
        return fruit
