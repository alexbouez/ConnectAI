#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################
# REQUIREMENTS #
################

import os, sys
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "True"
import pygame, json
import numpy as np
from ctypes import CDLL

# Import settings
def import_settings(settings):
    if os.path.exists(os.path.join(os.getcwd(), 'config.cfg')):
        with open('config.cfg', 'r') as settings_file:
            settings = json.load(settings_file) # load from file
    else:
        with open('config.cfg', 'w') as settings_file:
            json.dump(settings, settings_file)  # write to file

config = {
        'FPS': 30,
        'ROWS': 6,
        'COLS': 7
    }
import_settings(config)
ROWS, COLS = config['ROWS'], config['COLS']

# Ready player1
base = os.path.abspath(os.getcwd())
path_to_player = base + "/bin/player1.so"

try : 
    player1 = CDLL(path_to_player) 
    print("\33[90mINIT\33[0m"+" Player1 ready!") 
except OSError as error : 
    print("\33[31mERROR\33[0m"+" Player1 is not ready. Have you run 'make' already?")
    sys.exit()

# # Testing player 1
# if player1.square(2) == 4:
#     print("'Square' functional.")

##################
# GAME FUNCTIONS #
##################

class Board:
    def __init__(self):
        self.pieces = np.zeros((COLS, ROWS), dtype=int)
        self.turn = 0

    # Return the value of the piece in position (col,row)
    def get_piece(self, col, row):
        return self.pieces[col][row]

    # Check that the board is valid 
    def is_valid(self):
        for i in range(COLS):
            for j in range(ROWS-1):
                if (self.get_piece(i, j + 1) != 0) & (self.get_piece(i, j) == 0):
                    return False
        return True

    # Find the lowest empty space in a column
    def get_top_col(self, col):
        for i in range(ROWS):
            if self.pieces[col][i] == 0:
                return i
        return -1

    # Play a piece in col if possible
    def play_piece(self, col, piece):
        row = self.get_top_col(col)
        if row == -1:
            return -1
        self.pieces[col][row] = piece

    # Check if player piece has won
    def has_won(self, piece):
        # Check rows
        for i in range(COLS-3):
            for j in range(ROWS):
                if self.get_piece(i,j)==piece & self.get_piece(i+1,j)==piece & \
                        self.get_piece(i+2,j)==piece & self.get_piece(i+3,j)==piece:
                    return True
        # Check columns
        for i in range(COLS):
            for j in range(ROWS-3):
                if self.get_piece(i,j)==piece & self.get_piece(i,j+1)==piece & \
                        self.get_piece(i,j+2)==piece & self.get_piece(i,j+3)==piece:
                    return True
        # Check + sloped diagonals
        for i in range(COLS-3):
            for j in range(ROWS-3):
                if self.get_piece(i,j)==piece & self.get_piece(i+1,j+1)==piece & \
                        self.get_piece(i+2,j+2)==piece & self.get_piece(i+3,j+3)==piece:
                    return True
        # Check - sloped diagonals
        for i in range(COLS-3):
            for j in range(3, ROWS):
                if self.get_piece(i,j)==piece & self.get_piece(i+1,j-1)==piece & \
                        self.get_piece(i+2,j-2)==piece & self.get_piece(i+3,j-3)==piece:
                    return True
        return False

#############
# GAME LOOP #
#############

# TODO

###########
# TESTING #
###########

def _test():
    # Testing board init
    test = Board()
    for i in range(ROWS-1):
        test.play_piece(0, 1)
    
    # Testing valid board
    test.play_piece(0, 2)
    if test.is_valid():
        print("\33[32mPASSED\33[0m" + " Current board is valid")
    else:
        print("\33[31mFAILED\33[0m" + " Current board is invalid")
    
    # Testing invalid board
    test.pieces[0][1] = 0
    if not test.is_valid():
        print("\33[32mPASSED\33[0m" + " Altered board is invalid")
    else:
        print("\33[31mFAILED\33[0m" + " Altered board is valid")

    test.pieces =  np.array(
                   [[0, 2, 0, 5, 5, 5],
                    [5, 5, 2, 0, 5, 0],
                    [5, 5, 5, 2, 5, 4],
                    [5, 0, 0, 1, 2, 4],
                    [0, 0, 1, 0, 0, 4],
                    [5, 1, 0, 0, 0, 4],
                    [1, 0, 3, 3, 3, 3]])
    if test.has_won(1) and test.has_won(2) and test.has_won(3) \
            and test.has_won(4) and not test.has_won(5):
        print("\33[32mPASSED\33[0m" + " Win condition")
    else :
        print("\33[31mFAILED\33[0m" + " Win condition")



_test()