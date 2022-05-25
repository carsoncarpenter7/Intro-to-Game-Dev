#! /usr/bin/env python3
# Carson Carpenter
# CPSC 386-02
# 2022-03-29
# carson.carpenter7@csu.fullerton.edu
# @carsoncarpenter7
#
# Lab 03-00
#
# This my Blackjack game program with up to 4 players
#
# pylint blackjack.py
# pycodestyle blackjack.py
# black blackjack.py


"""This module is a toy module to demonstrate how to format a Python
    source file."""


from blackjackgame import game


if __name__ == "__main__":
    GAME = game.BlackJackGame()
    GAME.run()
