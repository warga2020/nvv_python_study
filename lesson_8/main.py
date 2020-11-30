from lesson_8.loto_game.sack import Sack
from lesson_8.loto_game.abstract_card import Card
from lesson_8.loto_game.arbiter import Arbiter


class PCCard(Card):
    def __init__(self):
        super().__init__('PC')

    def try_close_num(self, num):
        is_deleted = False
        for i in self._cells.keys():
            if num in self._cells[i]:
                ind = self._cells[i].index(num)
                self._cells[i][ind] = -1
                is_deleted = True
                break
        return is_deleted


class UserCard(Card):
    def __init__(self):
        super().__init__('User')

    def try_close_num(self, num):
        for i in self._cells.keys():
            if num in self._cells[i]:
                ind = self._cells[i].index(num)
                self._cells[i][ind] = -1
                break
        s = input(f'Close the number [{num}] - (y/Y)? ')
        return s.lower() == 'y'


sack = Sack()
gamers_cards = [PCCard(), UserCard()]
Arbiter(sack, gamers_cards).start_game()
