class Flashcard():
    def __init__(self):
        self.front_side = ''
        self.back_side = ''

    def set_front_side(self, front_side) -> None:
        self.front_side = front_side

    def set_back_side(self, back_side) -> None:
        self.back_side = back_side

    def get_front_side(self) -> str:
        return self.front_side

    def set_front_side(self, new_front_side: str) -> None:
        self.front_side = new_front_side

    def get_back_side(self) -> str:
        return self.back_side

    def set_back_side(self, new_back_side: str) -> None:
        self.back_side = new_back_side

    def get_both_sides(self) -> str:
        return self.front_side + '  |||  ' + self.back_side

    def line_for_file(self) -> str:
        return escape_tab_character(self.front_side) \
            + '\t' \
            + escape_tab_character(self.back_side)

    def read_as_line(self, line) -> None:
        parts_of_line: List[str] = line.split('\t')
        self.front_side = undo_escape_tab_character(parts_of_line[0])
        self.back_side = undo_escape_tab_character(parts_of_line[1])

    def ask_for_back_side(self) -> None:
        print('Give the back side of', self.get_front_side())
        attempted_backside: str = input('>')
        print('Compare your attempt:\nattempt:\t', attempted_backside, '\ncorrect:\t', self.get_back_side())
        print('Next card.')

    def ask_for_front_side(self) -> None:
        print('Give the front side of', self.get_back_side())
        attempted_backside: str = input('>')
        print('Compare your attempt:\nattempt:\t', attempted_backside, '\ncorrect:\t', self.get_front_side())
        print('Next card.')


def escape_tab_character(a_string : str) -> str:
    return a_string.replace('\t', '\\t')


def undo_escape_tab_character(a_string: str) -> str:
    return a_string.replace('\\t', '\t')
