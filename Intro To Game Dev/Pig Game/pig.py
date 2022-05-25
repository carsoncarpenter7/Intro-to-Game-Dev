#! /usr/bin/env python3
# Carson Carpenter
# CPSC 386-02
# 2022-03-07
# carson.carpenter7@csu.fullerton.edu
# @carsoncarpenter7
#
# Lab 02-00
#
# This my Pig game program with up to 4 players
#


"""This module is a toy module to demonstrate how to format a Python
    source file."""


# from piggame import *
from piggame import game

if __name__ == "__main__":
    GAME = game.PigGame()
    GAME.run()
