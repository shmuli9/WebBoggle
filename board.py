class Node:
    letter = ""
    transitions = {
        up: {},
        down: {},
        right: {},
        left: {},
        upRight: {},
        upLeft: {},
        downRight: {},
        downLeft: {}
    }

    def __init__(self, letter):
        self.letter = letter
