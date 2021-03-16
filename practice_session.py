import random
from typing import List
from flashcard import Flashcard

class PracticeSession:
    def start_practice(self, card_list: List[Flashcard]) -> None:
        print('Starting practice.')
        while True:
            random_index: int = random.randint(0, len(card_list) - 1)
            card: Flashcard = card_list[random_index]
            self.ask_for_other_side(card)
            option: str = input('([C] Continue) or \n [x] stop practice\n>')
            if option == 'x':
                break

    def ask_for_other_side(self, card) -> None:
        card.ask_for_back_side()
