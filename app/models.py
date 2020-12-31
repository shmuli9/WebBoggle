import random

from app import db
from app.config import Config
from app.solver import solver
from app.utils import generate_uuid


class Node:
    def __init__(self, letter, trans=None):
        self.letter = ""
        self.transitions = {}

        self.letter = letter
        if trans:
            self.transitions = trans

    def __str__(self):
        return self.letter

    def __repr__(self):
        return self.letter

    def add_transitions(self, trans):
        self.transitions = trans


class Board(db.Model):
    __tablename__ = "boards"

    id = db.Column(db.String(6), primary_key=True)

    dice = db.Column(db.String(17))  # not safe for larger boggle boards...

    nodes = [[]]

    def __init__(self, board=None):
        self.id = generate_uuid()
        self.size = Config.BOGGLE_BOARD_DIMENSION
        self.nodes = [[{} for i in range(self.size)] for j in range(self.size)]

        if not board:
            board_dice = random.sample(Config.DICE, len(Config.DICE))
            board = [[random.choice(board_dice.pop()) for __ in range(self.size)] for _ in range(self.size)]
        self.dice = "".join(["".join(row) for row in board])

        q_offset = 0
        for i in range(self.size):
            for j in range(self.size):
                die = self.dice[i * self.size + j + q_offset]
                if die == "Q":
                    die = "QU"
                    q_offset += 1
                self.nodes[i][j] = Node(die)

        for i in range(self.size):
            canUp = i != 0
            canDown = i != self.size - 1
            for j in range(self.size):
                canLeft = j != 0
                canRight = j != self.size - 1

                trans = {}

                if canUp:
                    trans["up"] = self.nodes[i - 1][j]
                    if canRight:
                        trans["upRight"] = self.nodes[i - 1][j + 1]
                        trans["right"] = self.nodes[i][j + 1]
                    if canLeft:
                        trans["upLeft"] = self.nodes[i - 1][j - 1]
                        trans["left"] = self.nodes[i][j - 1]
                if canDown:
                    trans["down"] = self.nodes[i + 1][j]
                    if canRight:
                        trans["downRight"] = self.nodes[i + 1][j + 1]
                        trans["right"] = self.nodes[i][j + 1]
                    if canLeft:
                        trans["downLeft"] = self.nodes[i + 1][j - 1]
                        trans["left"] = self.nodes[i][j - 1]

                self.nodes[i][j].add_transitions(trans)

    def generate_board(self, uppercase_u=False):
        """returns a 2 dimensional array for the dice"""

        table = []
        q_offset = 0

        for i in range(self.size):
            row = []
            for col in range(self.size):
                die = self.dice[i * self.size + col + q_offset]
                if die == "Q":
                    die = "QU" if uppercase_u else "Qu"
                    q_offset += 1
                row.append(die)
            table.append(row)

        return table

    def generate_words(self):
        return solver.generate_words(self)

    def __str__(self):
        out = ""
        for i in range(self.size):
            for j in range(self.size):
                out += f"{str(self.nodes[i][j].letter)} " \
                    # f"- Possible transitions: {str(self.nodes[i][j].possible_transitions())}"
                out += " " if j is not self.size - 1 else ""
            out += "\n" if i is not self.size - 1 else ""
        return out

    def print_board(self):
        row = ""
        for i in range(self.size):
            line1 = ""
            line2 = ""
            line3 = ""
            for j in range(self.size):
                lines = self._cell(self.nodes[i][j]).split("\n")
                line1 += lines[0]
                line2 += lines[1]
                line3 += lines[2]
            row += f"{line1}\n{line2}\n{line3}"
            row += " " if j is not self.size - 1 else ""
            row += "\n" if i is not self.size - 1 else ""
        return row

    def _cell(self, node):
        output = ""
        letter = node.letter
        trans = node.transitions
        symbols = {
            "up": " ⬆ ",
            "down": " ⬇ ",
            "right": " ➡ ",
            "left": " ⬅ ",
            "upRight": " ↗ ",
            "upLeft": " ↖ ",
            "downRight": " ↘ ",
            "downLeft": " ↙ "
        }
        spacing = "  "

        output += symbols["upLeft"] if "upLeft" in trans else spacing
        output += symbols["up"] if "up" in trans else spacing
        output += symbols["upRight"] if "upRight" in trans else spacing
        output += "\n"

        output += symbols["left"] if "left" in trans else spacing
        output += letter + " "
        output += symbols["right"] if "right" in trans else spacing
        output += "\n"

        output += symbols["downLeft"] if "downLeft" in trans else spacing
        output += symbols["down"] if "down" in trans else spacing
        output += symbols["downRight"] if "downRight" in trans else spacing
        output += "\n"

        return output
