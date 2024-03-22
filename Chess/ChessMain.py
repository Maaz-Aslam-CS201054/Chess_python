"""
Driver File: Responsible for handling User Input, also displaying the current gameState of the object
"""
import pygame as p
from Chess import ChessEngine

WIDTH = HEIGHT = 512  # 400 another option, bigget size means low res images of pieces arent of quality representation
DIMENSION = 8  # Chess board dimensions are 8x8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 20  # For animations
IMAGES = {}

'''
lOADING IMAGES VERY EXPENSIVE OPERATION, should be done only one time
Initializing a global dictionary of images will be called exactly once
'''


def loadImages():
    pieces = ['wp', "wR", "wN", "wB", "wQ", "wK", "bp", "bR", "bN", "bB", "bQ", "bK"]

    for piece in pieces:
        IMAGES[piece] = p.image.load("images/" + piece + ".png")
    # Using loops to efficiently loading images
    