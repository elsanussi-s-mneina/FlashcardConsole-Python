import random


class PracticeSession:
    def start_practice(self, card_list):
        print('Starting practice.')
        while True:
            random_index = random.randint(0, len(card_list) - 1)
            card = card_list[random_index]
            self.ask_for_other_side(card)
            option = input('([C] Continue) or \n [x] stop practice\n>')
            if option == 'x':
                break

    def ask_for_other_side(self, card):
        card.ask_for_back_side()
