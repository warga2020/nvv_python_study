from lesson_8.loto_game.consts import *
import random as rnd


class Sack:
    """ the sack with barrels """
    def __init__(self):
        self._num_set = [x for x in range(1, MAX_NUM_LOTO + 1)]

    def get_barrel(self):
        """ get a barrel with number out of the sack """
        while True:
            rnd.shuffle(self._num_set)
            rnd_i = rnd.randint(0, len(self._num_set) - 1)
            val = self._num_set[rnd_i]
            self._num_set.remove(val)
            yield val
            if len(self._num_set) == 0:
                break


if __name__ == '__main__':
    s = Sack()
    i = 1
    for n in s.get_barrel():
        print(f'{i} -> {n}')
        i += 1
