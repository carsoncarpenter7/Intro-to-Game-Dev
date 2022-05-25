#! /usr/bin/env python3
# Carson Carpenter
# CPSC 386-02
# 2022-03-07
# carson.carpenter7@csu.fullerton.edu
# @carsoncarpenter7
#
# Lab 02-00
#
# This my DIE class contents
#
""" Module to Generate Random Dice Role """
from random import randrange


class Die:
    """Initialize Die"""

    def __init__(self):
        """Initialize"""
        return

    def roll(self):
        """Random number roll between 1 - 6"""
        return randrange(1, 7)

    @staticmethod
    def none():
        """Fixing pylint errors"""
        return


if __name__ == "__main__":
    DICE = Die()
    for i in range(10):
        print(DICE.roll())
