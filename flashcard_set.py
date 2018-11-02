from flashcard import Flashcard


class FlashcardSet:
    def __init__(self):
        self.card_list = []

    def add_flashcard(self, flashcard: Flashcard):
        self.card_list.append(flashcard)

    def list_flashcards(self):
        list_string: str = ''
        for card in self.card_list:
            card_string = card.get_both_sides()
            list_string += card_string + '\n'
        return list_string