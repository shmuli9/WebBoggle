import random
import time

from flask import render_template, redirect, url_for, Blueprint

from app import db
from app.config import Config
from app.models import Board
from app.solver import solver

bp = Blueprint("routes", __name__)


@bp.route('/')
def index():
    return render_template("index.html")


@bp.route("/generate_board", methods=["POST"])
def generate_board():
    board_dice = random.sample(Config.DICE, len(Config.DICE))
    board = []

    for _ in range(4):
        board.append([random.choice(board_dice.pop()) for __ in range(4)])

    boggle_board = Board(board)

    db.session.add(boggle_board)
    db.session.commit()

    start = time.time()
    words = solver.generate_words(boggle_board)
    time_taken = f"{(time.time() - start) * 1000:.4f}"

    return {
        "game_id": boggle_board.id,
        "board": board,
        "words": words,
        "time_taken": time_taken
    }


@bp.route('/join/<game_id>')
def boggle_board(game_id):
    board = Board.query.filter_by(id=game_id).first()

    if not board:
        return redirect(url_for("routes.index"))

    words = sorted(solver.generate_words(Board(board.dice)))

    return render_template("index.html", game_id=board.id, dice=f"{board.generate_board()}",
                           words=words)