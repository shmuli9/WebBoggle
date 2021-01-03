import random
import time

from flask import Blueprint

from app import db
from app.config import Config
from app.models import Board
from app.solver import solver

bp = Blueprint("routes", __name__)


@bp.route("/generate_board/", defaults={"game_id": ""}, methods=["POST"])
@bp.route("/generate_board/<game_id>", methods=["POST"])
def generate_board(game_id):
    boggle_board = Board.query.filter_by(id=game_id).first()

    if not boggle_board:
        board_dice = random.sample(Config.DICE, len(Config.DICE))
        board = []

        for _ in range(4):
            board.append([random.choice(board_dice.pop()) for __ in range(4)])

        boggle_board = Board(board)

        db.session.add(boggle_board)
        db.session.commit()

    board = boggle_board.generate_board()

    start = time.time()
    words = solver.generate_words(boggle_board)
    time_taken = f"{(time.time() - start) * 1000:.4f}"

    return {
        "game_id": boggle_board.id,
        "board": board,
        "words": words,
        "time_taken": time_taken
    }
