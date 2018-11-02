class Flashcard():
    def __init__(self):
        self.front_side = ''
        self.back_side = ''
        pass

    def set_front_side(self, front_side):
        self.front_side = front_side

    def set_back_side(self, back_side):
        self.back_side = back_side

    def get_both_sides(self) -> str:
        return self.front_side + '  |||  ' + self.back_side
