"""
Responsible for storing the current state of a chess game.
Also, Responsible for determining the valid moves at the current state.
Also, keep a move log to undo moves redo etc
"""

class gameState():
    def __init__(self):  # Making a Constructor
        # Two-dimensional listing tho numpy arrays are more efficient for Ai-based work
        # Board is a 8x8 2d List, each element has 2 characters.
        # The first character represents the color of the piece, b or white.
        # The second character represents the type, e.g. 'K', 'Q' etc...
        # "--" Represents an empty space with no pieces
        self.board = [
            # Black Pieces
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            # Blank Spaces as double dash --
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            # White Pieces
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
        ]
        self.whiteToMove = True
        self.moveLog = []
