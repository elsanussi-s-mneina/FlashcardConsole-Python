from flashcard import Flashcard
from flashcard_set import FlashcardSet
from typing import List, Optional

flashcards = FlashcardSet()

already_saved: bool = False
file_name_chosen: Optional[str] = None


def main() -> None:
    print('Console Application for Memorizing Flashcards')
    response : Optional[str] = None
    while not response == 'x':
        print()
        print('What do you want to do?')
        print('[n] Create a new set of flashcards.')
        print('[l] load an existing set of flashcards.')
        print('[s] save the current set of flashcards.')
        print('[sa] save the current set of flashcards in a different file ')
        print('[a] about the program')
        print('[x] exit the program.')
        response = input('>')
        if response == 'n':
            create_new_flashcard_set()
        elif response == 'l':
            load_flashcard_set_from_csv()
        elif response == 's':
            save_flashcard_set(flashcards)
        elif response == 'sa':
            save_flashcard_set_as(flashcards)
        elif response == 'a':
            about_program()

    print('Program terminated normally.')


def create_new_flashcard_set() -> None:
    global flashcards
    print('Creating a new flashcard set...')
    set_name = input('What do you want to name the new flashcard set?\n>')
    flashcards = FlashcardSet()
    print('Creating a new flashcard set named', set_name)
    inside_flashcard_set_panel()


def inside_flashcard_set_panel():
    while True:
        print('What do you want to do?')
        print('[a] Add a flashcard')
        print('[v] list flashcards')
        print('[c] count flashcards')
        print('[e] edit flashcards')
        print('[q] start quiz')
        print('[p] start practice')
        print('[x] go back to main menu')
        option = input('>')
        if option == 'a':
            print('Adding a flashcard...')
            front_side = input('Type the text that goes on the front side:\n>')
            back_side = input('Type the text that goes on the back side:\n>')
            card = Flashcard()
            card.set_front_side(front_side)
            card.set_back_side(back_side)
            flashcards.add_flashcard(card)
        elif option == 'c':
            print('The number of flashcards is:', flashcards.count_flashcards())
        elif option == 'v':
            list_text = flashcards.list_flashcards()
            print(list_text)
        elif option == 'e':
            flashcards.edit_flashcards()
        elif option == 'q':
            flashcards.start_quiz()
        elif option == 'p':
            flashcards.start_practice()
        elif option == 'x':
            break


def load_flashcard_set():
    global flashcards
    global file_name_chosen, already_saved
    print('loading flashcard set...')
    file_name = input('Choose a file name to load from.\n>')
    file = open(file_name, 'r')
    file_contents = file.read()
    flashcards = FlashcardSet()
    flashcards.read_as_file(file_contents)
    print('Done loading file from', file_name)
    inside_flashcard_set_panel()
    file_name_chosen = file_name
    already_saved = True

def load_flashcard_set_from_csv():
    global flashcards
    global file_name_chosen, already_saved
    print('loading flashcard set...')
    file_name = input('Choose a file name to load from.\n>')
    flashcards = FlashcardSet()
    flashcards.read_as_file_comma_separated(file_name)
    print('Done loading file from', file_name)
    inside_flashcard_set_panel()
    file_name_chosen = file_name
    already_saved = True

def save_flashcard_set(flashcard_set: FlashcardSet) -> None:
    global file_name_chosen, already_saved
    print('saving flashcard set...')
    if already_saved:
        file_name = file_name_chosen
    else:
        file_name = input('Choose a file name to save to.\n>')
    file = open(file_name, 'w')
    file.write(flashcard_set.print_as_file())
    print('Done writing file to', file_name)
    already_saved = True
    file_name_chosen = file_name


def save_flashcard_set_as(flashcard_set: FlashcardSet) -> None:
    print('saving flashcard set as...')
    file_name = input('Choose a file name to save to.\n>')
    file = open(file_name, 'w')
    file.write(flashcard_set.print_as_file())
    print('Done writing file to', file_name)


def about_program() -> None:
    print('Programmed by Elsanussi Mneina, November 2, 2018')


main()
