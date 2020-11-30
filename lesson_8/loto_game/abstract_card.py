from lesson_8.loto_game.consts import *
from abc import ABC, abstractmethod
import random as rnd


class Card(ABC):
    def __init__(self, name):
        """ init the card with 0 in all cells """
        self.name = name
        lst = [0 for _ in range(1, COLS_COUNT + 1)]
        self._cells = {1: lst.copy(), 2: lst.copy(), 3: lst.copy()}
        self.__init_card_data()

    def __str__(self):
        s = self.name + '\n'
        s += '*' * CELL_WIDTH * COLS_COUNT + '\n'
        for row in self._cells.values():
            row = map(lambda x: str(x) if x != 0 else '', row)
            row = map(lambda x: '*' if x == '-1' else x, row)
            s += ''.join([str(it).rjust(CELL_WIDTH, ' ') for it in row])[1:] + '\n'
        s += '*' * CELL_WIDTH * COLS_COUNT
        return s

    def __init_card_data(self):
        """ 3 rows of 5 numbers. All numbers in the card are unique. """
        # in the card all numbers have to be unique
        common_set = set()
        for lst in self._cells.values():
            self.__fill_row(common_set, lst)

    @staticmethod
    def __fill_row(common_set, lst):
        """ fill row of card """
        while True:
            # the row has 5 numbers -> break
            if len(set(lst)) == NUMS_IN_ROW + 1:
                break
            # generate a num [1..90]
            num = rnd.randint(1, MAX_NUM_LOTO)
            x = num // 10
            decade = x if x != 9 else 8
            if lst[decade] == 0 and num not in common_set:
                common_set.add(num)
                lst[decade] = num

    def is_card_empty(self):
        st = set(self.__get_all_nums_in_card())
        return len(st.difference({0, -1})) == 0

    def is_exist_number(self, num):
        return num in self.__get_all_nums_in_card()

    def __get_all_nums_in_card(self):
        return self._cells[1] + self._cells[2] + self._cells[3]

    @abstractmethod
    def try_close_num(self, num):
        pass


if __name__ == '__main__':
    class TestCard(Card):
        def try_close_num(self, num):
            pass


    # 'hide' method __init_card_data
    tmp_method_ref = TestCard._Card__init_card_data
    TestCard._Card__init_card_data = lambda x: None
    testCard = TestCard('TEST CARD')

    assert testCard.is_card_empty()

    # restore method __init_card_data
    TestCard._Card__init_card_data = tmp_method_ref
    testCard._Card__init_card_data()

    print(testCard)

    all_nums = testCard._Card__get_all_nums_in_card()
    print(all_nums)

    assert testCard.is_exist_number(all_nums[1])
    assert not testCard.is_exist_number(-1)
    assert not testCard.is_card_empty()
