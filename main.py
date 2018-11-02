from flashcard import Flashcard
from typing import List, Optional


def main() -> None:
    print('Console Application for Memorizing Flashcards')
    response : Optional[str] = None
    while not response == 'x':
        print('What do you want to do?')
        print('[n] Create a new set of flashcards.')
        print('[l] load an existing set of flashcards.')
        print('[x] exit the program.')
        response = input('>')
        if response == 'n':
            create_new_flashcard_set()
        elif response == 'l':
            load_flashcard_set()

    print('Program terminated normally.')


def create_new_flashcard_set() -> None:
    print('Creating a new flashcard set...')
    set_name = input('What do you want to name the new flashcard set?\n')
    flashcards : List[Flashcard] = []
    print('Creating a new flashcard set named', set_name)
    while True:
        print('What do you want to do?')
        print('[a] Add a flashcard?')
        print('[v] list flashcards?')
        print('[x] go back to main menu')
        option = input('>')
        if option == 'a':
            print('Adding a flashcard...')
            front_side = input('Type the text that goes on the front side:\n>')
            back_side = input('Type the text that goes on the back side:\n>')
            card = Flashcard()
            card.set_front_side(front_side)
            card.set_back_side(back_side)
            flashcards.append(card)
        elif option == 'v':
            for card in flashcards:
                print(card.get_both_sides())
        elif option == 'x':
            break


def load_flashcard_set() -> None:
    print('loading flashcard set...')

main()