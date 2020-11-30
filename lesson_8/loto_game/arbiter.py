class Arbiter:
    """ Its job is:\n
    - to get the barrels from the sack
    - to announce the taken number
    - to control over the closure of existing numbers in user cards
    - to public the result of game
    """
    def __init__(self, sack, card_list):
        self.__sack = sack
        self.__card_list = card_list

    def start_game(self):
        for num in self.__sack.get_barrel():
            print('Barrel number = ' + str(num))
            for card in self.__card_list:
                print(card)
                # if the number exists - it will be deleted (True + True)
                # if the number absents - ... (False + False)
                is_exist = card.is_exist_number(num)
                is_closed_num = card.try_close_num(num)
                # wrong state
                if is_exist != is_closed_num:
                    print(f'\nGamer {card.name} lost!')
                    print('GAME OVER')
                    exit(0)
                if card.is_card_empty():
                    print(f'Gamer [{card.name}] is WINNER !!!')
                    print('GAME OVER')
                    exit(0)

