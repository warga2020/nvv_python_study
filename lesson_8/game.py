# Количество бочонков — 90 штук (с цифрами от 1 до 90).

# Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
# расположенных по возрастанию. Все цифры в карточке уникальны.

# 2 игрока - пользователь и компьютер

import random


class Sack:
    """ the sack with barrels """

    def __init__(self):
        # generate numbers in the bag
        self.__burrels = [x for x in range(1, 91)]

    def take_barrel(self):
        """ pull out a barrel from the bag"""
        pass


class Card:
    def __init__(self, name):
        self.name = name
        rr = [0 for _ in range(1, 10)]
        self.__card = {1: rr.copy(), 2: rr.copy(), 3: rr.copy()}
        self.__init_card_data()

    def __str__(self):
        s = ''
        s += '*' * 3 * 9 + '\n'
        for row in self.__card.values():
            row = [str(n) if n != 0 else '' for n in row]
            s += ''.join([str(it).rjust(3, ' ') for it in row])[1:] + '\n'
        s += '*' * 3 * 9
        return s

    def __init_card_data(self):
        """ 3 rows of 5 numbers. All numbers in the card are unique. """
        # общий набор чисел
        common_set = set()
        for i in (1, 2, 3):
            self.__fill_row(common_set, i)

    def __fill_row(self, common_set, row_i):
        """ fill row of card """
        while True:
            # the row has 5 numbers -> break
            if len([x for _ in self.__card[row_i] if _ != 0]) == 5:
                break
            # generate a num [1..90]
            num = random.randint(1, 90)
            # проверка что в данной строке есть число в соответствующем десятке
            # ...  и еще нет в "общем" наборе
            x = num // 10
            decade = x if x != 9 else 8
            if self.__card[row_i][decade] == 0 and num not in common_set:
                common_set.add(num)
                self.__card[row_i][decade] = num

    def look_barrel(self, b_val):
        """ remove number from this card if same number exist """
        for i in (1, 2, 3):
            if b_val in self.__card[i]:
                self.__card[i].remove(b_val)
                break

    def is_game_over(self):
        for i in (1, 2, 3):
            if sum(self.__card[i]) == 0:
                return True
        return False

    def find_num(self, num):
        for i in (1, 2, 3):
            if num in self.__card[i]:
                return True
        return False


# ------------- game ---------------


sack = Sack()
pc_card = Card('PC')
user_card = Card('YOU')

while True:
    if pc_card.is_game_over() or user_card.is_game_over:
        print('Game over!')
        break
    # pull out a barrel
    b_val = sack.take_barrel()
    # check
    pc_card.look_barrel(b_val)
    answer = input('You have same number [y/n] :')
    if answer
