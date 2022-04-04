import sys

import numpy as np
import pygame


def create_board():
    board = np.zeros((6,7))
    return board

board = create_board()
game_over = False
turn = 0

while not game_over:
    # ask for player 1 input
    if turn == 0:
        selection = int(input("Player 1 Make your selection (0-6):"))

    # ask for player 2 input
    else:
        selection = int(input("Player 2 Make your selection (0-6):"))
    
    turn += 1
    turn = turn % 2