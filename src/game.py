#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# requirements: pip, pygame, 

import os, sys
from ctypes import CDLL
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "True"
import pygame

# Preparing player1
base = os.path.abspath(os.getcwd())
path_to_player = base + "/bin/player1.so"

try : 
    player1 = CDLL(path_to_player)  
except OSError as error : 
    print("Player1 is not ready. Have you run 'make' already?")
    sys.exit()

if player1.square(2) == 4:
    print("Player1 ready!")
