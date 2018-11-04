from practice_session import PracticeSession


class ReversedPracticeSession(PracticeSession):
    def ask_for_other_side(self, card):
        card.ask_for_front_side()
