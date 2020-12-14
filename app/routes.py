import random

from flask import render_template, jsonify, redirect, url_for, Blueprint

from app import db
from app.config import Config
from app.models import Board
from app.solver import generate_valid_words
from app.wordtree import wt

bp = Blueprint("routes", __name__)


def async_reset_wt():
    wt.reset_tree()


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

    words = sorted(generate_valid_words(boggle_board))
    wt.reset_tree()
    # Thread(target=async_reset_wt()).start()

    return jsonify(
        {"game_id": boggle_board.id, "board": board, "words": words}), 200


@bp.route('/join/<game_id>')
def boggle_board(game_id):
    board = Board.query.filter_by(id=game_id).first()

    if not board:
        return redirect(url_for("routes.index"))

    words = sorted(generate_valid_words(Board(board.dice)))
    wt.reset_tree()
    # Thread(target=async_reset_wt()).start()

    return render_template("index.html", game_id=board.id, dice=f"{board.generate_board()}",
                           words=words)
