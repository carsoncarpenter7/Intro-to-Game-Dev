#! /usr/bin/env python3
# Carson Carpenter
# CPSC 386-02
# 2022-03-07
# carson.carpenter7@csu.fullerton.edu
# @carsoncarpenter7
#
# Lab 02-00
#
# This my player class contents
#


""" Player and Computer functions"""


class Player:
    """Player Class Setters and Getters"""

    def __init__(self, name):
        """Initialize"""
        self._name = name
        self._score = 0
        # self._order = order

    @property
    def name(self):
        """Name Getter Property"""
        return self._name

    @property
    def order(self):
        """Order Getter Property"""
        return self._order

    @property
    def score(self):
        """Score Getter Property"""
        return self._score

    @score.setter
    def score(self, new_score):
        """Score Setter Property"""
        self._score = new_score

    @classmethod
    def does_roll(cls):
        """If the user doesnt skip"""
        return True

    @classmethod
    def am_i_human(cls):
        """If it is not the computers turn"""
        return True

    @classmethod
    def are_you_real(cls):
        """If player is a person"""
        return "Yes, I am a human being."

    def __str__(self):
        """Return String Getter"""
        return self._name

    def __repr__(self):
        """Return String Name/Score Getter"""
        return 'Player("{}", {})'.format(self._name, self._score)


class ComputerPlayer(Player):
    """Computer AI Player Class"""

    def __init__(self, score, game):
        """Initialize Computer Player"""
        super().__init__("COMPUTER AI", score)
        self._game = game

    def am_i_human(self):
        """If computers turn"""
        return False

    def are_you_real(self):
        """Verification of Computer Player"""
        return self._game.am_i_real()

    def does_roll(self):
        """Computer doesnt skip their turn"""
        opponent_score = self._game.opponent_score(self)
        if opponent_score > 12:
            return bool(opponent_score)
        return False
