from typing import List
from flashcard import Flashcard
import random
import csv

from practice_session import PracticeSession
from reversed_practice_session import ReversedPracticeSession


class FlashcardSet:
    def __init__(self):
        self.card_list : List[Flashcard] = []

    def add_flashcard(self, flashcard: Flashcard) -> None:
        self.card_list.append(flashcard)

    def edit_flashcards(self) -> None:
        index = 0
        while True:
            if len(self.card_list) == 0:
                print('please add cards before editing!')
                print('Exiting editing cards panel...')
                break;
            if index >= len(self.card_list):
                print('Done going through cards. Starting back at beginning')
                index = 0
            if index < 0:
                print('Done going through cards before beginning. Going to the end.')
                index = len(self.card_list) - 1
            curr_card = self.card_list[index]
            print('Current card:')
            print(curr_card.get_both_sides())
            print('Make a selection:')
            print('[f] edit card front side')
            print('[b] edit card back side')
            print('[d] delete card')
            print('[n] go to next card')
            print('[p] go to previous card')
            print('[x] exit editing panel')
            option = input('What is your selection:\n>')

            if option == 'f':
                print('Editing front side')
                print('The current front side is:', self.card_list[index].get_front_side())
                new_frontside = input('Give the new front side:')
                self.card_list[index].set_front_side(new_frontside)
            elif option == 'b':
                print('Editing back side')
                print('The current front side is:', self.card_list[index].get_back_side())
                new_backside = input('Give the new back side:')
                self.card_list[index].set_back_side(new_backside)
            elif option == 'd':
                confirmation = input('Are you sure? [y/N]')
                if confirmation == 'y':
                    del self.card_list[index]
                    print('The card has been deleted.')
                else:
                    print('The card has not been deleted.')
            elif option == 'n':
                index += 1
                print('Going to next card...')
            elif option == 'p':
                index -= 1
                print('Going to previous card...')
            elif option == 'x':
                break

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

    def read_as_file_comma_separated(self, file_name: str):
        with open(file_name, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                flashcard = Flashcard()
                if len(row) > 0:
                    flashcard.set_front_side(row[0])
                if len(row) > 1:
                    flashcard.set_back_side(row[1])
                self.card_list.append(flashcard)

    def start_quiz(self):
        print('Starting quiz.')
        for card in self.card_list:
            card.ask_for_back_side()

    def start_quiz_with_reversed_sides(self):
        print('Starting quiz (reversed: back to front).')
        for card in self.card_list:
            card.ask_for_front_side()

    def start_practice(self):
        option = input('[n] Normal (front to back)\n[r] Reversed (back to front)')
        practice_session = PracticeSession()
        if option == 'r':
            practice_session = ReversedPracticeSession()
        practice_session.start_practice(self.card_list)

    def count_flashcards(self) -> int:
        return len(self.card_list)