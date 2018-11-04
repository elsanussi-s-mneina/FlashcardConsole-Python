class Flashcard():
    def __init__(self):
        self.front_side = ''
        self.back_side = ''
        pass

    def set_front_side(self, front_side) -> None:
        self.front_side = front_side

    def set_back_side(self, back_side) -> None:
        self.back_side = back_side

    def get_both_sides(self) -> str:
        return self.front_side + '  |||  ' + self.back_side

    def line_for_file(self) -> str:
        return escape_tab_character(self.front_side) \
            + '\t' \
            + escape_tab_character(self.back_side)

    def read_as_line(self, line) -> None:
        parts_of_line = line.split('\t')
        self.front_side = unescape_tab_character(parts_of_line[0])
        self.back_side = unescape_tab_character(parts_of_line[1])


def escape_tab_character(a_string : str) -> str:
    return a_string.replace('\t', '\\t')


def unescape_tab_character(a_string: str) -> str:
    return a_string.replace('\\t', '\t')