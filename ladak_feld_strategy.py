import random

class LadaKFeldStrategy:

    # FELD Strategy:
    # - always defect after the other player defects
    # - probability of cooperation after the other player cooperates is decreasing during the game:
    #               P(cooperation) =    cooperationIndex/100
    #       1 <=    P(cooperation) <=   0.5

    @staticmethod
    def author_name():
        return "Lada Kudlackova"

    @staticmethod
    def strategy_name():
        return "LadaK FELD Strategy"

    def __init__(self):
        self.reset()

    def reset(self):
        self.last_op = None
        self.cooperationIndex = 100

    def last_move(self, my_move, other_move):
        self.last_op = other_move

    def play(self):
        if self.cooperationIndex > 50.0:
            self.cooperationIndex = self.cooperationIndex - 1   

        if self.last_op == 'D':
            return 'D'

        rand = random.randint(1, 100);
        if rand <= self.cooperationIndex:
            return 'C'
        return 'D'

def create_strategy():
    return LadaKFeldStrategy()