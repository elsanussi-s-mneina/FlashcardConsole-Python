from typing import List
from flashcard import Flashcard
import random


class FlashcardSet:
    def __init__(self):
        self.card_list : List[Flashcard] = []

    def add_flashcard(self, flashcard: Flashcard) -> None:
        self.card_list.append(flashcard)

    def list_flashcards(self) -> str:
        list_string: str = ''
        for card in self.card_list:
            card_string = card.get_both_sides()
            list_string += card_string + '\n'
        return list_string

    def print_as_file(self) -> str:
        file_contents = ''
        for card in self.card_list:
            file_contents += card.line_for_file() + '\n'
        return file_contents

    def read_as_file(self, file_contents: str):
        lines = file_contents.split('\n')
        for line in lines:
            if '\t' in line:
                flashcard = Flashcard()
                flashcard.read_as_line(line)
                self.card_list.append(flashcard)

    def start_quiz(self):
        print('Starting quiz.')
        for card in self.card_list:
            card.ask_for_front_side()

    def start_practice(self):
        print('Starting practice.')
        while True:
            random_index = random.randint(0, len(self.card_list) - 1)
            card = self.card_list[random_index]
            card.ask_for_front_side()
            option = input('([C] Continue) or \n [x] stop practice\n>')
            if option == 'x':
                break
